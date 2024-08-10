# currency_converter
this is a simple currency converter tool that allows you to convert amounts between different currencies.
it uses real-time exchange rates from the ExchangeRate-API.

FEATURES
1. It fetches real-time exchange rate with the help of API.
2. It converts an amount from ome currency to another conveniently.
3. It includes basic error handling and logging.

REQUIREMENTS
1. Python 3.x
2. requests and logging library(you can download it using the command [pip install requests and pip install logging])

SETUP
1. Get an API key.
To use this,you need a api key which you can get by sign up at exchangerate-api.
2. Install required packages.
3. Run the script.

CODE OVERVIEW
1. API_KEY: The API key has to be fetched and can be stored in enviroment variable.
2. User Input: The user is asked to input the currencies and amount to change.
3. Error  Handling: It includes basic error handling for invalid input and API errors.
4. Logging: This code uses python's logging module to provide informative messages.