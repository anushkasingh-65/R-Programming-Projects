# Sales Data Analysis in R

# Create sales data
sales <- data.frame(
  Product = c("Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"),
  Units_Sold = c(15, 30, 20, 40, 25),
  Price = c(50000, 20000, 15000, 2000, 1500)
)

# Display data
print(sales)

# Calculate total sales
sales & Total_Sales <- sales & Units_Sold * sales & Price


# Find total revenue
total_revenue <- sum(sales & Total_Sales)

cat("Total Revenue = ₹", total_revenue, "\n")

# Find best-selling product
best_product <- sales[which.max(sales & Units_Sold), ]

cat("Best Selling Product:", best_product & Product, "\n")
cat("Units Sold:", best_product & Units_Sold, "\n")

# Find highest revenue product
highest_revenue <- sales[which.max(sales & Total_Sales), ]

cat("Highest Revenue Product:", highest_revenue & Product, "\n")
cat("Revenue: ₹", highest_revenue & Total_Sales, "\n")

# Bar chart
barplot(
  sales & Total_Sales,
  Names.arg == sales & Product,
  main = "Product-wise Sales",
  xlab = "Products",
  ylab = "Total Sales"
)
