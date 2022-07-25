# Подключение модулей
import requests
import time
# Token и id
token = 'vk1.a.Rx5A2rx_Dseg7HmFaGjBD-BeOeYhGp5PlUgW6AbmNIZ0lkAPK1BaOUbKh4aUfWz4FoX7Er5JtkqbxdmI2a8x-l5iTBkPiVm4KvrCVeAWcTeIbm97UMl3KbUFavZ3jdQ3xx_EMsr9wQo5VLlb4nO1vtCCxzsH1YRSRGrlIyekwcXBQoBloHX-aNaE1Sq8vFe2'
page_id = '96772899'
# Основной код
url = 'https://api.vk.com/method/users.get?user_ids=' + page_id + '&access_token=' + token + "&v=5.131"
response = requests.get(url)
user_name = response.json()
print(user_name)

