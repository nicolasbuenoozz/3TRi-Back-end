from flask import flask
app= flask (__name__)

@app.route('/')
def hello_world
     return 'hello, World!'
     if__name__=='__main__':
        app.run(debug=True)