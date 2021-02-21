library(ggplot2)
library(dplyr)

mtcars %>% 
    ggplot() + 
    geom_point(aes(x = mpg, y = carb)) + 
    labs(title = format(Sys.time(), "%Y-%m-%d, %H:%M"))
    ggsave(file = "img/plot.png", device = "png", 
           width = 5, height = 5, units = "in")