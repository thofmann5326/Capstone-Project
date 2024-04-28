#define and choose the dataset
Project<- read.csv(file.choose(), header=T, stringsAsFactors = TRUE)
# Install and load necessary libraries
# install.packages("dummies")
install.packages("dummy")
library("dummy")
#Assuming your dataset is named 'Project'
# Convert categorical variables to dummy variables (one-hot encoding)
# Assuming your dataset is named 'Project'
# Convert categorical variables to dummy variables (one-hot encoding)
Project <- dummy.data.frame(Project, names = c("brand", "model", "fuel_type", "transmission", "ext_col"))

# Convert binary categorical variables to 0s and 1s
Project1$accident <- as.numeric(Project1$accident == "Yes")
Project$clean_title <- as.numeric(Project$clean_title == "Yes")
Project$HighValueCar <- as.numeric(Project$HighValueCar == 1)

# Convert model_year to a factor if needed
Project$model_year <- as.factor(Project$model_year)
str(Project)
write.csv(Project2, file="Project2.csv")
summary(Project2)
str(Project2)
# Remove "mi." and convert milage to numeric
Project2$milage <- as.numeric(gsub("[^0-9.]", "", Project2$milage))
str(Project2)
write.csv(Project2, file="Project2.csv")
# Assuming your dataset is named 'Project2'
library(dummy)

# Specify categorical columns
categorical_columns <- c("brand", "model", "fuel_type", "transmission", "ext_col")

# Convert categorical variables to dummy variables (one-hot encoding)
Project2 <- dummy.data.frame(Project2, names = categorical_columns)

# Remove the original categorical columns
Project2 <- Project2[, !(names(Project2) %in% categorical_columns)]

# Now 'Project2' contains dummy variables for the specified categorical columns
# Install the 'dummy' package (if not installed)
install.packages("dummy")

# Load the 'dummy' package
library("dummy")

# Now try creating dummy variables again
Project2 <- dummy.data.frame(Project2, names = categorical_columns)
# Install the 'dummy' package
install.packages("dummy")

# Load the 'dummy' package
library("dummy")

# Now try creating dummy variables again
Project2 <- dummy.data.frame(Project2, names = categorical_columns)
# Identify categorical columns
categorical_columns <- c("brand", "model", "fuel_type", "transmission", "ext_col")

# Create dummy variables using model.matrix
dummy_variables <- model.matrix(~ 0 + as.factor(Project2[, categorical_columns]))

# Combine dummy variables with the original data
Project2 <- cbind(Project2, dummy_variables)

# Remove the original categorical columns
Project2 <- Project2[, !(names(Project2) %in% categorical_columns)]
install.packages("dummy")
library(dummy)
# Identify categorical columns
categorical_columns <- c("brand", "model", "fuel_type", "transmission", "ext_col")

# Create dummy variables
dummy_variables <- dummy_cols(Project2[, categorical_columns])

# Combine dummy variables with the original data
Project2 <- cbind(Project2, dummy_variables)

# Remove the original categorical columns
Project2 <- Project2[, !(names(Project2) %in% categorical_columns)]

# Load the 'dummy' package
library(dummy)

# Identify categorical columns
categorical_columns <- c("brand", "model", "fuel_type", "transmission", "ext_col")

# Now try creating dummy variables
Project2 <- dummy.data.frame(Project2, names = categorical_columns)

# Check the structure of the modified data
str(Project2)
# Identify categorical columns
categorical_columns <- c("brand", "model", "fuel_type", "transmission", "ext_col")

# Create dummy variables using model.matrix
dummy_variables <- model.matrix(~ 0 + as.factor(Project2[, categorical_columns]))

# Combine dummy variables with the original data
Project2 <- cbind(Project2, dummy_variables)
# Identify categorical columns
categorical_columns <- c("brand", "model", "fuel_type", "transmission", "ext_col")

# Convert categorical columns to factors
Project2[, categorical_columns] <- lapply(Project2[, categorical_columns], as.factor)

# Create dummy variables using model.matrix
dummy_variables <- model.matrix(~ . - 1, data = Project2[, categorical_columns])

# Combine dummy variables with the original data
Project2 <- cbind(Project2, dummy_variables)
str(Project2)
write.csv(Project2, file="Project2.csv")
summary(Project2)
