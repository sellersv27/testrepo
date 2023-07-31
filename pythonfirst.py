# Bar Plot
count_cyl=table(mtcars$cyl)
barplot(count_cyl, main='Count of Cars by Cylinder',
        xlab= 'Number of Cylinders',
        ylab= 'Count of Cars',
        col= c('darkred', 'green', 'orange'))
