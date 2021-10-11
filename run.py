from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def test():
    return 'test123'

if __name__ == '__main__':
    app.run()