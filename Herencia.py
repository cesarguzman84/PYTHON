class Vehiculos():

	def __init__(self, marca, modelo):		#CONSTRUCTOR

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo", self.modelo, "\nEn marcha ", self.enmarcha, 
			"\nacelerado: ", self.acelera, "\nfrenado", self.frena)


class Furgoneta(Vehiculos):

		def carga(self, cargar):
			self.cargado=cargar
			if(self.cargado):
				return "La furgoneta esta cargada"
			else:
				return "La furgoneta no esta cargada"


class Moto(Vehiculos):		#OBJETO MOTO TIENE 6 METODOS: 1 EL COMPORTAMIENTO INICIAL DEL CONSTRUCTOR
	hcaballito=""			# + 4 QUE HEREDA DEL OBJETO VEHICULO + 1 PROPIO
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo", self.modelo, "\nEn marcha ", self.enmarcha, 
			"\nacelerado: ", self.acelera, "\nfrenado", self.frena, "\n", self.hcaballito)


class Velectricos():
	def __init__(self, marca, modelo):
		
		super().__init__(marca, modelo)

		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True


miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

class BicicletaElectrica(Velectricos, Vehiculos):		#ESTO ES HERENCIA MULTIPLE

	pass

miBici=BicicletaElectrica("Orbea", "hj500")