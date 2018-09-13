from web_flow import WebFlowAuth
from template_parse import Parser

if __name__ == '__main__':
    username = input('username: ')
    password = input('password: ')

    webflow = WebFlowAuth(username, password)
    webflow.auth()

    parser = Parser('/home/rinat/PycharmProjects/webflow_parser')

    parser.webflow_css(webflow.get_webflow_css_file)

    # print('set 1: get all template')
    # print('set 2: get my template')
    # print('set 3: exit')

    key = input('key: ')

    data = webflow.project_content(key)

    parser.my_css(data['css'], data['cssFileName'])
    parser.normalize_css(data['cssNormalize'])
    parser.my_js(data['siteJs'], data['siteJsFileName'])

    for page in data['pages']:
        parser.html(page)
