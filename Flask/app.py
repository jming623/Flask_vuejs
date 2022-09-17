from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return 'Hello World'
 
@app.route('/create/')
def create():
    return 'create'

@app.route('/read/<bno>/')
def read(bno):
    return 'Read ' + bno    

app.run(debug=True)