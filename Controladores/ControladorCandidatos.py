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
        NuevoCandidato = Candidatos(InfoCandi)
        return self.RepositorioCandidatos.save(NuevoCandidato)

    def show(self, cedula):
        Candidato = Candidatos(self.RepositorioCandidatos.findById(cedula))
        return Candidatos.__dict__

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
