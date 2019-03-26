# Created by Oleksandr Sorochynskyi
# On 24.03.2019

prices = read.csv("stock_history.csv")
prices$date <- as.POSIXct(prices$date)

