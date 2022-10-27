from Modelos.Resultados import Resultados
from Modelos.Candidatos import Candidatos
from Modelos.Mesa import Mesa
from Repositorio.RepositorioResultados import RepositorioResultados
from Repositorio.RepositorioCandidatos import RepositorioCandidatos
from Repositorio.RepositorioMesa import RepositorioMesa


class ControladorResultados():
    def __init__(self):
        self.RepositorioResultados = RepositorioResultados()
        self.RepositorioMesa = RepositorioMesa()
        self.RepositorioCandidatos =RepositorioCandidatos()

    def index(self):
        return self.RepositorioResultados.findAll()

    def create(self, infoResultado, id_mesa, id_candidato):
        nuevaResultado=Resultados(infoResultado)
        mesa=Mesa(self.RepositorioMesa.findById(id_mesa))
        candidato=Candidatos(self.RepositorioCandidatos.findById(id_candidato))
        nuevaResultado.mesa=mesa
        nuevaResultado.candidato=candidato
        return self.RepositorioResultados.save(nuevaResultado)

    def show(self, id):
        resultados = Resultados(self.RepositorioResultados.findById(id))
        return resultados.__dict__

    def update(self, id, infoResultado, id_mesa, id_candidato):
        resultado=Resultados(self.RepositorioResultados.findById(id))
        mesa = Mesa(self.RepositorioMesa.findById(id_mesa))
        candidato = Candidatos(self.RepositorioCandidatos.findById(id_candidato))
        resultado.estudiante = mesa
        resultado.materia = candidato
        return self.RepositorioResultados.save(resultado)

    def delete(self, id):
        return self.RepositorioResultados.delete(id)