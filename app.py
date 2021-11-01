import os
from flask import Flask
from flask import request
from flask_cors import CORS
from playsound import playsound
import gtts

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>FALA MANO </h1>"

@app.route("/nome", methods=['GET'])
def teste():
    input = request.args.get('nome', default = 'sasa', type = str)
    return '{}'.format(input.split(','))

@app.route('/voz', methods=['GET'])
def voz():
    input = request.args.get('nome', default=' ', type=str)
    teste = 'Olá, {}'.format(input)
    frase = gtts.gTTS(teste, lang='pt-br')
    frase.save('frase.mp3')
    playsound('frase.mp3')
    return "<h1>Olá, {} </h1>".format(input)

def main():
    port = int(os.environ.get("PORT", 5000))
    print(port)   
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()