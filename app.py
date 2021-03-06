import os
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>FALA MANO, BLZ?</h1>"

@app.route("/nome", methods=['GET'])
def teste():
    input = request.args.get('nome', default = 'sasa', type = str)
    return '{}'.format(input.split(','))

def main():
    port = int(os.environ.get("PORT", 5000))
    print(port)   
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()