

class Parser(object):

    root_dir = None

    def __init__(self, dir):
        self.root_dir = dir

    def webflow_css(self, content):
        dir = '%s/assets/css/webflow.css' % self.root_dir

        with open(dir, 'w') as css_file:
            css_file.write(content)

    def normalize_css(self, content):
        dir = '%s/assets/css/normalize.css' % self.root_dir

        with open(dir, 'w') as css_file:
            css_file.write(content)

    def my_css(self, content, name):
        dir = '%s/assets/css/%s' % (self.root_dir, name)

        with open(dir, 'w') as css_file:
            css_file.write(content)

    def my_css(self, content, name):
        dir = '%s/assets/css/%s' % (self.root_dir, name)

        with open(dir, 'w') as css_file:
            css_file.write(content)

    def modernizr_js(self, content):
        dir = '%s/assets/js/modernizr.js' % self.root_dir

        with open(dir, 'w') as css_file:
            css_file.write(content)

    def my_js(self, content, name):
        dir = '%s/assets/js/%s' % (self.root_dir, name)

        with open(dir, 'w') as css_file:
            css_file.write(content)

    def html(self, page):
        dir = '%s/assets/%s.html' % (self.root_dir, page['page']['title'])

        with open(dir, 'w') as css_file:
            css_file.write(page['html'])
