from SharekhanApi.sharekhanConnect import SharekhanConnect

api_key = "Your API KEY"
version_id = "Version_id"
login = SharekhanConnect(api_key)
print(login.login_url(version_id))

session=login.generate_session(request_token="Your Request Token",secret_key="Your Secret Key")
sessionwithoutvesionId=login.generate_session_without_versionId(request_token="Your Request Token",secret_key="Your Secret Key")

apiKey = api_key
requestToken = "Your Encrypted Request Token Value"
access_token=login.get_access_token(apiKey,requestToken,userId=12345,versionId=1006)
print(access_token)

access_token = " Your Access Token "
sharekhan = SharekhanConnect(api_key,access_token=access_token)
print(sharekhan.requestHeaders())


# Place order history

orderparams={
 "customerId": "XXXXX",
 "scripCode": 1052,
 "tradingSymbol": "USDINR",
 "exchange": "RN",
  "transactionType": "B",
  "quantity": 1,
  "disclosedQty": 0,
  "price": "82.0075",
  "triggerPrice": "0",
   "rmsCode": "ANY",
   "afterHour": "N",
   "orderType": "NORMAL",
   "channelUser": "XXXXX",
   "validity": "GFD",
   "requestType": "NEW",
   "productType": "INVESTMENT",
   "instrumentType": "FUTCUR",
   "strikePrice": -1,
   "expiry": "31/03/2023",
   "optionType": "XX"
   }
order=sharekhan.placeOrder(orderparams)
print("PlaceOrder: {}".format(order))

# modify order

orderparams={
 "orderId":"259130707",
    "customerId": "XXXXX",
    "scripCode": 1052,
    "tradingSymbol": "USDINR",
    "exchange": "RN",
    "transactionType": "B",
    "quantity": 2,
    "disclosedQty": 0,
    "price": "81.1050",
    "triggerPrice": "0",
    "rmsCode": "SKNSECURR2",
    "afterHour": "N",
    "orderType": "NORMAL",
    "channelUser": "XXXXX",
    "validity": "GFD",
    "requestType": "MODIFY",
    "productType": "INVESTMENT",
    "instrumentType": "FUTCUR",
    "strikePrice": -1,
    "expiry": "31/03/2023",
    "optionType": "XX"
    }
order=sharekhan.modifyOrder(orderparams)
print("ModifyOrder: {}".format(order))

#cancel  order

orderparams={
  "orderId":"259130707",
    "customerId": "XXXXX",
    "scripCode": 1052,
    "tradingSymbol": "USDINR",
    "exchange": "RN",
    "transactionType": "B",
    "quantity": 2,
    "disclosedQty": 0,
    "price": "81.1050",
    "triggerPrice": "0",
    "rmsCode": "SKNSECURR2",
    "afterHour": "N",
    "orderType": "NORMAL",
    "channelUser": "XXXXX",
    "validity": "GFD",
    "requestType": "CANCEL",
    "productType": "INVESTMENT",
    "instrumentType": "FUTCUR",
    "strikePrice": -1,
    "expiry": "31/03/2023",
    "optionType": "XX"
    }
order=sharekhan.cancelOrder(orderparams)
print("CancelOrder: {}".format(order))

# Fund details

exchange="MX"
customerId=1487617
order=sharekhan.funds(exchange, customerId)
print("Fund Details : {}".format(order))

# Retrieves all orders for the day

customerId=1487617
order=sharekhan.reports(customerId)
print("Order Reports: {}".format(order))

#Retrieve history of an given order

exchange="RN"
customerId=1487617
orderId=259130707
order=sharekhan.exchange(exchange, customerId, orderId)
print("Order Details: {}".format(order))


# Retrieves all positions
customerId=1487617
order=sharekhan.trades(customerId)
print("Postion Reports: {}".format(order))


# Retrieves the trade  generated by an order

exchange="NC"
customerId=1487617
orderId=585194484
order=sharekhan.exchangetrades(exchange, customerId, orderId)
print("Trade Generated By an Order : {}".format(order))

# services Holdings

customerId=1487617
order=sharekhan.holdings(customerId)
print("Holdings : {}".format(order))

#Script Master

exchange="MX"
order=sharekhan.master(exchange)
print("Script Master : {}".format(order))

# Historical Data

exchange="BC"
scripcode=500410
interval="daily"
order=sharekhan.historicaldata(exchange, scripcode, interval)
print("Holdings Data: {}".format(order))

