import os
from flask import Flask
from back import route
template_dir = os.path.abspath('./front/templates')
app = Flask(__name__, template_folder=template_dir)

app.add_url_rule('/', view_func=route.entry_point)
app.add_url_rule('/hello_world', view_func=route.hello_world)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
