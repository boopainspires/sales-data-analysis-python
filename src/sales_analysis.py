from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project_root = Path(__file__).resolve().parents[1]
data_file = project_root / "data" / "sales_data.csv"
visuals_dir = project_root / "visuals"

visuals_dir.mkdir(exist_ok=True)

df = pd.read_csv(data_file)

df["Revenue"] = df["Quantity"] * df["Price"]

total_revenue = df["Revenue"].sum()

revenue_by_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
revenue_by_category = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
revenue_by_city = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
top_customers = df.groupby("Customer")["Revenue"].sum().sort_values(ascending=False)

best_product = revenue_by_product.idxmax()
best_product_revenue = revenue_by_product.max()

best_category = revenue_by_category.idxmax()
best_category_revenue = revenue_by_category.max()

best_city = revenue_by_city.idxmax()
best_city_revenue = revenue_by_city.max()

best_customer = top_customers.idxmax()
best_customer_revenue = top_customers.max()

print("Total Revenue:", total_revenue)

print("\nRevenue by Product:")
print(revenue_by_product)

print("\nRevenue by Category:")
print(revenue_by_category)

print("\nRevenue by City:")
print(revenue_by_city)

print("\nTop Customers:")
print(top_customers)

print("\nSimple Insights:")
print("1. Total revenue is", total_revenue)
print("2. Best product is", best_product, "with revenue", best_product_revenue)
print("3. Best category is", best_category, "with revenue", best_category_revenue)
print("4. Best city is", best_city, "with revenue", best_city_revenue)
print("5. Top customer is", best_customer, "with spending", best_customer_revenue)

plt.figure(figsize=(8, 5))
revenue_by_product.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(visuals_dir / "revenue_by_product.png")
plt.show()

plt.figure(figsize=(6, 5))
revenue_by_category.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(visuals_dir / "revenue_by_category.png")
plt.show()

plt.figure(figsize=(7, 5))
revenue_by_city.plot(kind="bar")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(visuals_dir / "revenue_by_city.png")
plt.show()