df<-data.frame(x=1:3,y=c("a","b","c"))
              
print(df[1,1]) 

print(df[1,1:2])

print(df[c(1,3),2])

print(df[c(1,3),1])

print(df[c(1,3),c(1,2)])

