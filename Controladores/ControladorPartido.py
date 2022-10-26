import json
from Repositorio.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido


class ControladorPartido():
    def __init__(self):
        self.RepositorioPartido = RepositorioPartido()

    def index(self):
        return self.RepositorioPartido.findAll()

    def create(self, infoPartido):
        NuevoPartido = Partido(infoPartido)
        return self.RepositorioPartido.save(NuevoPartido)

    def show(self, id):
        partido = Partido(self.RepositorioPartido.findById(id))
        return partido.__dict__

    def update(self, id, infoPartido):
        PartidoActual = Partido(self.RepositorioPartido.findById(id))
        PartidoActual.id = infoPartido["id"]
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.RepositorioPartido.save(PartidoActual)

    def delete(self, id):
        return self.RepositorioPartido.delete(id)