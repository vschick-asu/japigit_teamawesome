#!/usr/bin/env python3

# Import some libs
import requests


def get_stock_data(my_symbol):
    # Set some typically overridable vars
    my_apikey = "ANSDAR3FGKMZSDT6"
    request_function = "GLOBAL_QUOTE"
    stock_url = "https://www.alphavantage.co/"

    # Set some vars to help build out an api url
    stock_funct = "query?function=" + request_function + "&"
    stock_sym = "symbol=" + my_symbol + "&"
    stock_interval = "interval=5min&"
    stock_key = "apikey=" + my_apikey
    req_url = stock_url + stock_funct + stock_sym + stock_interval + stock_key

    # Actually start the request
    myrequest = requests.get(req_url)
    myresponse = myrequest.json()

    # Return as just a string of the actual price.
    # The directions also say to print as json.
    # To do this, only return `myresponse`
    return myresponse["Global Quote"]["05. price"]


# Main function
def main():
    user_input = input("Enter stock symbol or quit: ")

    # Keep running until quit is entered.
    while user_input != "quit":
        print("The current price of " + user_input + " is: " + get_stock_data(user_input))
        user_input = input("Enter stock symbol or quit: ")

    print("Stock Quotes retrieved successfully!")


if __name__ == "__main__":
    main()
