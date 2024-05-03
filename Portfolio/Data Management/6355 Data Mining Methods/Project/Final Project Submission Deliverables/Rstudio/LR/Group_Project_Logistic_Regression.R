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


