import requests, json
data = requests.get('https://cloud.iexapis.com/stable/stock/GME/quote?token=sk_c809dfddad204a39a965806caa34bcdf').json()
print(data['latestPrice'])