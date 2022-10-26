from Repositorio.RepositorioResultados import RepositorioResultados
from Modelos.Resultados import Resultados


class ControladorResultados():
    def __init__(self):
        self.RepositorioResultados = RepositorioResultados()

    def index(self):
        return self.RepositorioResultados.findAll()

    def create(self, infoResultados):
        NuevoResultados = Resultados(infoResultados)
        return self.RepositorioResultados.save(NuevoResultados)

    def show(self, id):
        Resultados = Resultados(self.RepositorioResultados.findById(id))
        return Resultados.__dict__

    def update(self, id, infoResultados):
        ResultadosActual = Resultados(self.RepositorioResultados.findById(id))
        ResultadosActual.id = infoResultados["id"]
        ResultadosActual.numero_mesa = infoResultados["numero_mesa"]
        ResultadosActual.id_partido = infoResultados["id_partido"]#revisar esta linea
        return self.RepositorioResultados.save(ResultadosActual)

    def delete(self, id):
        return self.RepositorioResultados.delete(id)