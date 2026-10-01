# Employee Salary Analysis in R

# Create employee data
employees <- data.frame(
  Name = c("Aman", "Riya", "Rahul", "Priya", "Neha"),
  Department = c("IT", "HR", "IT", "Finance", "HR"),
  Salary = c(55000, 45000, 65000, 60000, 48000),
  Experience = c(2, 3, 5, 4, 2)
)

# Display employee data
print(employees)

# Calculate average salary
average_salary <- mean(Salary)

cat("Average Salary: ₹", average_salary, "\n")

# Find employee with highest salary
highest_salary <- employees[which.max(Salary), ]

cat("Highest Paid Employee:", highest_salaryName, "\n")
cat("Salary: ₹", highest_salary Salary, "\n")

# Find employee with lowest salary
lowest_salary <- employees[which.min(Salary), ]

cat("Lowest Paid Employee:", Name, "\n")
cat("Salary: ₹", sSalary, "\n")

# Calculate average salary by department
department_salary <- aggregate(
  Salary ~ Department,
  data = employees,
  FUN = mean
)

print(department_salary)

# Create salary bar chart
barplot(
  employees$Salary,
  names.arg = employees$Name,
  main = "Employee Salary Analysis",
  xlab = "Employees",
  ylab = "Salary"
)
