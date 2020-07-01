from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'

if __name__ == "__main__":
    app.run(debug=True, host='192.168.254.253', port=5000)
