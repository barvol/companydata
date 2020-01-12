import requests
import json
import pickle
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
#data_file = 'data_file.json'
id_data = ''
inn = input ('Введите ИНН: ')
base_url = 'https://www.rusprofile.ru/ajax.php?&query=' + inn + '&action=search'
real_url = 'https://www.rusprofile.ru'

def rus_profile(base_url, real_url, headers, id_data):
    session = requests.Session()
    request = session.get(base_url, headers = headers)
    data = json.loads(request.text)
    id_data = data['ul'][0]['link']
    real_url = real_url + id_data
    request_n = session.get(real_url, headers = headers)
    soup = bs(request_n.content, 'html.parser')
    comp_name = data['ul'][0]['name']
    address = data['ul'][0]['address']
    ceo_name = data['ul'][0]['ceo_name']
    ceo_type = data['ul'][0]['ceo_type']
    okved = data['ul'][0]['okved_descr']
    #seo = soup.find('span', {"class": "company-info__text"}).text
    print(comp_name)
    print(address)
    print(ceo_type)
    print(ceo_name)
    print('ОКВЭД: ', okved)

rus_profile(base_url, real_url, headers, id_data)


