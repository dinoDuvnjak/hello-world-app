from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # Bind to 0.0.0.0 so the container is reachable on the network.
    app.run(host='0.0.0.0', port=8080)
