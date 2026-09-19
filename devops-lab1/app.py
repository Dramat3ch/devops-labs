from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host="my-db", port=6379, decode_responses=True)

@app.route("/")
def hello_world():
    visits = r.incr("visits")
    return f"<p>Hello, DevOps! Visits: {visits}</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
