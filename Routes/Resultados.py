from flask import jsonify,request,Blueprint
from Controladores.ControladorResultados import ControladorResultados

miControladorResultados = ControladorResultados()
Resultados=Blueprint('Resultados',__name__)

# @Resultados.route("/Resultados", methods=['GET'])
# def getResultados():
#     json = miControladorResultados.index()
#     return jsonify(json)

@Resultados.route("/Resultados", methods=['POST'])
def crearResultados():
    data = request.get_json()#
    json = miControladorResultados.create(data)
    return jsonify(json)

@Resultados.route("/Resultados/<string:id>", methods=['GET'])
def getResultados(id):
    json = miControladorResultados.show(id)
    return jsonify(json)


@Resultados.route("/Resultados/<string:id>", methods=['PUT'])
def modificarResultados(id):
    data = request.get_json()
    json = miControladorResultados.update(id, data)
    return jsonify(json)


@Resultados.route("/Resultados/<string:id>", methods=['DELETE'])
def eliminarResultados(id):
    json = miControladorResultados.delete(id)
    return jsonify(json)