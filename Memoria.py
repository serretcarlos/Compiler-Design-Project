from CSP_Cubo import *

'''
dicMemorias = {
    'global': {
        'int': {1000: 0},
        'float': {2000: 0},
        'string': {3000: 0},
        'bool': {4000: 0}
    },
    'local': {
        'int': {5000: 0},
        'float': {7000: 0},
        'string': {9000: 0},
        'bool': {11000: 0}
    },
    'temp': {
        'int': {13000: 0},
        'float': {15000: 0},
        'string': {17000: 0},
        'bool': {19000: 0}
    },
    'const': {
        'int': {21000: 0},
        'float': {23000: 0},
        'string': {25000: 0},
        'bool': {27000: 0}
    }
}
'''

globalInts = 1000
globalFloats = 2000
globalStrings = 3000
globalBools = 4000

localInts = 5000
localFloats = 7000
localStrings = 9000
localBools = 11000

tempInts = 13000
tempFloats = 15000
tempStrings = 17000
tempBools = 19000

constInts = 21000
constFloats = 23000
constStrings = 25000
constBools = 27000

basesMem = {
	'global': {
		'ints': {'base':globalInts},
		'floats': {'base':globalFloats},
		'strings': {'base':globalStrings},
		'bools': {'base':globalBools}
	},
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
	},
	'const': {
		'ints':{'base':constInts},
		'floats': {'base':constFloats},
		'strings': {'base':constStrings},
		'bools': {'base':constBools}
	}
}



class Memoria:
	def __init__(self, idF, dicConstantes, dicGlobales, dicLocales, dicTemporales):
		self.nombre = idF

		self.mapaMem = {
			'global': {
				'ints': {},
				'floats': {},
				'strings': {},
				'bools': {}
			},
			'local': {
				'ints':{},
				'floats': {},
				'strings': {},
				'bools': {}
			},
			'temp': {
				'ints': {},
				'floats': {},
				'strings': {},
				'bools': {}
			},
			'const': {
				'ints':{},
				'floats': {},
				'strings': {},
				'bools': {}
			}
		}
		print("ID DE GLOBALES EN CLASE MEMORIA")
		print(id(dicGlobales))

		#se crea copia de locales y temporales para que sea unico en esta memoria
		dicLocalesCopia = dict(dicLocales)
		dicTemporalesCopia = dict(dicTemporales)
		print("ID DE DE LOCALES EN MEMORIA")
		print(id(dicLocales))
		print("ID DE COPIA LOCALES EN MEMOERIA")
		print(id(dicLocalesCopia))

		self.guardaConstantes(dicConstantes)
		self.generaGlobales(dicGlobales)
		self.generaLocales(dicLocalesCopia)
		self.generaTemporales(dicTemporalesCopia)
		print("MAPA MEMORIA")
		print(self.mapaMem)

	def guardaConstantes(self, dicConstantes):
		for a in dicConstantes.keys():
			if dicConstantes[a]['tipo'] == 'int':
				pos = a-constInts
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'], a))
					exit()
				self.mapaMem['const']['ints'][pos]= dicConstantes[a]['val']

			elif dicConstantes[a]['tipo'] == 'float':
				pos = a-constFloats
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'],a))
					exit()
				self.mapaMem['const']['floats'][pos]= dicConstantes[a]['val']

			elif dicConstantes[a]['tipo'] == 'string':
				pos = a-constStrings
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'], a))
					exit()
				self.mapaMem['const']['strings'][pos]= dicConstantes[a]['val']

			elif dicConstantes[a]['tipo'] == 'bool':
				pos = a-constBools
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'], a))
					exit()
				self.mapaMem['const']['bools'][pos]= dicConstantes[a]['val']

	def generaGlobales(self, dicGlobales):
		for a in dicGlobales.keys():
			if dicGlobales[a]['tipo'] == 'int':
				pos = dicGlobales[a]['dir']-globalInts
				if pos < 0:
					print("Error, la variable global %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicGlobales[a]['dir']))
					exit()
				self.mapaMem['global']['ints'][pos] = None

			elif dicGlobales[a]['tipo'] == 'float':
				pos = dicGlobales[a]['dir']-globalFloats
				if pos < 0:
					print("Error, la variable global %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicGlobales[a]['dir']))
					exit()
				self.mapaMem['global']['floats'][pos] = None

			elif dicGlobales[a]['tipo'] == 'string':
				pos = dicGlobales[a]['dir']-globalStrings
				if pos < 0:
					print("Error, la variable global %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicGlobales[a]['dir']))
					exit()
				self.mapaMem['global']['strings'][pos] = None

			elif dicGlobales[a]['tipo'] == 'bool':
				pos = dicGlobales[a]['dir']-globalBools
				if pos < 0:
					print("Error, la variable global %s guardada en la pos %s esta furea del rango de memoria (el indice es negativo)" % (a, dicGlobales[a]['dir']))
					exit()
				self.mapaMem['global']['bools'][pos] = None
		print("ID GLOBALES EN FUNCION GENERA GLOBALES")
		print(id(dicGlobales))

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

	def imprimirValores(self, scopes, tipos):
		dirs=self.mapaMem[scopes][tipos].keys()
		dirReal = scopes + tipos.title()
		for a in dirs:
			print(a+basesMem[scopes][tipos]['base'] , self.mapaMem[scopes][tipos][a])
	
	def getIdPrograma(self):
		return self.nombre

	# regresa el valor guardado en una direccion de memoria
	def getValorDir(self, direccion):
		scope = getScopeDir(direccion)
		tipo = getTipoScope(direccion, scope)
		llave = direccion - basesMem[scope][tipo]['base']
		valor = self.mapaMem[scope][tipo][llave]
		if valor == None:
			print("Error, variable con scope %s y de tipo %s con direccion %s no inicializada en nombre func: %s!" % (scope, tipo, direccion, self.nombre))
			
		return valor

	# toma un valor y lo guarda en una direccion si los tipos son compatibles
	def guardarValDir(self, valor, direccion):
		scope = getScopeDir(direccion)
		tipo = getTipoScope(direccion, scope)
		llave = direccion - basesMem[scope][tipo]['base']
		self.mapaMem[scope][tipo][llave] = valor

	def getTipoDir(self, direccion):
		scope = getScopeDir(direccion)
		tipo = getTipoScope(direccion, scope)
		return tipo


#Funciones fuuera de la clase
def getScopeDir(direccion):
	if direccion >= 1000 and direccion <= 4999:
		return 'global'
	elif direccion >= 5000 and direccion <= 12999:
		return 'local'
	elif direccion >= 13000 and direccion <= 20999:
		return 'temp'
	elif direccion >= 21000 and direccion <= 28999:
		return 'const'
	else:
		print("Error, la direccion no esta mapeada correctamente! No se encontro un scope!")
		exit()

def getTipoScope(direccion, scope):
	if scope == 'global':
		if direccion >= 1000 and direccion <= 1999:
			return 'ints'
		elif direccion <= 2000 and direccion <= 2999:
			return 'floats'
		elif direccion >= 3000 and direccion <= 3999:
			return 'strings'
		elif direccion >= 4000 and direccion <= 4999:
			return 'bools'

	elif scope == 'local':
		if direccion >= 5000 and direccion <= 6999:
			return 'ints'
		elif direccion <= 7000 and direccion <= 8999:
			return 'floats'
		elif direccion >= 9000 and direccion <= 10999:
			return 'strings'
		elif direccion >= 11000 and direccion <= 12999:
			return 'bools'

	elif scope == 'temp':
		if direccion >= 13000 and direccion <= 14999:
			return 'ints'
		elif direccion <= 15000 and direccion <= 16999:
			return 'floats'
		elif direccion >= 17000 and direccion <= 18999:
			return 'strings'
		elif direccion >= 19000 and direccion <= 20999:
			return 'bools'

	elif scope == 'const':
		if direccion >= 21000 and direccion <= 22999:
			return 'ints'
		elif direccion <= 23000 and direccion <= 24999:
			return 'floats'
		elif direccion >= 25000 and direccion <= 26999:
			return 'strings'
		elif direccion >= 27000 and direccion <= 28999:
			return 'bools'
	else:
		print("Error, no se pudo encontrar el tipo usando el scope!")
		exit()



