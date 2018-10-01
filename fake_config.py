import requests


user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
login_url = 'https://www.hockeyarena.net/en/index.php?p=security_log.php'
values = {'nick': 'YourNick',
          'password': 'YourPW'}


s = requests.Session()
s.post(login_url, data=values, headers=user_agent)

def get_html(url):
    r = s.get(url, cookies=s.cookies)
    return r.text

