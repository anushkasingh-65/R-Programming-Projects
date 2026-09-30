# Student Marks Analysis using R

# Student names
students <- c("Anu", "Rahul", "Priya", "Aman", "Neha")

# Marks in three subjects
Maths <- c(85, 72, 90, 65, 78)
Science <- c(88, 75, 92, 70, 80)
English <- c(82, 80, 85, 68, 75)

# Create data frame
data <- data.frame(
  Student = students,
  Maths = Maths,
  Science = Science,
  English = English
)

# Calculate total marks
data$Total <- data$Maths + data$Science + data$English

# Calculate percentage
data$Percentage <- data$Total / 3

# Display student data
print(data)

# Find average percentage
average <- mean(data$Percentage)

cat("Average Percentage:", average, "%\n")

# Find student with highest percentage
top_student <- data$Student[which.max(data$Percentage)]

cat("Top Student:", top_student, "\n")

# Display students who scored above 80%
cat("Students scoring above 80%:\n")
print(data$Student[data$Percentage > 80])

# Bar chart of student percentages
barplot(
  data$Percentage,
  names.arg = data$Student,
  main = "Student Percentage",
  xlab = "Students",
  ylab = "Percentage"
)
