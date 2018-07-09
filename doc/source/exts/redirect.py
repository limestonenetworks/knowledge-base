import os
from shutil import copyfile

REDIRECT_TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), '_templates')

def update_templates_path(app):
    app.builder.config.templates_path.append(os.path.relpath(REDIRECT_TEMPLATE_PATH, app.confdir))
    app.builder.init_templates()

def copy_redirect_files(app):
    page_redirects = []
    redirects = app.config.redirects

    for redir in redirects:
        context = {
            'title': 'Test Title',
            'body': 'Test Body',
            'redirect_target': redir[1],
        }
        page_redirects.append((redir[0], context, 'redirect.html'))
    return page_redirects

def setup(app):
    app.add_config_value('redirects', None, True)
    app.connect('builder-inited', update_templates_path)
    app.connect('html-collect-pages', copy_redirect_files)
