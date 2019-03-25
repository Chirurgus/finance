# Created by Oleksandr Sorochynskyi
# On 24.03.2019

library(reticulate)
api <- import("data")
stocks <- sample(api.symbols(), 100)
prices <- api$stock_history(stocks)
prices$symbol <- factor(prices$symbol)
prices$date <- as.POSIXct(prices$date)

sapply(2014 + 0:5, function(year) {
  sum(is.na(subset(prices, as.POSIXlt(date)$year + 1900 >= year)$open))
});

plot(subset(prices, symbol=="WB")$open)

