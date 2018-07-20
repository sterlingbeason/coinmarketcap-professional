# filename:     simple_crypto_cli.py
# description:  A simple crypto asset command-line interface built on
#               coinmarketcap-professional Python wrapper (v0.0.1)
# date:         2018-07-20
# author:       sterlingbeason
# note:         API key needed to substitute below

import re, time
from coinmarketcap_pro.client import Client
client = Client("API-KEY-HERE") # replace with your API key

# get crytos mapping data
print "Initializing crypto asset data... ",
try:
    cryptos = response = client.request_api_endpoint("cryptocurrency/map")
    if response["status"]["error_code"] is not 0:
        print("[FAIL]")
        print(response["status"]["error_message"])
        quit()
    else:
        print("[DONE]")
except Exception as e:
    print("Error: " + e)
    quit()

def search_crytos_by_name(name):
    match_count = 0
    perfect_match_found = False
    match_list = [] # hold an aggregate of matched crpyto names
    for crypto in cryptos["data"]:
        crypto_name = crypto["name"]
        if re.search(name, crypto_name, re.IGNORECASE):
            match_count += 1
            # check for perfect match
            if len(name) == len(crypto_name):
                # perfect match found | return perfect match id
                perfect_match_found = True
                return crypto["id"]

            # partial match | append aggregate list
            match_list.append(crypto_name)

    # no perfect match | display search Results
    print("---------------Search Results----------------")

    if len(match_list) > 3:
        for a,b,c in zip(match_list[::3],match_list[1::3],match_list[2::3]):
            print '{:<27}{:<27}{:<}'.format(a,b,c)
    else:
        for crypto in match_list:
            print(crypto)

    # print something if no results
    if match_count == 0:
        print("NO RESULTS FOUND! try something else.")
    else:
        print("...now enter complete name!")

    return False

print("-------------------Instructions-------------------")
print("|    * search for crypto by partial/full name    |")
print("|    * enter 'exit' to terminate program         |")
print("--------------------------------------------------")

while True:
    search_term = raw_input("\nSearch by Crypto Name: ")
    # check if user wants to exit program
    if search_term == "exit":
        quit()
    result = search_crytos_by_name(search_term)
    if result is False:
        continue # no perfect match | try again

    # get latest quote data for matched crypto
    print("getting lastest quote...")

    c_data = client.request_api_endpoint("cryptocurrency/quotes/latest", {'id': result, "convert" : "USD,BTC,ETH"})
    c_data = c_data["data"][str(result)]

    # print latest quote data
    print("-----------" + c_data["name"] + " (" + c_data["symbol"] + ")-----------")
    print(time.ctime())
    print "{:<20}{:20}".format("Rank: ", str(c_data["cmc_rank"]))
    print "{:<20}{:20}".format("Markets: ", str(c_data["num_markets"]))
    print "{:<20}{:20}".format("Supply: ", str(c_data["circulating_supply"]) + "/" + str(c_data["total_supply"]))
    print "{:<20}{:20}".format("Price ($): ", str(c_data["quote"]["USD"]["price"]))
    print "{:<20}{:20}".format("Price (BTC): ", str(round(c_data["quote"]["BTC"]["price"], 7)))
    print "{:<20}{:20}".format("Price (ETH): ", str(round(c_data["quote"]["ETH"]["price"], 7)))
    print("-----------" + c_data["name"] + " (" + c_data["symbol"] + ")-----------")
