import os
from tornado.template import Template, Loader

template_path = os.path.join(os.path.dirname(__file__), 'templates')
loader = Loader(template_path)
output_path = os.path.join(os.path.dirname(__file__), 'website')
templates = [fname for fname in os.listdir(template_path) if fname[-4:]=='html']

args = dict()
for template in templates:
    args[template] = dict()


def main():
    for template in templates:
        rendered = loader.load(template).generate(**args[template])
        with open(os.path.join(output_path, template), 'wb') as f:
            f.write(rendered)

if __name__ == '__main__':
    main()
