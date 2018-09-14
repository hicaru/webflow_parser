import os
import shutil
from .web_flow import WebFlowAuth
from .template_parse import Parser


CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def file_write(webflow, key):
    parser = Parser(CURRENT_DIRECTORY)

    if not os.path.exists(CURRENT_DIRECTORY + '/assets'):
        os.makedirs(CURRENT_DIRECTORY + '/assets')
    if not os.path.exists(CURRENT_DIRECTORY + '/assets/js'):
        os.makedirs(CURRENT_DIRECTORY + '/assets/js')
    if not os.path.exists(CURRENT_DIRECTORY + '/assets/css'):
        os.makedirs(CURRENT_DIRECTORY + '/assets/css')

    parser.webflow_css(webflow.get_webflow_css_file)

    data = webflow.project_content(key)

    parser.my_css(data['css'], data['cssFileName'])
    parser.normalize_css(data['cssNormalize'])
    parser.my_js(data['siteJs'], data['siteJsFileName'])

    for page in data['pages']:
        parser.html(page)


def command_line():
    username = input('username: ')
    password = input('password: ')

    webflow = WebFlowAuth(username, password)
    webflow.auth()

    print('set 1: get all project keys')
    print('set 2: get my template')
    print('set 3: dir clear')
    print('set 4: exit')

    key = input('set your key: ')
    try:
        key = int(key)
    except ValueError:
        print('key is number')
        return None

    if key == 1:
        data = []

        for index, project_key in enumerate(webflow.get_all()):
            print('set project id: ', index, project_key)
            data.append(project_key)

        project_id = input('set id: ')
        try:
            project_id = int(project_id)
            file_write(webflow, data[project_id])
        except Exception as err:
            print('id error', err)
            return None

    if key == 2:
        project_key = input('project key: ')

        try:
            file_write(webflow, project_key)
        except Exception:
            print('key error')
            return None

    if key == 3:
        shutil.rmtree(CURRENT_DIRECTORY + '/assets')

    if key == 4:
        print('good buy')
        return None
