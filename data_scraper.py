def fetch_XRP_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
    response =requests.get(url)
    data = response.json()
    xrp_price = data["XRP"]["usd"]
    print(f"The current price of XRP is: {xrp_price}")
    return xrp_price

fetch_XRP_data()