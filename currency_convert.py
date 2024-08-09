"""this code is for currency converter using api"""

import requests

# replace it with you unique API key
API_KEY = "enter your unique API key"
# input the currency you are converting from and to
current_currency = input("enter your currency: ")
change_currency = input("enter the currency in which you want to change it: ")
# enter the amount you want to convert
amount = int(input("enter the amount you want to convert: "))
# url to get the currency exchange
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{current_currency}"
# send request to API for getting data
response = requests.get(url)
# checking if the response is fetched properly
if response.status_code != 200:
    print(f"error fetching excghange: {response.status_code}")
data = response.json()
# checking and handling if the given currency is not in API
if current_currency not in data:
    print(f"the currency: {change_currency} is not available in the API.")
# calculating the converted_amount
try:
    conversion_rate = data["conversion_rates"][change_currency]
    converted_amount = amount * conversion_rate
    # print the result
    print(
        f"the amount: {amount} in this currency: {change_currency} is: {converted_amount}"
    )
except Exception as e:
    print(str(e))