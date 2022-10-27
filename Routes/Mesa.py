from flask import jsonify,request,Blueprint
from Controladores.ControladorMesa import ControladorMesa

miControladorMesa = ControladorMesa()
mesas=Blueprint('mesas',__name__)

@mesas.route("/Mesas", methods=['GET'])
def getMesa():
    json = miControladorMesa.index()
    return jsonify(json)


@mesas.route("/Mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()#
    json = miControladorMesa.create(data)
    return jsonify(json)


@mesas.route("/Mesas/<string:id>", methods=['GET'])
def getMesas(id):
    json = miControladorMesa.show(id)
    return jsonify(json)


@mesas.route("/Mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)


@mesas.route("/Mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)
