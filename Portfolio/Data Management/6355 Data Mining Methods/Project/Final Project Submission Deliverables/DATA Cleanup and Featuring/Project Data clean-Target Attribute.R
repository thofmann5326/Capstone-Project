#define and choose the dataset
Project<- read.csv(file.choose(), header=T)
# Set the threshold for high-value cars
threshold_price <- 51074

# Create a new column 'HighValueCar' based on the threshold
Project$HighValueCar <- ifelse(Project$price >= threshold_price, 1, 0)
print(summary(Project$HighValueCar))
str(Project)
summary(Project)
write.csv(Project, file="Project.csv")
summary(Project$price)
threshold_price <- 51074
print(head(Project))
print(summary(Project$HighValueCar))
# Convert 'price' to numeric
Project$price <- as.numeric(gsub("[^0-9.]", "", Project$price)) 
threshold_price <- 51074
Project$HighValueCar <- ifelse(Project$price >= threshold_price, 1, 0)
summary(Project$HighValueCar)
str(Project)
write.csv(Project, file="Project.csv")
Project2 <- read.csv(file.choose(), header=T)
# Create a new column 'engine_power_numeric' using regular expressions
Project2$engine_power_numeric <- as.numeric(gsub("[^0-9.]", "", Project2$engine))

# Identify non-numeric entries
non_numeric_values <- is.na(Project2$engine_power_numeric)

# Replace non-numeric entries with NA
Project2$engine_power_numeric[non_numeric_values] <- NA

# Print the first few rows of the updated data
print(head(Project2[, c("engine", "engine_power_numeric")]))
write.csv(Project2, file="Project2.csv")
