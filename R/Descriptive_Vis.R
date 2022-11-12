# airquality <- read.csv(r"\Users\Slmss\Desktop\Wholesale customers data.csv",header=TRUE, sep=",")


airquality  <- datasets::airquality 

####Top 10 rows and last 10 rows
head(airquality,10)
tail(airquality,10)

######Columns

airquality[50:60,c(1,2)]


df<-airquality[,-6]

#Descriptive statistics
#1
summary(airquality[,c(4,5)]) #generate for column 2,3

airquality$Ozone
airquality$Temp
airquality$Wind
airquality$Ozone

airquality$Solar.R

#1
summary(airquality$Wind)
summary(airquality$Month)

#Ozone
summary(airquality$Ozone)
###########Summary of the data#########

summary(airquality)
summary(airquality$Wind) 

#####################
#visualization
#scatter Plot
plot(airquality$Wind,type="l")

plot(airquality$Temp,airquality$Ozone,type="p")

plot(airquality) #SCatter Matrix

# points and lines 
plot(airquality$Wind, type= "l") # p: point l: lines,b: both

plot(airquality$Wind, type= "b")
plot(airquality$Wind, xlab = 'Ozone Concentration', 
     ylab = 'No of Instances', main = 'Ozone levels in NY city',
     col = 'blue',type='l')

# Horizontal bar plot
barplot(airquality$Ozone, main = 'Ozone Concenteration in air',
        ylab = 'ozone levels', col= 'blue',horiz = T,axes=T)

#Histogram
hist(airquality$Temp)
hist(airquality$Temp, 
     main = 'Solar Radiation values in air',
     xlab = 'Solar rad.', col='blue')


#Single box plot
boxplot(airquality$Wind,main="Boxplot")
boxplot.stats(airquality$Wind)$out

boxplot.stats(airquality$Ozone)$out

# Multiple box plots

boxplot(airquality[,1:4],main='Multiple')

-----------------------
#margin of the grid(mar), 
#no of rows and columns(mfrow), 
#whether a border is to be included(bty) 
#and position of the 
#labels(las: 1 for horizontal, las: 0 for vertical)
#bty - box around the plot

par(mfrow=c(3,3),mar=c(2,5,2,1),  las=0, bty="o")

plot(airquality$Ozone) 
plot(airquality$Ozone, airquality$Wind)
plot(airquality$Ozone, type= "l")
plot(airquality$Ozone, type= "l")
plot(airquality$Ozone, type= "l")
barplot(airquality$Ozone, main = 'Ozone Concenteration in air',
        xlab = 'ozone levels', col='green',horiz = TRUE)
hist(airquality$Solar.R)
boxplot(airquality$Solar.R)
boxplot(airquality[,0:4], main='Multiple Box plots')

#summary(airquality)

##
e_quakes<-datasets::quakes
sd(airquality$Ozone,na.rm = T)

#var
#skewness
#kurtosis
#Density plot









