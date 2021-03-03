from flask import render_template

def entry_point():
    return render_template('./app.html')

def hello_world():
    return 'Hello Boug'
