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

    """def create(self, infoResultados):
        NuevoResultados = Resultados(infoResultados)
        return self.RepositorioResultados.save(NuevoResultados)"""

    def show(self, id):
        Resultados = Resultados(self.RepositorioResultados.findById(id))
        return Resultados.__dict__

    """def update(self, id, infoResultados):
        ResultadosActual = Resultados(self.RepositorioResultados.findById(id))
        ResultadosActual.id = infoResultados["id"]
        ResultadosActual.numero_mesa = infoResultados["numero_mesa"]
        ResultadosActual.id_partido = infoResultados["id_partido"]
        return self.RepositorioResultados.save(ResultadosActual)"""

    def update(self, id, infoResultado, id_mesa, id_candidato):
        resultado=Resultados(self.RepositorioResultados.findById(id))
        resultado.numero_mesa = infoResultado["numero_mesa"]
        resultado.notaFinal=infoResultado["nota_final"]
        mesa = Mesa(self.RepositorioMesa.findById(id_mesa))
        candidato = Candidatos(self.RepositorioCandidatos.findById(id_candidato))
        resultado.estudiante = mesa
        resultado.materia = candidato
        return self.RepositorioResultados.save(resultado)

    def delete(self, id):
        return self.RepositorioResultados.delete(id)