# Welcome to coinmarketcap-professional v0.0.1
This is an unofficial Python wrapper for the CoinMarketCap Professional API v1. I am in no way affiliated with CoinMarketCap, use at your own risk.

**CoinMarketCap Professional API has been released to the public. API documentation and keys can be obtained from [https://pro.coinmarketcap.com/](https://pro.coinmarketcap.com/).**

## Features
* Authenticated requests to all valid Cryptocurrency, Exchange, Global Metrics, and Tools endpoints (v1).
* Simple handling of unexpected HTTP error codes

... more planned.

## Quick Start
```Python
from coinmarketcap_pro.client import Client
client = Client("API-KEY-HERE") # replace with your API key

# request specific endpoint w/ optional params
response = client.request_api_endpoint("cryptocurrency/map", {'limit': 10}) # returns dictionary from parsed JSON response

if response["status"]["error_code"] is not 0:
    # error exists
    print(response["status"])
else:
    # successful response
    print(response)
```
