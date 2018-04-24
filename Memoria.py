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


class Memoria:
	def __init__(self, id):
		self.nombre = id

		self.arrGlobalesInt = [None] *1000
		self.arrGlobalesFloat = [None] *1000
		self.arrGlobalesString = [None] *1000
		self.arrGlobalesBool = [None] *1000

		self.arrLocalesInt = [None] *2000
		self.arrLocalesFloat = [None] *2000
		self.arrLocalesString = [None] *2000
		self.arrLocalesBool = [None] *2000

		self.arrTempsInt = [None] *2000
		self.arrTempsFloat = [None] *2000
		self.arrTempsString = [None] *2000
		self.arrTempsBool = [None] *2000

		self.arrConstInt = [None] * 2000
		self.arrConstFloat = [None] * 2000
		self.arrConstString = [None] * 2000
		self.arrConstBool = [None] * 2000


		self.stackSegment = []


	def guardaConstantes(self, dicConstantes):
		for a in dicConstantes.keys():
			if dicConstantes[a]['tipo'] == 'int':
				pos = a-constInts
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango (el indice es negativo)" % (a, dicConstantes[a]['val']))
					exit()

				self.arrConstInt[pos] = dicConstantes[a]['val']

			elif dicConstantes[a]['tipo'] == 'float':
				pos = a-constFloats
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango (el indice es negativo)" % (a, dicConstantes[a]['val']))
					exit()

				self.arrConstFloat[pos] = dicConstantes[a]['val']

			elif dicConstantes[a]['tipo'] == 'string':
				pos = a-constStrings
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango (el indice es negativo)" % (a, dicConstantes[a]['val']))
					exit()

				self.arrConstString[pos] = dicConstantes[a]['val']

			elif dicConstantes[a]['tipo'] == 'bool':
				pos = a-constBools
				if pos < 0:
					print("Error, la constante %s guardad en la pos %s esta fuera del rango (el indice es negativo)" % (a, dicConstantes[a]['val']))
					exit()
				self.arrConstBool[pos] = dicConstantes[a]['val']
			else:
				print("El tipo del constante no esta reconocido o no fue asignado")
				exit()

		print("Constatnes Enteras")
		for i in self.arrConstInt:
			if i == None:
				break
			else:
				print(i)
		print("\nConstantes FLotantes")
		for i in self.arrConstFloat:
			if i == None:
				break
			else:
				print(i)
		print("\nConstantes Strings")
		for i in self.arrConstString:
			if i == None:
				break
			else:
				print(i)
		print("\nCOnstantes booleanas")
		for i in self.arrConstBool:
			if i == None:
				break
			else:
				print(i)






