import re
import requests
from requests import RequestException
from json import JSONDecodeError


class WebFlowAuth(object):

    auth_url = 'https://webflow.com/dashboard/login'
    s3_url = 'https://s3.amazonaws.com/webflow-tmp-site-export-production'
    css_webflow = 'https://d3e54v103j8qbb.cloudfront.net/gen/css/site.81b28da069.css'
    session = None

    def __init__(self, username, password):
        self.data = {
            'username': username,
            'password': password,
            'googleToken': None
        }

    def auth(self):
        with requests.session() as session:
            headers = {
                'X-XSRF-Token': 'qIFQVnCo-_rBel0auoZpHW9zaIHqBbF8nD3I',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/65.0.3325.146 Safari/537.36'
            }

            r = session.post(url=self.auth_url, data=self.data, headers=headers)

            try:
                r = r.json()
                print('auth is fail')
            except JSONDecodeError:
                r = r.text
                print('auth is ', r)
                self.session = session

    def get_projects(self):
        if self.session is None:
            print('none auth')
            raise RequestException
        url = 'https://webflow.com/api/sites'

        r = self.session.get(url).json()['sites']
        return [{'name': i['name'], 'shortName': i['shortName']} for i in r]

    def get_all(self):
        r = requests.get(self.s3_url).text
        r = re.findall(r'<Key>(.+?)</Key>', r)
        temp = [i.replace('www.', '') for i in r]
        return temp

    @property
    def get_webflow_css_file(self):
        return requests.get(self.css_webflow).content

    @property
    def project_content(self, key):
        url = '%s/%s' %(self.s3_url, key)
        return requests.get(url).json()
