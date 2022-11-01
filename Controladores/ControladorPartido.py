from Repositorio.RepositorioPartido import RepositorioPartido
from Repositorio.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Partido import Partido
from Modelos.Candidatos import Candidatos


class ControladorPartido():
    def __init__(self):
        self.RepositorioPartido = RepositorioPartido()

    def index(self):
        return self.RepositorioPartido.findAll()

    def create(self, infoPartido):
        for x in infoPartido:
            if x == "nombre" or x == "lema":
                pass
            else:
                return {"msg":"Hay campos no permitidos"}
        try:
            if infoPartido["nombre"]==True and infoPartido["lema"]==True:
                pass
        except:
            return {"msg":"Faltan datos por llenar"}
        NuevoPartido = Partido(infoPartido)
        return self.RepositorioPartido.save(NuevoPartido)

    def show(self, id):
        partido = Partido(self.RepositorioPartido.findById(id))
        return partido.__dict__

    def update(self, id, infoPartido):
        PartidoActual = Partido(self.RepositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.RepositorioPartido.save(PartidoActual)

    def delete(self, id):
       
        return self.RepositorioPartido.delete(id)