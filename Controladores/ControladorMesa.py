from Repositorio.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
from flask import Response


class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        try:
            if infoMesa["numero"]==True and infoMesa["cantidad_inscritos"]==True:
                pass
        except:
            return {"msg":"Faltan datos por llenar"}
        info={"numero":0,"cantidad_inscritos":"0"}
        nuevaMesa = Mesa(info)
        nuevaMesa.numero = infoMesa["numero"]
        nuevaMesa.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        mesa = Mesa(self.repositorioMesa.findById(id))
        return mesa.__dict__

    def update(self, id, infoMesa):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)

