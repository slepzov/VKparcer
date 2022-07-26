# Подключение модулей
import requests
import time
import sqlite3

# Token и id
token = 'vk1.a.d5li-4DJYYpC0TFjkKetdzKNhicQ3cByC9YFKV6lIrxBPumG56GLd7-Da6lNQ-HAWscfwuRQ3GhzURB-7zmYAywjKWzWYapS2GZVDGK_J8dsU7v3tw57y7QUCBprgZImpY54YzqukUpu-0nK6WjKUZ6CnKrxUKDc5NS75JWLARDx8tX8yROK362PQk04CSwJ'
page_id = input("Введите id страницы: ")


# Основной код
def vk_download(method, parameters, token=token):
    url = 'https://api.vk.com/method/' + method + '?' + parameters + '&access_token=' + token + "&v=5.131"
    response = requests.get(url)
    try:
        return (response.json())['response']
    except:
        print('Пожалуйста, обновите токен, для этого воспользуйтесь ссылкой из файла main.py')
        exit()


title_page = vk_download('users.get', 'user_ids=' + page_id)
new_id = str(title_page[0]['id'])
wall = vk_download('wall.get', 'owner_id=' + new_id)
count_notes = wall['count']
name_page = title_page[0]['first_name'] + ' ' + title_page[0]['last_name']
n = int(input('На странице '+str(count_notes)+' записей. Сколько скачаем записей? '))
conn = sqlite3.connect(name_page+'.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS wall(
   number TEXT,
   author TEXT,
   comments TEXT,
   likes TEXT,
   reposts TEXT);
""")
for i in range(0, n):
    param = '&count=1&offset=' + str(i)
    note = vk_download('wall.get', 'owner_id=' + new_id + param)
    note = note['items'][0]
    author_note, coments_count = 'Гость', str(note['comments']['count'])
    likes_count, reposts_count = str(note['likes']['count']), str(note['reposts']['count'])
    if int(note['from_id']) == int(note['owner_id']):
        author_note = 'Владелец'
    information_recording = (i, author_note, coments_count, likes_count, reposts_count)
    cur.execute("INSERT INTO wall VALUES(?, ?, ?, ?, ?);", information_recording)
    conn.commit()
    time.sleep(0.5)
    print('Записей скачано:', i + 1)
print('Посты скачаны. Всего скачано: ' + str(n))
