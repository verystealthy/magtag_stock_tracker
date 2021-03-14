# magtag_stock_tracker
Stock Tracker with Adafruit's MagTag Display

This code will cycle through stock symbols from a list, and will display the following on Adafruit's MagTag e-ink display:

* Stock symbol (e.g. AAPL, TSLA, GME, etc.)
* Percent change from last closing price (e.g. ```10%``` if the latest updated price is 10% more than the opening price)
- Note that this is *NOT* the percent change between latest price and opening price. It is percent change between latest price and the last closing. 
* Latest share price
* Market Open / Closed
* Neopixels are green / red if the Percent Change is positive / negative.  

The background changes if the stonk is up or down from the previous opening price. 

Just change the "symbols" list to reflect your portfolio. 

TODO:

- Add crypto
- Add diamond hands icons

This code needs to be heavily optimized. There's no need to use the ```requests``` library at all, yet here we are. 

This code uses the IEX Cloud API to grab a nice JSON with all the info we need. For a small number of API calls, the IEX Cloud free account is more than enough.
The free tier gives you 50k API calls a month, which is plenty for this project. Here's a referral code if you want to use IEX Cloud: https://iexcloud.io/s/629d1c60

## Usage
Create a ```secrets.py``` like so:

```
secrets = {
    'ssid' : 'home_wifi_network',
    'password' : 'wifi_password',
    'API_TOKEN' : "sk_123456789abcds", # Your IEX Cloud API token. 
    }
```
* Change the ```symbols``` list to reflect your portfolio. 
* Save the code as ```code.py``` into your ```CIRCUITPY``` device (don't forget the libraries, fonts, and BMPs)
* Forgo all paper hands thoughts. 
