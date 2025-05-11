from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def home():
    return render_template('index.html')



clients = []

@sock.route('/ws')
def ws(sock):
    clients.append(sock)
    try:
        while True:
            data = sock.receive()
            print("Received from ESP32:", data)
            for c in clients:
                if c != sock:
                    c.send(data)
    except:
        clients.remove(sock)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
