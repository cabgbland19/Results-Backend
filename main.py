from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json
from waitress import serve#expone la aplicacion, servidor web
from Routes.Mesa import *
app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(mesas)

@app.route("/test",methods=['GET']) #los @ son decorador, "/url"
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)#convierte los diccionarios en json respons, serializa la imformacion a api rest

def loadFileConfig():
    with open('config.json') as f:#with open sirve para abrir archivos que se encuentre en el programa
        data = json.load(f)#load sirve para cargar archivos, loads carga texto
        #print(type(data))
    return data
#print(loadFileConfig())

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"])) #casteo para concardenar el str
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
