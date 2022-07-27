import logging
from flask import Flask
from flask.logging import create_logger

app = Flask(__name__)

LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def hello():
    LOG.info("request successful")
    return "Theo's capstone"

if __name__ == "__main__":
    app.run()
