library(tidyverse)

mtcars %>% head(2) %>% write.csv("data/test.csv")