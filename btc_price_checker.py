import requests

# URL της API για την τιμή του Bitcoin
url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'

# Κάνουμε το αίτημα GET
response = requests.get(url)

if response.status_code == 200:
    # Μετατρέπουμε την απόκριση σε JSON
    data = response.json()
    # Λαμβάνουμε την τιμή του Bitcoin σε USD
    btc_price = data['bpi']['USD']['rate']
    print(f"Η τρέχουσα τιμή του Bitcoin είναι: ${btc_price}")
else:
    print("Κάτι πήγε στραβά. Δεν μπορώ να πάρω την τιμή του Bitcoin.")
