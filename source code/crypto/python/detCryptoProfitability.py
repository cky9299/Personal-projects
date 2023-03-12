CurrentPrice=float(input("Enter current crypto price:"))

FuturePrice=float(input("Enter future crypto price:"))

Times=FuturePrice/CurrentPrice

MoneySpent=float(input("Enter usd spent:"))

Units=MoneySpent/CurrentPrice

Cost=CurrentPrice*Units

FutureTotalPrice=FuturePrice*Units

Profit=FutureTotalPrice-Cost

Fee=MoneySpent*.4/100

NetProfit=Profit-Fee

print('crypto price now:',CurrentPrice,'\n','you buy',Units,'units.','the cost is',Cost,'\n','Price changed to',FuturePrice,'\n','ur crypto value is',FutureTotalPrice,'\n','price changed by',Times,'times\n','fee:',Fee,'\n','ur profit is',Profit,'\nnet profit:',NetProfit)
