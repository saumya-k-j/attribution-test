import os
import sentry_sdk
from flask import Flask
from calc import divide

sentry_sdk.init(
    dsn="https://5381fc6a6c741623760eff9870b1c585@o4511516319219712.ingest.us.sentry.io/4511516322234368",
    traces_sample_rate=0.0,
)

app = Flask(__name__)

@app.route("/")
def home():
    return "ok - try /crash"

@app.route("/crash")
def crash():
    return str(divide(10, 0))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
