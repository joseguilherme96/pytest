import requests

def get_chainlink_price():

    response = requests.get('https://fakeapi.com')
    return response.json()

if __name__ == "__main__":
    print(get_chainlink_price())