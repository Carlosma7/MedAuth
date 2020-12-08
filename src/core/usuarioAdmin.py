from usuario import Usuario

# Clase de usuario administrativo
class UsuarioAdmin(Usuario):
	def __init__(self, nombre: str, email: str, dni: str, email_empresarial: str):
		self.__email_empresarial = email_empresarial
		super().__init__(nombre, email, dni)
	
	# Métodos get/set
	def get_email_empresarial(self):
		return self.__email_empresarial
	
	def set_email_empresarial(self, email_empresarial: str):
		self.__email_empresarial = email_empresarial
	
	# Override método equal
	def __eq__(self, otra):
		return super().__eq__(otra) and (self.__email_empresarial == otra.get_email_empresarial())
