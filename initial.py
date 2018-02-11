import bottle
from bottle import route, run, template, BaseTemplate, static_file

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url  # reference to function

@route('/')
def crack():
    return template('index.tpl')

@route('/static/<filename:path>', name='static')
def serve_static(filename):
    return static_file(filename, root='static')
run(host='localhost', port=8080)
