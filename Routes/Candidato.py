from flask import jsonify,request,Blueprint
from Controladores.ControladorCandidatos import ControladorCandidatos

miControladorCandidatos = ControladorCandidatos()
candidatos=Blueprint('candidatos',__name__)

@candidatos.route("/candidatos", methods=['GET'])
def getCandidato():
    json = miControladorCandidatos.index()
    return jsonify(json)


@candidatos.route("/candidatos", methods=['POST'])
def crearCandidatoss():
    data = request.get_json()#
    json = miControladorCandidatos.create(data)
    return jsonify(json)


@candidatos.route("/candidatos/<string:id>", methods=['GET'])
def getCandidatos(id):
    json = miControladorCandidatos.show(id)
    return jsonify(json)


@candidatos.route("/candidatos/<string:cedula>", methods=['PUT'])
def modificarCandidatos(cedula):
    data = request.get_json()
    json = miControladorCandidatos.update(cedula, data)
    return jsonify(json)


@candidatos.route("/candidatos/<string:cedula>", methods=['DELETE'])
def eliminarCandidatos(cedula):   
    json = miControladorCandidatos.delete(cedula)
    return jsonify(json)

@candidatos.route("/candidatos/<string:id_candidato>/partidos/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id_candidato, id_partido):
    json=miControladorCandidatos.asignarPartido(id_candidato, id_partido)
    return jsonify(json)