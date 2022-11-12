mba <- read.csv("E:/New Daywise Data/Day 4-R intro/mba.csv")


barplot(mba$gmat)


hist(mba$gmat)
hist(mba$workex)


boxplot(mba$gmat)
boxplot(mba$workex)
boxplot(mba$gmat, horizontal = T)

mean(mba$workex)
sd(mba$workex)

mean(mba$gmat)
sd(mba$gmat)

install.packages("moments")
library(moments)

skewness(mba$gmat)
skewness(mba$workex)


kurtosis(mba$workex)
kurtosis(mba$gmat)


summary(mba)


mean(mba$workex)
median(mba$workex)
var(mba$workex)
sd(mba$workex)
summary(mba)

skewness(mba$workex)
skewness(mba$gmat)
kurtosis(mba$workex)
