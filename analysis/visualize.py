pip install pandas matplotlib

# ---------------------------------------------------------------------------
# Chart 1: return_rate_by_payment.png
# ---------------------------------------------------------------------------
ret = (
    merged.groupby("payment_method")["returned"]
    .mean()
    .mul(100)
    .round(1)
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(ret.index, ret.values, color=["#e74c3c", "#3498db", "#2ecc71"])
ax.set_ylabel("Return Rate (%)")
ax.set_xlabel("Payment Method")
ax.set_title("COD Returns at 44.4% — 3x Card")
ax.set_ylim(0, max(ret.values) * 1.25)

for bar, val in zip(bars, ret.values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1.0,
        f"{val}%",
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold"
    )

plt.tight_layout()
plt.savefig("visualizations/return_rate_by_payment.png", dpi=150)
plt.close()
print("Saved: visualizations/return_rate_by_payment.png")
print(f"Return rates (descending): {ret.to_dict()}")

# ---------------------------------------------------------------------------
# Chart 2: monthly_revenue_trend.png  (outlier-corrected)
# ---------------------------------------------------------------------------
merged["order_date"] = pd.to_datetime(merged["order_date"])
merged["year_month"] = merged["order_date"].dt.to_period("M")

monthly_clean = (
    merged.loc[~merged["is_outlier"]]
    .groupby("year_month")["order_value"]
    .sum()
    .sort_index()
)

labels = [str(p) for p in monthly_clean.index]
values = monthly_clean.values

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(labels, values, marker="o", linewidth=2, markersize=8, color="#2980b9")
ax.set_xlabel("Month")
ax.set_ylabel("Total Order Value (INR)")
ax.set_title("Monthly Revenue Trend (Outlier-Corrected) — Peak in March 2026")
ax.grid(True, linestyle="--", alpha=0.5)

# Annotate the real peak (March)
peak_idx = values.argmax()
ax.annotate(
    f"Peak: {values[peak_idx]:,.0f} INR",
    xy=(peak_idx, values[peak_idx]),
    xytext=(peak_idx, values[peak_idx] + 1500),
    ha="center",
    fontsize=10,
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="black")
)

plt.tight_layout()
plt.savefig("visualizations/monthly_revenue_trend.png", dpi=150)
plt.close()
print("Saved: visualizations/monthly_revenue_trend.png")
print(f"Outlier-corrected monthly totals: {dict(zip(labels, [round(v, 2) for v in values]))}")

print("\nBoth visualizations generated successfully.")
