import ipaddress
import ssl
import wifi
import socketpool
import json
import adafruit_requests
import terminalio
import time
from adafruit_magtag.magtag import MagTag
    
# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise
    
print("Connecting to %s"%secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!"%secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

# Grab IEX Cloud API token from secrets file
IEX_API = secrets["API_TOKEN"]

# Creates Socket and requests object
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
magtag = MagTag()

# Ticker Text (e.g. AAPL, TSLA, etc. )
magtag.add_text(
    text_font="fonts/Arial-Bold-24.bdf",
    text_position=(
        100,
        20,
    ),
    text_scale=0,
)
# Latest price of the stock from the json. 
magtag.add_text(
    text_font="fonts/Lato-Bold-ltd-25.bdf",
    text_position=(
        60,
        75,
    ),
    text_scale=2,
)

# Percent change between the last closing price and the latest price retrieved by the json. 
# e.g if it last closed at $100, and it's $110 at the time of the latest update, this will show "%10" 
magtag.add_text(
    text_font="fonts/Lato-Bold-ltd-25.bdf",
    text_position=(
        210,
        20,
    ),
    text_scale=0,
)

# Grabs the json data from IEX Cloud
def fetch_data(symbol):
    response = requests.get(f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={IEX_API}').json()
    # If the current price is less than the opening price, stonks down.bmp 
    if response['open'] > response['latestPrice']:
        magtag.graphics.set_background("bmps/down.bmp")
    # Otherwise, stonks up.bmp (TODO - diamond_hands.bmp)
    else:
        magtag.graphics.set_background("bmps/up.bmp")
    magtag.set_text(response['symbol'], index=0, auto_refresh=False) # Get the ticker from the json 
    magtag.set_text("$" + str(response['latestPrice']), index=1, auto_refresh=False) # Get the latest price from the json
    magtag.set_text(str(round((response['changePercent'] * 100), 2)) + "%", index=2, auto_refresh=True) # Get the % change from the json & redraw the display with all info. 
    time.sleep(2) # Let the display update. 

symbols = ["AAPL", "VTI", "TSLA", "GME"] # Change this to reflect your portfolio (TODO - Press buttons for crypto - Different API endpoint)
while True: # Cycle through tickers every 60 seconds. 
    for ticker in symbols:
        fetch_data(ticker)
        time.sleep(60) # Change this if you want faster or slower updates. 