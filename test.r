#library(readr)
library(tidyverse)
library(readr)
# Local path to the CSV file
local_path <- "D:/Programming/issues/Uni-Tasks/data.csv"  # Use forward slashes or double backslashes

# Read the CSV file into a data frame
data <- read_csv(local_path)

# Display the structure of the data frame
str(data)

print(data)

