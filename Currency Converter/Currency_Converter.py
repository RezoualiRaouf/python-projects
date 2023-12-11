import requests

def fix_initial_err(initial):
    string_error_message = "Value Error: The amount must be a string"
    while True:
        try:
            initial = str(input("Enter a shortcut of your initial currency: "))
            
            if not initial.isalpha():
                raise ValueError(1)
            break
        except ValueError:
            print(string_error_message)
            
    return (initial)


def fix_target_err(target):
    string_error_message = "Value Error: The target currency must be a string"
    while True:
        try:
            target = str(input("Enter a shortcut of your target currency: "))
            
            if not target.isalpha():
                raise ValueError(1)
            break
        except ValueError:
            print(string_error_message)

    return target


def fix_float_err(amount):
    number_error_message = "Value Error: The shortcut must be a number"
    
    while True:
        try:
            amount = float(input("Enter the amount: "))
            
            if not isinstance(amount, (int, float)):
                raise ValueError(1)
            break
        except ValueError:
            print(number_error_message)
            
    return amount


initial = fix_initial_err('')
target = fix_target_err('')
amount = fix_float_err(0)

url = f"https://api.apilayer.com/fixer/convert?to={target}&from={initial}&amount={amount}"

payload = {}
headers= {
  "apikey": "J8POf4136ZYrMzeKVpHgbICq79qgOBIC"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if status_code != 200:
    raise SystemError("soryy a we are having somme problems over her try later!")

result = response.json()
print(f"{amount} {initial} is equal to {result['result']} {target}")
