#Download the data set
equakes <- datasets::quakes

####Top 10 rows and last 10 rows
head(equakes,10)
tail(equakes,10)
######Columns
equakes[,c(1,2)]

df<-equakes[,-5]

summary(equakes[,1])

equakes$depth

summary(equakes$depth)

###########Summary of the data#########

summary(equakes)
summary(equakes$Wind) 

#####################
plot(equakes$depth)
plot(equakes$depth,equakes$mag,type="p")
plot(equakes)
# points and lines 
plot(equakes$depth, type= "l") # p: points, l: lines,b: both
plot(equakes$depth, xlab = 'depth Concentration', 
     ylab = 'No of Instances', main = 'depth levels in NY city',
     col = 'blue')
# Horizontal bar plot
barplot(equakes$mag, main = 'depth Concenteration in air',
        ylab = 'depth levels', col= 'blue',horiz = F,axes=T)
#Histogram
hist(equakes$depth)
hist(equakes$mag, 
     main = 'Solar Radiation values in air',
     xlab = 'Solar rad.', col='blue')

#Single box plot
boxplot(equakes$mag,main="Boxplot")
boxplot.stats(equakes$mag)$out



# Multiple box plots
boxplot(equakes[,1:4],main='Multiple')
#margin of the grid(mar), 
#no of rows and columns(mfrow), 
#whether a border is to be included(bty) 
#and position of the 
#labels(las: 1 for horizontal, las: 0 for vertical)
#bty - box around the plot
par(mfrow=c(3,3),mar=c(2,5,2,1),  las=0, bty="o")
plot(equakes$depth)
plot(equakes$depth, equakes$Wind)
plot(equakes$depth, type= "l")
plot(equakes$depth, type= "l")
plot(equakes$depth, type= "l")
barplot(equakes$depth, main = 'depth Concenteration in air',
        xlab = 'depth levels', col='green',horiz = TRUE)
hist(equakes$depth)
boxplot(equakes$depth)
boxplot(equakes[,0:4], main='Multiple Box plots')


##Home work
e_quakes<-datasets::quakes
sd(equakes$mag)#,na.rm = T)
sd(airquality$Ozone,na.rm = T)

var(equakes$mag)
skewness(equakes$mag)
kurtosis(equakes$mag)

mean(equakes$mag)



