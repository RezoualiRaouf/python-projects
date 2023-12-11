import requests

def get_currency_list_starting_with(letter, symbols):
    """Get a list of currencies starting with the specified letter."""
    return [symbol for symbol in symbols if symbol.startswith(letter)]

def fetch_symbols(api_key):
    """Fetch and return the currency symbols from the Fixer API."""
    url_symbols = "https://api.apilayer.com/fixer/symbols"
    response_symbols = requests.get(url_symbols, headers={"apikey": api_key})
    
    if response_symbols.status_code != 200:
        raise SystemError("Failed to fetch currency symbols. Please try again later!")
    
    return response_symbols.json().get('symbols', {})

def input_currency_letter(prompt):
    """Get the user input for the first letter of the currency."""
    return input(prompt).upper()

def print_matching_currencies(letter, symbols):
    """Print currencies starting with the specified letter."""
    matching_currencies = get_currency_list_starting_with(letter, symbols)
    
    if matching_currencies:
        print(f"Currencies starting with '{letter}':")
        for currency in matching_currencies:
            print(f"{currency}: {symbols[currency]}")
    else:
        print(f"No currencies found starting with '{letter}'")

def fix_input_err(prompt, error_message, condition, symbols):
    """Handle input errors with a custom prompt and error message."""
    while True:
        try:
            value = input(prompt)
            
            if not condition(value, symbols):
                raise ValueError(1)
            
            break
        except ValueError:
            print(error_message)

    return value

def is_valid_currency(value, symbols):
    """Check if the value is a valid currency symbol."""
    return value.isalpha() and value in symbols

def fix_initial_err(api_key, symbols):
    """Fix errors related to the initial currency input."""
    return fix_input_err(
        "Enter the shortcut of your initial currency: ",
        "Value Error: The shortcut is incorrect. Try again.",
        lambda value, symbols: is_valid_currency(value, symbols),
        symbols
    )

def fix_target_err(api_key, symbols):
    """Fix errors related to the target currency input."""
    return fix_input_err(
        "Enter the shortcut of your target currency: ",
        "Value Error: The shortcut is incorrect. Try again.",
        lambda value, symbols: is_valid_currency(value, symbols),
        symbols
    )

def fix_float_err():
    """Fix errors related to the amount input."""
    number_error_message = "Value Error: The amount must be a number."
    
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print(number_error_message)
    
    return amount

def convert_currency(api_key, initial, target, amount):
    """Convert currency using the Fixer API."""
    url_convert = f"https://api.apilayer.com/fixer/convert?to={target}&from={initial}&amount={amount}"
    response_convert = requests.get(url_convert, headers={"apikey": api_key})
    
    if response_convert.status_code != 200:
        raise SystemError("Sorry, we are having some problems. Please try again later!")

    return response_convert.json().get('result')

def main():
    api_key = "J8POf4136ZYrMzeKVpHgbICq79qgOBIC"
    symbols = fetch_symbols(api_key)
    
    symble_print = input("If you want the currency list to see the shortcut to your wanted currency, enter 1. Otherwise, press any other key to skip this step: ")

    if symble_print == "1":
        initial_letter = input_currency_letter("Enter the first letter of the currency you are searching for: ")
        print_matching_currencies(initial_letter, symbols)

    initial = fix_initial_err(api_key, symbols)
    target = fix_target_err(api_key, symbols)
    amount = float(fix_float_err())

    converted_result = convert_currency(api_key, initial, target, amount)
    print(f"{amount} {initial} is equal to {converted_result} {target}")

if __name__ == "__main__":
    main()
