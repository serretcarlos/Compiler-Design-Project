from CSP_Cubo import *

localInts = 5000
localFloats = 7000
localStrings = 9000
localBools = 11000

tempInts = 13000
tempFloats = 15000
tempStrings = 17000
tempBools = 19000

basesMem = {
	'local': {
		'ints':{'base':localInts},
		'floats': {'base':localFloats},
		'strings': {'base':localStrings},
		'bools': {'base':localBools}
	},
	'temp': {
		'ints': {'base':tempInts},
		'floats': {'base':tempFloats},
		'strings': {'base':tempStrings},
		'bools': {'base':tempBools}
	}
}

class ExecutionStack:

	def __init__(self, idF, dicLocales, dicTemporales):
		self.nombre = idF

		self.mapaMem = {
			'local': {
				'ints': {},
				'floats': {},
				'strings': {},
				'bools': {}
			},
			'temp': {
				'ints': {},
				'floats': {},
				'strings': {},
				'bools': {}
			}
		}

		dicLocalesCopia = dict(dicLocales)
		dicTemporalesCopia = dict(dicTemporales)

		#Aqui se puede mejorar usando el arreglo cantvar de la lista de funciones
		self.generaLocales(dicLocalesCopia)
		self.generaTemporales(dicTemporalesCopia)

	def generaLocales(self, dicLocales):
		for a in dicLocales.keys():
			if dicLocales[a]['tipo'] == 'int':
				pos = dicLocales[a]['dir']-localInts
				if pos < 0:
					print("Error, la variable local %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicLocales[a]['dir']))
					exit()
				self.mapaMem['local']['ints'][pos] = None

			elif dicLocales[a]['tipo'] == 'float':
				pos = dicLocales[a]['dir']-localFloats
				if pos < 0:
					print("Error, la variable local %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicLocales[a]['dir']))
					exit()
				self.mapaMem['local']['floats'][pos] = None

			elif dicLocales[a]['tipo'] == 'string':
				pos = dicLocales[a]['dir']-localStrings
				if pos < 0:
					print("Error, la variable local %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicLocales[a]['dir']))
					exit()
				self.mapaMem['local']['strings'][pos] = None

			elif dicLocales[a]['tipo'] == 'bool':
				pos = dicLocales[a]['dir']-localBools
				if pos < 0:
					print("Error, la variable local %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicLocal[a]['dir']))
					exit()
				self.mapaMem['local']['bools'][pos] = None

	def generaTemporales(self, dicTemporales):
		for a in dicTemporales.keys():
			if dicTemporales[a]['tipo'] == 'int':
				pos = dicTemporales[a]['dir']-tempInts
				if pos < 0:
					print("Error, la variable temporal %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicTemporales[a]['dir']))
					exit()
				self.mapaMem['temp']['ints'][pos] = None

			elif dicTemporales[a]['tipo'] == 'float':
				pos = dicTemporales[a]['dir']-tempFloats
				if pos < 0:
					print("Error, la variable temporal %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicTemporales[a]['dir']))
					exit()
				self.mapaMem['temp']['floats'][pos] = None

			elif dicTemporales[a]['tipo'] == 'string':
				pos = dicTemporales[a]['dir']-tempStrings
				if pos < 0:
					print("Error, la variable temporal %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicTemporales[a]['dir']))
					exit()
				self.mapaMem['temp']['strings'][pos] = None

			elif dicTemporales[a]['tipo'] == 'bool':
				pos = dicTemporales[a]['dir']-tempBools
				if pos < 0:
					print("Error, la variable temporal %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicTemporales[a]['dir']))
					exit()
				self.mapaMem['temp']['bools'][pos] = None

	def getIdPrograma(self):
		return self.nombre

	def getMapaMem(self):
		return self.mapaMem

	def getValorMapaMem(self, scope, tipo, llave, direccion):
		valor = self.mapaMem[scope][tipo][llave]
		if valor == None:
			print("Error, variable con scope %s y de tipo %s con direccion %s no inicializada en nombre func: %s!" % (scope, tipo, direccion, self.nombre))
			exit()
		return valor

	def guardaValMapaMem(self, valor, scope, tipo, llave):
		self.mapaMem[scope][tipo][llave] = valor












