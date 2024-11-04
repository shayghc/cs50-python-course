import json
import requests
import sys

# Check command-line input count
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Enter one amount only")

# Check for int value
try:
    amount_requested = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    pass
else:
    # Query bitcoin rate
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    bitcoin_rate = o["bpi"]["USD"]["rate_float"]
    print(f"${bitcoin_rate * amount_requested:,.4f}")