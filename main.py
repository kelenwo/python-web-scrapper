import requests
from bs4 import BeautifulSoup
from pprint import pprint


#Link declarations, Stage1 is login
stage1 = 'https://cvr.inecnigeria.org/home/login'
stage2 = 'https://cvr.inecnigeria.org/VotersRegister'


s = requests.Session()

#Add headers to make it think you are crawling from a web browser, inecvr rejects requests not coming from a browser
headers = {
    'Referer': 'https://cvr.inecnigeria.org/register',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

#Login data, this is a valid login details created for this purpose
data = {
    '_method': 'POST',
    'data[Login][email]': 'kelvin@axumtechnologies.com',
    'data[Login][password]': 'password123',
}

response = s.get(stage1)

#Cache cookies
cookieJar = s.cookies

response = s.post(stage1, headers=headers, data=data)

#recache cookies to able to access the next page. Without cookies the session is not registered.
cookieJar = s.cookies

#Initiate second request which fetches the main page where you can fill forms to display register
res2= requests.get(stage2, headers=headers,cookies=cookieJar)

html = BeautifulSoup(res2.text, 'html.parser')

#Display the page source as text
pprint(html)

# captcha = html.find_all('.g-recaptcha')

