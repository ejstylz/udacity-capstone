from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('request successful')
    return "Theo's capstone"

if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
