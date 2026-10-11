import os
os.makedirs("data", exist_ok=True)
os.makedirs("visualizations", exist_ok=True)

# ---------- customers.csv ----------
customers_csv = """customer_id,name,city,city_tier,signup_date,acquisition_source
C001,Aarav,Mumbai,1,2026-01-07,Organic
C002,Vivaan,Delhi,1,2026-02-27,Referral
C003,Aditi,Mumbai,1,2026-06-23,Organic
C004,Ananya,Lucknow,2,2026-01-23,Organic
C005,Ishaan,Mumbai,1,2026-01-08,Referral
C006,Diya,Delhi,1,2026-05-10,Organic
C007,Kabir,Lucknow,2,2026-02-20,Organic
C008,Meera,Lucknow,2,2026-04-18,Ad
C009,Rohan,Lucknow,2,2026-03-13,Social
C010,Sara,Mumbai,1,2026-02-10,Organic
C011,Arjun,Bangalore,1,2026-03-13,Referral
C012,Priya,Bangalore,1,2026-01-27,Referral
C013,Karan,Mumbai,1,2026-04-02,Social
C014,Neha,Lucknow,2,2026-03-09,Social
C015,Yash,Jaipur,2,2026-05-18,Referral
C016,Pooja,Jaipur,2,2026-01-21,Organic
C017,Rahul,Lucknow,2,2026-04-03,Organic
C018,Simran,Mumbai,1,2026-01-12,Organic
C019,Dev,Bangalore,1,2026-01-21,Social
C020,Tara,Mumbai,1,2026-04-08,Ad
C021,Aryan,Bangalore,1,2026-02-11,Ad
C022,Kavya,Delhi,1,2026-06-21,Ad
C023,Nikhil,Mumbai,1,2026-06-05,Organic
C024,Riya,Lucknow,2,2026-03-04,Referral
C025,Varun,Jaipur,2,2026-03-11,Social
C026,Isha,Lucknow,2,2026-02-26,Organic
C027,Manav,Mumbai,1,2026-02-28,Social
C028,Shreya,Bangalore,1,2026-04-13,Ad
C029,Tanish,Delhi,1,2026-05-26,Social
C030,Anika,Bangalore,1,2026-02-24,Organic
C031,Aditya,Jaipur,2,2026-06-14,Ad
C032,Naina,Bangalore,1,2026-02-05,Ad
C033,Siddharth,Lucknow,2,2026-05-18,Ad
C034,Zara,Lucknow,2,2026-04-20,Social
C035,Krishna,Jaipur,2,2026-04-03,Ad
C036,Aisha,Delhi,1,2026-05-11,Ad
C037,Rudra,Mumbai,1,2026-01-29,Referral
C038,Myra,Delhi,1,2026-06-24,Ad
C039,Om,Mumbai,1,2026-04-09,Ad
C040,Vanya,Jaipur,2,2026-05-16,Ad
C041,Ayaan,Lucknow,2,2026-01-03,Organic
C042,Sanya,Mumbai,1,2026-06-24,Social
C043,Reyansh,Bangalore,1,2026-06-14,Ad
C044,Aria,Bangalore,1,2026-04-22,Referral
C045,Vihaan,Mumbai,1,2026-03-09,Social
"""
with open("data/customers.csv", "w") as f:
    f.write(customers_csv)

# ---------- products.csv ----------
products_csv = """product_id,product_name,category,price
P01,Onion Hair Oil,Haircare,349
P02,Onion Shampoo,Haircare,399
P03,Argan Hair Mask,Haircare,599
P04,Anti-Hairfall Serum,Haircare,649
P05,Rice Water Conditioner,Haircare,349
P06,Vitamin C Face Wash,Skincare,249
P07,Vitamin C Serum,Skincare,699
P08,Tea Tree Face Wash,Skincare,229
P09,Ubtan Face Mask,Skincare,299
P10,Rice Sunscreen SPF50,Skincare,449
P11,Milky Soft Baby Lotion,Babycare,299
P12,Baby Shampoo,Babycare,249
P13,Baby Massage Oil,Babycare,279
P14,Charcoal Deodorant,PersonalCare,199
P15,Tea Tree Body Wash,PersonalCare,349
P16,Aloe Vera Gel,PersonalCare,199
"""
with open("data/products.csv", "w") as f:
    f.write(products_csv)

# ---------- orders.csv ----------
orders_csv = """order_id,customer_id,product_id,order_date,quantity,discount_pct,payment_method,rating,returned
O0001,C012,P04,2026-03-18,2,10,upi,2,0
O0002,C024,P06,2026-05-16,1,30,UPI,1,0
O0003,C008,P12,2026-03-20,2,0,COD,1,1
O0004,C032,P03,2026-05-17,3,30,UPI,5,0
O0005,C011,P09,2026-06-05,1,10,Card,3,0
O0006,C026,P12,2026-05-13,1,0,Card,3,0
O0007,C002,P08,2026-01-02,1,10,COD,1,0
O0008,C003,P11,2026-03-02,1,10,COD,,0
O0009,C037,P16,2026-05-02,1,0,UPI,4,0
O0010,C023,P14,2026-01-14,1,0,Card,1,0
O0011,C026,P11,2026-01-28,25,0,COD,2,1
O0012,C028,P06,2026-03-05,1,0,UPI,1,1
O0013,C042,P01,2026-03-02,3,,COD,4,0
O0014,C004,P06,2026-04-10,1,30,cod,3,0
O0015,C028,P16,2026-03-17,1,,COD,3,1
O0016,C004,P02,2026-05-09,1,0,UPI,5,0
O0017,C006,P06,2026-01-18,1,,Card,5,0
O0018,C016,P02,2026-04-18,2,20,CARD,3,0
O0019,C014,P11,2026-04-12,1,30,COD,3,0
O0020,C005,P01,2026-05-25,1,10,UPI,5,1
O0021,C017,P05,2026-01-18,3,10,UPI,,0
O0022,C035,P10,2026-06-17,2,20,Card,1,0
O0023,C009,P09,2026-01-28,1,20,Card,5,0
O0024,C014,P11,2026-06-12,1,20,UPI,1,0
O0025,C006,P14,2026-01-12,2,20,COD,2,0
O0026,C029,P14,2026-01-29,1,10,COD,5,0
O0027,C003,P12,2026-02-07,1,20,card,1,1
O0028,C023,P07,2026-06-20,2,30,COD,5,0
O0029,C010,P08,2026-02-15,2,20,UPI,4,1
O0030,C043,P08,2026-06-29,1,,COD,2,0
O0031,C013,P15,2026-02-28,1,30,COD,3,0
O0032,C018,P03,2026-03-13,3,,Card,1,0
O0033,C008,P09,2026-03-09,1,20,COD,3,0
O0034,C028,P04,2026-05-28,1,30,COD,1,1
O0035,C034,P07,2026-01-18,1,20,UPI,1,0
O0036,C020,P10,2026-03-25,2,,Card,2,0
O0037,C027,P13,2026-02-14,2,0,Card,3,0
O0038,C019,P07,2026-05-29,1,30,Card,4,0
O0039,C044,P07,2026-02-13,1,20,Card,1,0
O0040,C016,P10,2026-02-20,1,30,cod,5,1
O0041,C005,P15,2026-06-11,1,30,Card,4,0
O0042,C026,P08,2026-06-26,1,0,COD,4,0
O0043,C015,P06,2026-06-28,2,10,Card,1,1
O0044,C030,P05,2026-06-20,2,20,Card,4,0
O0045,C040,P14,2026-05-21,2,30,Card,4,0
O0046,C017,P08,2026-03-12,2,10,UPI,3,0
O0047,C029,P03,2026-03-02,2,0,COD,2,1
O0048,C010,P08,2026-02-09,1,30,Card,3,1
O0049,C035,P15,2026-02-22,1,0,UPI,5,0
O0050,C025,P16,2026-04-01,1,30,COD,5,1
O0051,C035,P08,2026-03-11,1,20,Card,4,1
O0052,C011,P15,2026-06-09,3,0,CARD,1,0
O0053,C042,P14,2026-04-29,1,20,cod,,1
O0054,C030,P11,2026-04-08,1,30,COD,,0
O0055,C006,P16,2026-05-19,1,10,COD,1,0
O0056,C042,P02,2026-03-05,2,10,COD,2,1
O0057,C009,P16,2026-05-25,2,20,UPI,3,0
O0058,C011,P04,2026-02-11,2,0,UPI,3,0
O0059,C037,P13,2026-02-20,1,10,COD,1,0
O0060,C020,P04,2026-05-25,2,30,UPI,3,0
O0061,C005,P11,2026-04-18,1,20,UPI,4,0
O0062,C010,P14,2026-05-14,1,30,UPI,4,0
O0063,C028,P09,2026-03-04,1,30,UPI,2,1
O0064,C030,P13,2026-05-07,1,10,UPI,3,0
O0065,C017,P11,2026-06-02,1,0,Card,5,0
O0066,C013,P03,2026-04-15,1,30,card,4,0
O0067,C029,P01,2026-02-26,1,20,Card,4,0
O0068,C036,P12,2026-05-21,1,20,Card,3,0
O0069,C017,P08,2026-02-19,1,10,CARD,2,0
O0070,C014,P16,2026-05-31,1,20,UPI,1,0
O0071,C013,P10,2026-02-15,1,10,Card,3,0
O0072,C003,P02,2026-06-28,1,30,UPI,1,0
O0073,C001,P10,2026-04-23,1,20,Card,,0
O0074,C008,P03,2026-01-19,1,10,Card,2,0
O0075,C037,P10,2026-03-05,1,10,COD,5,0
O0076,C025,P15,2026-03-18,3,20,UPI,5,0
O0077,C040,P02,2026-01-26,2,10,UPI,3,0
O0078,C043,P03,2026-02-14,1,30,Card,4,0
O0079,C039,P16,2026-03-01,1,30,cod,,1
O0080,C044,P08,2026-06-10,3,,Card,4,0
O0081,C008,P08,2026-03-10,2,10,UPI,3,1
O0082,C039,P10,2026-04-30,1,,Card,5,0
O0083,C035,P16,2026-06-03,1,20,COD,5,0
O0084,C017,P01,2026-06-22,1,0,UPI,3,0
O0085,C037,P02,2026-02-14,2,,Card,2,0
O0086,C038,P14,2026-05-06,2,30,UPI,3,0
O0087,C021,P04,2026-03-26,2,30,Card,5,0
O0088,C003,P15,2026-03-06,1,30,Card,,0
O0089,C001,P15,2026-02-18,1,30,Card,4,0
O0090,C004,P07,2026-02-03,1,30,UPI,1,0
O0091,C002,P08,2026-03-21,2,0,Card,2,0
O0092,C008,P15,2026-06-15,3,20,upi,5,0
O0093,C018,P14,2026-05-01,2,30,COD,2,0
O0094,C039,P05,2026-03-12,2,20,UPI,5,0
O0095,C018,P01,2026-03-18,1,30,UPI,,0
O0096,C029,P16,2026-05-22,1,20,UPI,2,0
O0097,C016,P13,2026-04-16,1,30,COD,4,0
O0098,C043,P05,2026-01-10,30,0,COD,1,0
O0099,C029,P04,2026-04-27,1,10,COD,1,1
O0100,C031,P09,2026-06-27,1,20,Card,5,1
O0101,C025,P11,2026-05-05,2,0,UPI,2,1
O0102,C041,P10,2026-01-24,3,0,Card,4,1
O0103,C011,P10,2026-01-12,3,20,CARD,3,1
O0104,C028,P05,2026-04-16,1,10,Card,2,0
O0105,C006,P13,2026-03-03,2,10,card,4,0
O0106,C041,P09,2026-06-20,1,20,COD,5,0
O0107,C011,P03,2026-03-30,1,30,UPI,3,0
O0108,C030,P10,2026-04-09,1,30,UPI,5,0
O0109,C023,P10,2026-03-17,3,30,COD,3,0
O0110,C001,P02,2026-05-08,3,10,UPI,5,0
O0111,C023,P08,2026-06-08,2,10,COD,1,0
O0112,C041,P02,2026-04-23,1,10,COD,1,1
O0113,C019,P11,2026-02-14,2,20,COD,5,0
O0114,C033,P09,2026-03-07,2,20,UPI,3,0
O0115,C008,P15,2026-02-06,3,30,UPI,5,0
O0116,C024,P03,2026-01-04,2,20,COD,3,1
O0117,C038,P13,2026-04-06,2,0,COD,5,1
O0118,C036,P11,2026-02-26,3,30,card,,0
O0119,C042,P14,2026-01-12,1,30,UPI,1,0
O0120,C007,P08,2026-02-04,2,30,CARD,5,0
O0121,C010,P14,2026-05-06,2,20,Card,1,0
O0122,C024,P07,2026-03-02,1,20,UPI,5,1
O0123,C042,P12,2026-03-12,1,30,COD,1,1
O0124,C043,P07,2026-06-02,2,20,UPI,,1
O0125,C009,P07,2026-05-22,1,10,COD,3,1
O0126,C010,P01,2026-02-07,1,10,UPI,1,0
O0127,C043,P01,2026-04-02,1,20,UPI,1,0
O0128,C012,P09,2026-04-18,1,30,Card,4,0
O0129,C024,P04,2026-02-26,1,20,UPI,4,1
O0130,C042,P01,2026-05-03,1,0,UPI,4,0
O0131,C029,P03,2026-03-24,2,20,card,5,1
O0132,C041,P11,2026-06-02,1,30,Card,1,0
O0133,C008,P07,2026-02-28,1,30,Card,4,0
O0134,C007,P11,2026-06-20,1,30,COD,,0
O0135,C006,P03,2026-01-25,1,10,Card,5,0
O0136,C004,P11,2026-04-16,2,30,Card,1,0
O0137,C019,P10,2026-05-28,1,30,CARD,2,0
O0138,C007,P12,2026-04-05,2,10,COD,4,1
O0139,C036,P01,2026-06-18,2,10,UPI,3,0
O0140,C020,P11,2026-02-16,1,30,UPI,1,0
O0141,C010,P01,2026-05-16,1,20,COD,2,1
O0142,C024,P10,2026-05-26,2,10,Card,2,0
O0143,C040,P02,2026-03-11,2,30,Card,4,0
O0144,C018,P07,2026-01-30,2,30,card,5,0
O0145,C043,P10,2026-04-12,1,10,UPI,3,1
O0146,C014,P05,2026-03-16,2,30,Card,2,1
O0147,C009,P13,2026-02-28,1,20,Card,1,0
O0148,C026,P02,2026-04-28,1,30,UPI,5,0
O0149,C026,P14,2026-04-14,1,30,COD,,1
O0150,C006,P14,2026-03-04,2,0,Card,4,0
O0151,C020,P11,2026-02-13,1,10,COD,3,0
O0152,C023,P05,2026-02-07,1,,COD,1,1
O0153,C012,P16,2026-05-25,1,20,UPI,3,0
O0154,C010,P15,2026-04-24,1,0,CARD,3,0
O0155,C033,P03,2026-04-26,1,20,COD,1,1
O0156,C042,P03,2026-05-10,2,,Card,4,0
O0157,C037,P07,2026-05-02,1,30,card,1,0
O0158,C022,P03,2026-02-14,1,30,COD,5,0
O0159,C034,P06,2026-03-14,1,0,Card,3,0
O0160,C005,P11,2026-06-23,1,10,Card,3,0
O0161,C006,P05,2026-03-21,3,30,UPI,2,0
O0162,C039,P03,2026-04-07,1,10,Card,5,0
O0163,C006,P14,2026-01-05,1,10,Card,,0
O0164,C032,P07,2026-02-05,1,0,COD,,1
O0165,C035,P02,2026-06-08,2,10,COD,2,1
O0166,C040,P06,2026-01-12,2,10,Card,4,0
O0167,C040,P10,2026-04-25,2,30,COD,2,1
O0168,C024,P15,2026-03-14,1,30,UPI,,0
O0169,C013,P05,2026-01-14,2,,Card,5,0
O0170,C008,P10,2026-02-11,1,10,cod,4,0
O0171,C006,P08,2026-03-31,2,30,UPI,5,0
O0172,C024,P08,2026-01-21,1,0,Card,3,1
O0173,C010,P05,2026-05-01,1,30,Card,4,0
O0174,C040,P01,2026-01-05,3,30,COD,1,0
O0175,C019,P08,2026-01-13,1,30,COD,1,0
O0176,C032,P03,2026-05-17,3,30,UPI,5,0
O0177,C005,P15,2026-06-11,1,30,Card,4,0
O0178,C008,P08,2026-03-10,2,10,UPI,3,1
O0179,C010,P14,2026-05-06,2,20,Card,1,0
O0180,C020,P11,2026-02-13,1,10,COD,3,0
"""
with open("data/orders.csv", "w") as f:
    f.write(orders_csv)

print("All 3 CSV files created successfully!")


import pandas as pd
import numpy as np


# Task 1 — Load and inspect


customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")

print(f"orders.shape before any cleaning: {orders.shape}")
assert orders.shape == (180, 9)

print("\ncustomers.shape:", customers.shape)
print("products.shape:", products.shape)
print("\norders head:")
print(orders.head())
print("\norders null counts:")
print(orders.isnull().sum())


# Task 2 — Standardize payment_method casing


print("Before fix — unique payment_method values:")
print(sorted(orders["payment_method"].unique().tolist()))
print(f"Number of distinct raw values: {orders['payment_method'].nunique()}")
assert orders["payment_method"].nunique() == 7

orders["payment_method"] = orders["payment_method"].str.strip().str.upper()

print("\nAfter fix — unique payment_method values:")
print(sorted(orders["payment_method"].unique().tolist()))
print("\nValue counts after standardization:")
print(orders["payment_method"].value_counts().sort_index())
assert orders["payment_method"].nunique() == 3
assert orders["payment_method"].value_counts()["CARD"] == 70
assert orders["payment_method"].value_counts()["UPI"] == 55
assert orders["payment_method"].value_counts()["COD"] == 55


# Task 3 — Remove duplicate orders


natural_key = [
    "customer_id", "product_id", "order_date", "quantity",
    "discount_pct", "payment_method", "rating", "returned",
]

dup_mask = orders.duplicated(subset=natural_key, keep="first")
dropped = orders.loc[dup_mask, "order_id"].tolist()
print(f"Number of duplicate rows flagged: {dup_mask.sum()}")
print(f"Dropped order_id values: {dropped}")
assert dup_mask.sum() == 5
assert set(dropped) == {"O0176", "O0177", "O0178", "O0179", "O0180"}

orders_clean = orders[~dup_mask].copy()
print(f"orders_clean.shape after dropping duplicates: {orders_clean.shape}")
assert orders_clean.shape == (175, 9)

dropped_rows = orders.loc[dup_mask].copy()


# Task 4 — Impute missing values

n_discount_na = orders_clean["discount_pct"].isnull().sum()
print(f"discount_pct missing rows (on deduplicated frame): {n_discount_na}")
assert n_discount_na == 12
orders_clean["discount_pct"] = orders_clean["discount_pct"].fillna(0)

median_rating = orders_clean["rating"].median()
print(f"Median of non-null ratings (before imputing): {median_rating}")
assert median_rating == 3.0
n_rating_na = orders_clean["rating"].isnull().sum()
print(f"rating missing rows (on deduplicated frame): {n_rating_na}")
assert n_rating_na == 15
orders_clean["rating"] = orders_clean["rating"].fillna(median_rating)

print("\nAfter imputation — null counts:")
null_after = orders_clean[["discount_pct", "rating"]].isnull().sum()
print(null_after.to_dict())
assert null_after["discount_pct"] == 0 and null_after["rating"] == 0


# Task 5 — Merge and reconcile


merged = (
    orders_clean
    .merge(products, on="product_id", how="left")
    .merge(customers, on="customer_id", how="left")
)

merged["order_value"] = (
    merged["quantity"] * merged["price"] * (1 - merged["discount_pct"] / 100)
)

total_order_value = merged["order_value"].sum()
print(f"Total order_value across 175 cleaned rows: {total_order_value:.2f}")
assert abs(total_order_value - 97358.30) < 0.01

dropped_merged = (
    dropped_rows
    .merge(products, on="product_id", how="left")
    .merge(customers, on="customer_id", how="left")
)
dropped_merged["discount_pct"] = dropped_merged["discount_pct"].fillna(0)
dropped_merged["order_value"] = (
    dropped_merged["quantity"] * dropped_merged["price"] * (1 - dropped_merged["discount_pct"] / 100)
)
dropped_value_sum = dropped_merged["order_value"].sum()
print(f"Combined order_value of the 5 dropped duplicate rows: {dropped_value_sum:.2f}")
assert abs(dropped_value_sum - 2501.90) < 0.01

print(
    "\nRECONCILIATION NOTE: The cleaned total order_value of ₹97,358.30 is "
    "exactly ₹2,501.90 less than Part 1 Report (a)'s raw total of ₹99,860.20. "
    "This entire delta is attributable solely to the 5 duplicate rows removed in "
    "Task 3 (order_ids O0176–O0180). Their combined order_value is ₹2,501.90 "
    "(verified by independently summing order_value on those five rows after "
    "joining to products). Discount and rating imputation do not affect any "
    "order_value calculation, because order_value depends only on quantity, "
    "price and discount_pct, and the missing discount_pct values were already "
    "treated as zero under the same business rule used for imputation."
)


# Task 6 — IQR outlier detection


Q1 = merged["quantity"].quantile(0.25)
Q3 = merged["quantity"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(f"Q1 = {Q1}, Q3 = {Q3}, IQR = {IQR}, lower = {lower}, upper = {upper}")
assert Q1 == 1.0 and Q3 == 2.0 and IQR == 1.0 and lower == -0.5 and upper == 3.5

merged["is_outlier"] = (merged["quantity"] < lower) | (merged["quantity"] > upper)
outlier_rows = merged.loc[merged["is_outlier"], ["order_id", "quantity"]]
print("\nOutlier rows (flagged, not dropped):")
print(outlier_rows.to_string(index=False))
assert len(outlier_rows) == 2
assert set(outlier_rows["order_id"]) == {"O0011", "O0098"}


# Task 7 — Hypothesis: COD higher return rate?


print("HYPOTHESIS: COD (Cash on Delivery) orders have a higher return rate than CARD or UPI orders.")

ret_by_pay = (
    merged.groupby("payment_method")["returned"]
    .agg(["count", "mean"])
    .rename(columns={"mean": "return_rate"})
)
ret_by_pay["return_rate_pct"] = (ret_by_pay["return_rate"] * 100).round(1)
print("\nReturn rate by payment_method:")
print(ret_by_pay)

assert abs(ret_by_pay.loc["CARD", "return_rate_pct"] - 14.7) < 0.1
assert abs(ret_by_pay.loc["COD", "return_rate_pct"] - 44.4) < 0.1
assert abs(ret_by_pay.loc["UPI", "return_rate_pct"] - 18.9) < 0.1

print("\nHYPOTHESIS STATUS: Confirmed — COD return rate (44.4%) is substantially higher than CARD (14.7%) and UPI (18.9%).")


# Task 8 — Multi-level segmentation


seg = (
    merged.groupby(["payment_method", "city_tier"])["returned"]
    .agg(["count", "mean"])
    .rename(columns={"mean": "return_rate"})
)
seg["return_rate_pct"] = (seg["return_rate"] * 100).round(1)
print("Return rate by payment_method × city_tier:")
print(seg)

cod_tier2 = seg.loc[("COD", 2), "return_rate_pct"]
cod_tier1 = seg.loc[("COD", 1), "return_rate_pct"]
print(
    f"\nHighest-risk segment: COD + Tier-2 cities at {cod_tier2}% "
    f"({int(seg.loc[('COD', 2), 'count'])} Tier-2 COD orders), "
    f"versus COD + Tier-1 at {cod_tier1}% "
    f"({int(seg.loc[('COD', 1), 'count'])} Tier-1 COD orders). "
    "COD risk is not uniform across tiers — the blended COD rate hides the "
    "concentration of the problem in Tier-2 cities."
)
assert abs(cod_tier2 - 54.5) < 0.1
assert abs(cod_tier1 - 37.5) < 0.1


# Task 9 — Correlation analysis


corr_cols = ["rating", "returned", "discount_pct", "quantity"]
corr_matrix = merged[corr_cols].corr()
print("Correlation matrix:")
print(corr_matrix.round(4))

def strength_band(r):
    abs_r = abs(r)
    if abs_r < 0.2: return "negligible"
    elif abs_r < 0.4: return "weak"
    elif abs_r < 0.7: return "moderate"
    else: return "strong"

print("\nPairwise correlation strength labels:")
pairs = [
    ("rating", "returned"), ("rating", "discount_pct"), ("rating", "quantity"),
    ("returned", "discount_pct"), ("returned", "quantity"), ("discount_pct", "quantity"),
]
for a, b in pairs:
    r = corr_matrix.loc[a, b]
    print(f"  {a} vs {b}: r = {r:.4f} → {strength_band(r)}")
    assert abs(r) < 0.2

disc_ret_r = corr_matrix.loc["discount_pct", "returned"]
print(f'\nHypothesis "higher discounts reduce returns" is Busted (discount_pct vs returned ≈ {disc_ret_r:.2f}).')


# Task 10 — Outlier-corrected time series

merged["order_date"] = pd.to_datetime(merged["order_date"])
merged["year_month"] = merged["order_date"].dt.to_period("M")

monthly_all = merged.groupby("year_month")["order_value"].sum().sort_index()
print("Monthly total order_value INCLUDING outliers:")
for ym, val in monthly_all.items():
    print(f"  {ym}: {val:.2f}")

assert abs(monthly_all.loc["2026-01"] - 29582.10) < 0.1

monthly_clean = (
    merged.loc[~merged["is_outlier"]]
    .groupby("year_month")["order_value"]
    .sum()
    .sort_index()
)
print("\nMonthly total order_value EXCLUDING outliers (outlier-corrected):")
for ym, val in monthly_clean.items():
    print(f"  {ym}: {val:.2f}")

assert abs(monthly_clean.loc["2026-01"] - 11637.10) < 0.1
assert abs(monthly_clean.loc["2026-03"] - 20318.90) < 0.1

print(
    "\nJanuary's apparent lead (₹29,582.10) is an artifact of the two bulk "
    "outlier orders landing in January (O0011 on 2026-01-28 with quantity 25, "
    "O0098 on 2026-01-10 with quantity 30). Once those two rows are excluded, "
    "March becomes the genuine peak month at ₹20,318.90."
)

print("\n" + "=" * 60)
print("ALL TASKS 1–10 COMPLETED SUCCESSFULLY")
print("=" * 60)
