# Подключение модулей
import requests
import time

# Token и id
token = 'vk1.a.Rx5A2rx_Dseg7HmFaGjBD-BeOeYhGp5PlUgW6AbmNIZ0lkAPK1BaOUbKh4aUfWz4FoX7Er5JtkqbxdmI2a8x-l5iTBkPiVm4KvrCVeAWcTeIbm97UMl3KbUFavZ3jdQ3xx_EMsr9wQo5VLlb4nO1vtCCxzsH1YRSRGrlIyekwcXBQoBloHX-aNaE1Sq8vFe2'
page_id = 'dm'
n = 1

# Основной код
def vk_download(method, parameters, token=token):
    url = 'https://api.vk.com/method/' + method + '?' + parameters + '&access_token=' + token + "&v=5.131"
    response = requests.get(url)
    return response.json()


title_page = vk_download('users.get', 'user_ids=' + page_id)
title_page = title_page['response']
new_id = str(title_page[0]['id'])
wall = vk_download('wall.get','owner_id=' + new_id)
wall = wall['response']


for i in range(0,n):
    param = '&count=1&offset=' + str(i)
    note = vk_download('wall.get', 'owner_id=' + new_id + param)
    note = note['response']
    note = note['items'][0]
    author_note, coments_count = 'Гость', str(note['comments']['count'])
    likes_count, reposts_count = str(note['likes']['count']), str(note['reposts']['count'])
    if int(note['from_id']) == int(note['owner_id']):
        author_note = 'Владелец'
    print(author_note, coments_count, likes_count, reposts_count)

