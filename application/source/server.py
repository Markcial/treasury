from flask import Flask
app = Flask(__name__)
from tasks import add


@app.route('/')
def hello_world():
    print add.delay(3, 5)
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
