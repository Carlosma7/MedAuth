from .testUsuarioCliente import TestUsuarioCliente
from .especialidad import Especialidad
from typing import List
import datetime


class TestPrescripcion:
	def __init__(self, id_prescripcion: str, asegurado: TestUsuarioCliente, id_poliza: str, fecha_realizacion: datetime, especialidad: Especialidad, facultativo_prescriptor: str, facultativo_realizador: str, servicios_solicitados: List[str], consulta: str):
		self.__id_prescripcion = id_prescripcion
		self.__asegurado = asegurado
		self.__id_poliza = id_poliza
		self.__fecha_realizacion = fecha_realizacion
		self.__especialidad = especialidad
		self.__facultativo_prescriptor = facultativo_prescriptor
		self.__facultativo_realizador = facultativo_realizador
		self.__servicios_solicitados = servicios_solicitados[:]
		self.__consulta = consulta

		assert isinstance(self.__especialidad, Especialidad)

	def get_id_prescripcion(self):
		return self.__id_prescripcion

	def get_asegurado(self):
		return self.__asegurado

	def get_id_poliza(self):
		return self.__id_poliza

	def get_fecha_realizacion(self):
		return self.__fecha_realizacion

	def get_especialidad(self):
		return self.__especialidad

	def get_facultativo_prescriptor(self):
		return self.__facultativo_prescriptor

	def get_facultativo_realizador(self):
		return self.__facultativo_realizador

	def get_servicios_solicitados(self):
		return self.__servicios_solicitados

	def get_consulta(self):
		return self.__consulta

	def __eq__(self, otra):
		assert self.__id_prescripcion == otra.get_id_prescripcion()
		assert self.__asegurado == otra.get_asegurado()
		assert self.__id_poliza == otra.get_id_poliza()
		assert self.__fecha_realizacion == otra.get_fecha_realizacion()
		assert self.__especialidad == otra.get_especialidad()
		assert self.__facultativo_prescriptor == otra.get_facultativo_prescriptor()
		assert self.__facultativo_realizador == otra.get_facultativo_realizador()
		assert self.__servicios_solicitados == otra.get_servicios_solicitados()
		assert self.__consulta == otra.get_consulta()
    	
		return ((self.__id_prescripcion == otra.get_id_prescripcion()) and (self.__asegurado == otra.get_asegurado()) and (self.__id_poliza == otra.get_id_poliza()) and (self.__fecha_realizacion == otra.get_fecha_realizacion()) and (self.__especialidad == otra.get_especialidad()) and (self.__facultativo_prescriptor == otra.get_facultativo_prescriptor()) and (self.__facultativo_realizador == otra.get_facultativo_realizador()) and (self.__servicios_solicitados == otra.get_servicios_solicitados()) and (self.__consulta == otra.get_consulta()))

def test_compare_prescripcion():
	u = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	
	t1 = TestPrescripcion("PR-12345678", u, "MA-75925767-1", fecha, Especialidad.Traumatologia, "D. Fernando", "D. Juan", ["Radiografía", "Ortopedia"], "Centro médico capital, Sala 2")
	t2 = TestPrescripcion("PR-12345678", u, "MA-75925767-1", fecha, Especialidad.Traumatologia, "D. Fernando", "D. Juan", ["Radiografía", "Ortopedia"], "Centro médico capital, Sala 2")
	
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test
