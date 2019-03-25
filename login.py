import requests, lxml.html
import urllib3

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
}

# Change to url to login to
url = 'URL'

s = requests.session()
# update the header in the session object
s.headers.update(headers)
login = s.get(url)
login_html = lxml.html.fromstring(login.text)
# find the csrf token
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
# set params in data 
form['username'] = 'USER'
form['password'] = 'PASS'
response = s.post(url, data=form)

if response.status_code == 200:
    print('Login Success')

