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

set.seed(123)  # For reproducibility
install.packages("ipred")
library(e1071)
library(caret)


#Importing File
GroupData <- read.csv(file.choose(),header = T)
#Selecting certain columns
GroupData1 <- GroupData[,c("brand","model_year","milage","accident","HighValueCar")]
#Formatting mileage column to integer
GroupData1[, c(3)] <- sapply(GroupData1[, c(3)], as.integer)

sample_size <- floor(0.7 * nrow(GroupData1))
sample_indices <- sample(nrow(GroupData1), size = sample_size, replace = TRUE)

train_data <- GroupData1[sample_indices, ]
test_data <- GroupData1[-sample_indices, ]

test_data_new <- test_data   
test_data_new$brand[which(!(test_data_new$brand %in% unique(train_data$brand)))] <- NA 
test_data_new

full_group_data<-GroupData1
full_group_data$brand[which(!(full_group_data$brand %in% unique(train_data$brand)))] <- NA 



LogModel <- glm(HighValueCar~ brand + model_year + milage + accident, family="binomial", data = train_data)

summary(LogModel)

predictions <- predict(LogModel,test_data_new, type = "response")
round(predictions,3)
summary(predictions)
predictions

predictions_all <- predict(LogModel,full_group_data, type = "response")
summary(predictions_all)
predictions_all

#Gauging performance of model
LogClass <- as.factor(predictions)
confusion_matrix <- table(Actual = test_data$HighValueCar, Predicted = predictions)
confusion_matrix
accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
round(accuracy,6)
# Convert predicted probabilities to binary predictions using a threshold (e.g., 0.5)
binary_predictions <- ifelse(predictions >= 0.5, 1, 0)

# Create a confusion matrix with binary predictions
confusion_matrix <- table(Actual = test_data$HighValueCar, Predicted = binary_predictions)
confusion_matrix
