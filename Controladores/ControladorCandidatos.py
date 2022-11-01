from Repositorio.RepositorioCandidatos import RepositorioCandidatos
from Repositorio.RepositorioPartido import RepositorioPartido
from Modelos.Candidatos import Candidatos
from Modelos.Partido import Partido


class ControladorCandidatos():
    def __init__(self):
        self.RepositorioCandidatos = RepositorioCandidatos()
        self.RepositorioPartido = RepositorioPartido()

    def index(self):
        return self.RepositorioCandidatos.findAll()

    def create(self, InfoCandi):
        for x in InfoCandi:
            if x == "cedula" or x == "numero_resolucion" or x == "nombre" or x == "apellido":
                pass
            else:
                return {"msg":"Hay campos no permitidos"}
        try:
            if InfoCandi["numero_resolucion"]==True and InfoCandi["cedula"]==True and InfoCandi["nombre"]==True and InfoCandi["apellido"]==True:
                pass
        except:
            return {"msg":"Faltan datos por llenar"}
        
        NuevoCandidato = Candidatos(InfoCandi)
        return self.RepositorioCandidatos.save(NuevoCandidato)

    def show(self, cedula):
        Candidato = Candidatos(self.RepositorioCandidatos.findById(cedula))
        return Candidato.__dict__

    def update(self, cedula, infoCandidatos):
        CandidatosActual = Candidatos(self.RepositorioCandidatos.findById(cedula))
        CandidatosActual.cedula = infoCandidatos["cedula"]
        CandidatosActual.numero_resolucion = infoCandidatos["numero_resolucion"]
        CandidatosActual.nombre = infoCandidatos["nombre"]
        CandidatosActual.apellido = infoCandidatos["apellido"]
        return self.RepositorioCandidatos.save(CandidatosActual)

    def delete(self, cedula):
        return self.RepositorioCandidatos.delete(cedula)

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidatos(self.RepositorioCandidatos.findById(id))
        partidoActual= Partido(self.RepositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.RepositorioCandidatos.save(candidatoActual)
