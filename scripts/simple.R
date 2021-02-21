library(ggplot2)
library(dplyr)

mtcars %>% 
    ggplot() + 
    geom_point(aes(x = mpg, y = carb)) + 
    ggsave(file = "img/plot.jpeg", device = "jpeg", 
           width = 5, height = 5, units = "in")