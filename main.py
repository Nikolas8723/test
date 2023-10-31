import requests

from bs4 import BeautifulSoup as bs



URL = "https://site.ru"

paramsMain = {
    'mod':'main',
    'subaction': 'dologin',
    'username': 'admin',
    'password': 'admin',
    'selected_language': 'Russian'
}

session = requests.Session()



user = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.2296 YaBrowser/23.9.0.2296 Yowser/2.5 Safari/537.36'
}

session.headers = user

adminSite = session.post(URL + '/admin.php?mod=main', data=paramsMain)

adminSite = session.get(URL + '/admin.php?mod=addnews&action=addnews')

soup = bs(adminSite.text, 'html.parser')

user_hash = soup.find('input', {'name':'user_hash'}).get('value')


paramsImage = {
    'mod':'upload',
    'subaction': 'upload',
    'news_id': 0,
    'area': 'xfieldsimage',
    'author': 'admin',
    'xfname':'poster',
    'user_hash': user_hash,
    'qqfile':'1697799834245.jpg'
}
Adnews = {
'tr':''
}


image_file_path = '1697799834245.jpg'



with open(image_file_path, "rb") as image_file:
    files = {"image": (image_file_path, image_file)}

    print(files)
    response = session.post(URL + '/engine/ajax/controller.php', files=files, data=paramsImage)


print(response.text)
