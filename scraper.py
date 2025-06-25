import requests
import sys

url = "https://pixelford.com/blog/"
try:
    response = requests.get(url)

except requests.exceptions.ConnectionError as e:
    print("Connection error. Please check your internet connection,", e)
    sys.exit()
except requests.exceptions.Timeout as e:
    print("Connection timed out. Please check your internet connection," e)
    sys.exit()
print(response.content)