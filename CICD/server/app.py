from flask import Flask

app = Flask(__name__)

@app.route("/healthz")
def healthz():
    return "200 OK\n"

if __name__ == '__main__':
    app.run()