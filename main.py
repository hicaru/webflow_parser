from web_flow import WebFlowAuth
from template_parse import Parser

if __name__ == '__main__':
    username = input('username: ')
    password = input('password: ')

    webflow = WebFlowAuth(username, password)
    webflow.auth()

    print('set 1: get all template')
    print('set 2: get my template')
    print('set 3: exit')

    option = input('set: ')

    if True:
        for i, j in enumerate(webflow.get_all()):
            print('set: ', i, j)

        option = input('set: ')

    if option == 1:
        print(webflow.get_projects())
    if option == 3:
        print('exit')
