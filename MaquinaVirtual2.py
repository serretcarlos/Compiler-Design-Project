from CSP_Cubo import *
from Memoria3 import *


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

mapaMemoria = {
	'global': {
		'ints': {},
		'floats': {},
		'strings': {},
		'bools': {}
	},
	'const': {
		'ints': {},
		'floats': {},
		'strings': {},
		'bools': {}
	},
}

def guardaConstantes(dicConstantes):
	global mapaMemoria
	for a in dicConstantes.keys():
		if dicConstantes[a]['tipo'] == 'int':
			pos = a-constInts
			if pos < 0:
				print("Error, la constante %s guardada en la posicion %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'],a))
				exit()
			mapaMemoria['const']['ints'][pos] = dicConstantes[a]['val']

		elif dicConstantes[a]['tipo'] == 'float':
			pos = a-constFloats
			if pos < 0:
				print("Error, la constante %s guardada en la posicion %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'],a))
				exit()
			mapaMemoria['const']['floats'][pos] = dicConstantes[a]['val']

		elif dicConstantes[a]['tipo'] == 'string':
			pos = a-constStrings
			if pos < 0:
				print("Error, la constante %s guardada en la posicion %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'],a))
				exit()
			mapaMemoria['const']['strings'][pos] = dicConstantes[a]['val']

		elif dicConstantes[a]['tipo'] == 'bool':
			pos = a-constBools
			if pos < 0:
				print("Error, la constante %s guardada en la posicion %s esta fuera del rango de memoria (el indice es negativo)" % (dicConstantes[a]['val'],a))
				exit()
			mapaMemoria['const']['bools'][pos] = dicConstantes[a]['val']

def generaGlobales(dicVarGlobales):
	for a in dicVarGlobales.keys():
		if dicVarGlobales[a]['tipo'] == 'int':
			pos = dicVarGlobales[a]['dir'] - globalInts
			if pos < 0:
				print("Error, la variable global %s guardada en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (a, dicVarGlobales[a]['dir']))
				exit()
			mapaMemoria['global']['ints'][pos] = None

		elif dicVarGlobales[a]['tipo'] == 'float':
			pos = dicVarGlobales[a]['dir'] - globalFloats
			if pos < 0:
				print("Error, la variable global %s guardada en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (a, dicVarGlobales[a]['dir']))
				exit()
			mapaMemoria['global']['floats'][pos] = None

		elif dicVarGlobales[a]['tipo'] == 'string':
			pos = dicVarGlobales[a]['dir'] - globalStrings
			if pos < 0:
				print("Error, la variable global %s guardada en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (a, dicVarGlobales[a]['dir']))
				exit()
			mapaMemoria['global']['strings'][pos] = None

		elif dicVarGlobales[a]['tipo'] == 'bool':
			pos = dicVarGlobales[a]['dir'] - globalBools
			if pos < 0:
				print("Error, la variable global %s guardada en la pos %s esta fuera del rango de memoria (el indice es negativo)" % (a, dicVarGlobales[a]['dir']))
				exit()
			mapaMemoria['global']['bools'][pos] = None

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
		elif direccion >= 2000 and direccion <= 2999:
			return 'floats'
		elif direccion >= 3000 and direccion <= 3999:
			return 'strings'
		elif direccion >= 4000 and direccion <= 4999:
			return 'bools'

	elif scope == 'local':
		if direccion >= 5000 and direccion <= 6999:
			return 'ints'
		elif direccion >= 7000 and direccion <= 8999:
			return 'floats'
		elif direccion >= 9000 and direccion <= 10999:
			return 'strings'
		elif direccion >= 11000 and direccion <= 12999:
			return 'bools'

	elif scope == 'temp':
		if direccion >= 13000 and direccion <= 14999:
			return 'ints'
		elif direccion >= 15000 and direccion <= 16999:
			return 'floats'
		elif direccion >= 17000 and direccion <= 18999:
			return 'strings'
		elif direccion >= 19000 and direccion <= 20999:
			return 'bools'

	elif scope == 'const':
		if direccion >= 21000 and direccion <= 22999:
			return 'ints'
		elif direccion >= 23000 and direccion <= 24999:
			return 'floats'
		elif direccion >= 25000 and direccion <= 26999:
			return 'strings'
		elif direccion >= 27000 and direccion <= 28999:
			return 'bools'
	else:
		print("Error, no se pudo encontrar el tipo usando el scope!")
		exit()

def getValor(direccion, exStack):
	global mapaMemoria
	scope = getScopeDir(direccion)
	tipo = getTipoScope(direccion, scope)
	llave = direccion - basesMem[scope][tipo]['base']
	if scope == 'local' or scope == 'temp':
		valor = exStack.getValorMapaMem(scope, tipo, llave, direccion)
	else:
		valor = mapaMemoria[scope][tipo][llave]
	if valor == None:
		print("Error, variable de tipo %s en la direccion %s no tiene un valor asignado" % (tipo, direccion))
		exit()
	return valor

def guardarValDir(val, direccion, exStack):
	global mapaMemoria
	scope = getScopeDir(direccion)
	tipo = getTipoScope(direccion, scope)
	llave = direccion - basesMem[scope][tipo]['base']
	if scope == 'local' or scope == 'temp':
		exStack.guardaValMapaMem(val, scope, tipo, llave)
	else:
		mapaMemoria[scope][tipo][llave] = val

def getTipoDir(direccion):
	scope = getScopeDir(direccion)
	tipo = getTipoScope(direccion, scope)
	return tipo



def inicializarMaquinaVirtual(idPrograma, dicQuadruplos, dicFunciones, dicVarGlobales, dicVarLocales, dicConstantes, dicTemporales):
	global mapaMemoria

	guardaConstantes(dicConstantes)
	generaGlobales(dicVarGlobales)
	exeStack = ExecutionStack(idPrograma, dicFunciones['main']['cantVar'])

	stackExeStacks = []
	stackSaltos = []
	quadCont = 0

	while dicQuadruplos[quadCont]['operador'] != 'END':

		currentQuad = dicQuadruplos[quadCont]
		operador = currentQuad['operador']
		opIzq = currentQuad['izq']
		opDer = currentQuad['der']
		resultado = currentQuad['res']

		if type(opIzq) is str and opIzq.startswith('(') and opIzq.endswith(')'):
			opIzq = opIzq.replace('(', '')
			opIzq = opIzq.replace(')', '')
			opIzq = int(opIzq)
			opIzq = getValor(opIzq, exeStack)

		if type(opDer) is str and opDer.startswith('(') and opDer.endswith(')'):
			opDer = opDer.replace('(', '')
			opDer = opDer.replace(')', '')
			opDer = int(opDer)
			opDer = getValor(opDer, exeStack)

		if type(resultado) is str and resultado.startswith('(') and resultado.endswith(')'):
			resultado = resultado.replace('(', '')
			resultado = resultado.replace(')', '')
			resultado = int(resultado)
			resultado = getValor(resultado, exeStack)


		if operador == '+':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			suma = opIzq + opDer

			guardarValDir(suma, resultado, exeStack)

		elif operador == '-':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			resta = opIzq - opDer
			guardarValDir(resta, resultado, exeStack)

		elif operador == '*':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			multiplicacion = opIzq * opDer
			guardarValDir(multiplicacion, resultado, exeStack)

		elif operador == '/':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			if opDer == 0:
				print("Error, no se puede dividir por cero!")
				exit()

			division = opIzq / opDer
			guardarValDir(division, resultado, exeStack)

		elif operador == '=':
			opDer = getValor(opDer, exeStack)

			guardarValDir(opDer, resultado, exeStack)

		elif operador == '<':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			menorQue = opIzq < opDer
			guardarValDir(menorQue, resultado, exeStack)

		elif operador == '>':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			mayorQue = opIzq > opDer
			guardarValDir(mayorQue, resultado, exeStack)

		elif operador == '<=':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			menorIgual = opIzq <= opDer
			guardarValDir(menorIgual, resultado, exeStack)

		elif operador == '>=':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			mayorIgual = opIzq >= opDer
			guardarValDir(mayorIgual, resultado, exeStack)

		elif operador == '!=':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			noIgual = opIzq != opDer
			guardarValDir(noIgual, resultado, exeStack)

		elif operador == '==':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			igualIgual = opIzq == opDer 
			guardarValDir(igualIgual, resultado, exeStack)

		elif operador == '&&':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			simboloAnd = opIzq and opDer 
			guardarValDir(simboloAnd, resultado, exeStack)

		elif operador == '||':
			opIzq = getValor(opIzq, exeStack)
			opDer = getValor(opDer, exeStack)

			simboloOr = opIzq or opDer 
			guardarValDir(simboloOr, resultado, exeStack)

		elif operador == '!':
			opDer = getValor(opDer, exeStack)

			valorNegado = not opDer
			guardarValDir(valorNegado, resultado, exeStack)

		elif operador == 'cwrite':
			opDer = getValor(opDer, exeStack)
			print(opDer)

		elif operador == 'cread':
			tipo = getTipoDir(resultado)
			if tipo == 'ints':
				cRead = int(raw_input())
			elif tipo == 'floats':
				cRead = float(raw_input())
			elif tipo == 'strings':
				cRead = str(raw_input())
			elif tipo == 'bools':
				cRead = raw_input()
				if cRead == 'True' or cRead == 'true' or cRead == '1':
					cRead = True
				elif cRead == 'False' or cRead =='false' or cRead == '0':
					cRead = False
				else:
					print("Error, el valor ingresado en el input no es de tipo booleano!")
					exit()
			guardarValDir(cRead, resultado, exeStack)

		elif operador == 'ERA':
			funcion = dicFunciones[resultado]
			memERA = ExecutionStack(resultado, funcion['cantVar'])
			stackExeStacks.append(memERA)

		elif operador == 'Param':
			valorParam = getValor(opIzq, exeStack)
			memAux = stackExeStacks.pop()
			guardarValDir(valorParam, resultado, memAux)
			stackExeStacks.append(memAux)

		elif operador == 'GoSub':
			stackSaltos.append(quadCont)
			quadCont = resultado - 1
			memAux = stackExeStacks.pop()
			stackExeStacks.append(exeStack)
			exeStack = memAux

		elif operador == 'EndSub':
			exeStack = stackExeStacks.pop()
			quadCont = stackSaltos.pop()

		elif operador == 'Return':
			valorRetorno = getValor(opIzq, exeStack)
			dirRetorno = dicFunciones[exeStack.getIdPrograma()]['dirRet']

			guardarValDir(valorRetorno, dirRetorno, exeStack)

		elif operador == 'GoTo':
			quadCont = resultado - 1

		elif operador == 'GoToF':
			valorEval = getValor(opDer, exeStack)
			if valorEval == False:
				quadCont = resultado - 1

		elif operador == 'VER':
			opIzq = getValor(opIzq, exeStack)

			if not(resultado >= opIzq and opIzq >= opDer):
				print("Error, se esta intentando accesar un espacio de memoria fuera del rango de la lista!")
				exit()


		quadCont += 1


	









