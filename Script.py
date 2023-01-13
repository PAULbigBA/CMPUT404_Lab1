
import requests

print(requests.__version__)

response = requests.get("http://google.com")

print(response.content)

get_script = requests.get("https://raw.githubusercontent.com/PAULbigBA/CMPUT404_Lab1/main/Script.py")

print(get_script.text)

