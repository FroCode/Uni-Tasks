# Install and load the readr package
if (!requireNamespace("readr", quietly = TRUE)) {
  install.packages("readr")
}
library(readr)

# Local path to the CSV file
local_path <- "D:/Programming/issues/Uni-Tasks/data.csv"  # Use forward slashes or double backslashes

# Read the CSV file into a data frame
data <- read_csv(local_path)

# Display the structure of the data frame
str(data)

print(is.data.frame(data))
print(ncol(data))
print(nrow(data))
# Get the max salary from data frame.
calo <- min(data$Km)
print(calo)
fruits <- list(data$Km)

for (x in fruits) {
  s = x + 10
  print(s) 
}