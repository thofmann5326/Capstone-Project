set.seed(123)  # For reproducibility
install.packages("rpart")
library(rpart)
install.packages("rpart.plot")
library(rpart.plot)

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

summary(train_data)
names(train_data)
dim(train_data)

attach(train_data)

#HighValueCar is target attribute using four other attributes to predict this one variable
DecisionTree <- rpart(HighValueCar ~ brand + model_year + milage + accident , method = "class")

summary(DecisionTree)

#Formatting the decision tree to read more easily
prp(DecisionTree,extra = 102,faclen = 0, varlen =0,digits=-3 ,split.border.col = "darkgray")

PredictTree <- predict(DecisionTree,newdata = data_test_new, type = "class")

#Gauging performance of model
confusion_matrix <- table(Actual = test_data$HighValueCar, Predicted = PredictTree)
summarry(confusion_matrix)
accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
accuracy

#predicting the values in the predictions dataset
predictions <- predict(DecisionTree, newdata = test_data_new, type = "class")

#predicting the values in the overall dataset
predictions_all <- predict(DecisionTree, newdata = full_group_data, type = "class")
#creating new column called Predicted_HighValueCar to compare results to original column HighValueCar column
GroupData1$Predicted_HighValueCar <- predictions_all

write.csv(GroupData1, "Decision_Tree_with_Predictions.csv", row.names = FALSE)
