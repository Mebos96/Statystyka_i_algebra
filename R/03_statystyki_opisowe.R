#Exercise 1

df <- data.frame('wartosc'= c(1,2,3,4,5,6), 'prawdopodobienstwo'=c(1/6, 1/6, 1/6, 1/6, 1/6, 1/6))
print(min(df$wartosc))
print(max(df$wartosc))
print(mean(df$wartosc))

#Exercise 2
library("Rlab")
rbern(100)
ber
