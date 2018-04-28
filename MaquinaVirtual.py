from CSP_Cubo import *
from Memoria import *

def inicializarMaquinaVirtual(idPrograma, dicQuadruplos, dicFunciones, dicVarGlobales, dicVarLocales, dicConstantes, dicTemporales):

	print("ID DE GLOBALES EN MQUINA VIRTUAL")
	print(id(dicVarGlobales))

	memPrincipal = Memoria(idPrograma, dicConstantes, dicVarGlobales, dicVarLocales, dicTemporales)


	nomMem = memPrincipal.getIdPrograma()
	print("Nombre: %s" % nomMem)

	stackMemoria = []
	stackSaltos = []
	quadCont = 0

	while dicQuadruplos[quadCont]['operador'] != 'END':

		currentQuad = dicQuadruplos[quadCont]
		operador = currentQuad['operador']
		opIzq = currentQuad['izq']
		opDer = currentQuad['der']
		resultado = currentQuad['res']

		if operador == '+':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			suma = opIzq + opDer
			memPrincipal.guardarValDir(suma, resultado)

		elif operador == '-':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)
			print("OpIzq: %s\n OpDer: %s" % (opIzq, opDer))

			resta = opIzq - opDer
			memPrincipal.guardarValDir(resta, resultado)

		elif operador == '*':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			multiplicacion = opIzq * opDer
			memPrincipal.guardarValDir(multiplicacion, resultado)

		elif operador == '/':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			division = opIzq / opDer
			memPrincipal.guardarValDir(division, resultado)

		elif operador == '=':
			opDer = memPrincipal.getValorDir(opDer)

			memPrincipal.guardarValDir(opDer, resultado)

		elif operador == '<':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			menorQue = opIzq < opDer
			memPrincipal.guardarValDir(menorQue, resultado)

		elif operador == '>':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			mayorQue = opIzq > opDer
			memPrincipal.guardarValDir(mayorQue, resultado)

		elif operador == '<=':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			menorIgual = opIzq <= opDer
			memPrincipal.guardarValDir(menorIgual, resultado)

		elif operador == '>=':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			mayorIgual = opIzq > opDer
			memPrincipal.guardarValDir(mayorIgual, resultado)

		elif operador == '!=':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			noIgual = opIzq != opDer
			memPrincipal.guardarValDir(noIgual, resultado)

		elif operador == '==':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			igualIgual = opIzq == opDer 
			memPrincipal.guardarValDir(igualIgual, resultado)

		elif operador == '&&':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			simboloAnd = opIzq and opDer 
			memPrincipal.guardarValDir(simboloAnd, resultado)

		elif operador == '||':
			opIzq = memPrincipal.getValorDir(opIzq)
			opDer = memPrincipal.getValorDir(opDer)

			simboloOr = opIzq or opDer 
			memPrincipal.guardarValDir(simboloOr, resultado)

		elif operador == 'cwrite':

			opDer = memPrincipal.getValorDir(opDer)
			print(opDer)

		elif operador == 'cread':
			tipo = memPrincipal.getTipoDir(resultado)
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
			memPrincipal.guardarValDir(cRead, resultado)

		elif operador == 'ERA':
			funcion = dicFunciones[resultado]
			tempsFuncion = funcion['temps']
			varsFuncion = funcion['vars']
			memERA = Memoria(resultado, dicConstantes, dicVarGlobales, varsFuncion, tempsFuncion)
			stackMemoria.append(memERA)

		elif operador == 'Param':
			valorParam = memPrincipal.getValorDir(opIzq)
			memAux = stackMemoria.pop()
			memAux.guardarValDir(valorParam, resultado)
			stackMemoria.append(memAux)

		elif operador == 'GoSub':
			stackSaltos.append(quadCont)
			quadCont = resultado - 1
			memAux = stackMemoria.pop()
			stackMemoria.append(memPrincipal)
			memPrincipal = memAux

		elif operador == 'EndSub':
			memPrincipal = stackMemoria.pop()
			quadCont = stackSaltos.pop()

		elif operador == 'Return':
			valorRetorno = memPrincipal.getValorDir(opIzq)
			dirRetorno = dicFunciones[memPrincipal.getIdPrograma()]['dirRet']

			print(opIzq)
			print(valorRetorno)
			print(dirRetorno)
			memPrincipal.guardarValDir(valorRetorno, dirRetorno)
			print(memPrincipal.getIdPrograma(),id(memPrincipal.getValorDir(dirRetorno)))

		elif operador == 'GoTo':
			quadCont = resultado - 1

		elif operador == 'GoToF':
			valorEval = memPrincipal.getValorDir(opDer)
			if valorEval == False:
				quadCont = resultado - 1


		quadCont += 1

	print("MEMORIA DESPUES DE WHILE:")
	memPrincipal.imprimirValores('const', 'ints')
	memPrincipal.imprimirValores('const', 'floats')
	memPrincipal.imprimirValores('const', 'strings')
	memPrincipal.imprimirValores('const', 'bools')
	memPrincipal.imprimirValores('global', 'ints')
	memPrincipal.imprimirValores('global', 'floats')
	memPrincipal.imprimirValores('global', 'strings')
	memPrincipal.imprimirValores('global', 'bools')
	memPrincipal.imprimirValores('local', 'ints')
	memPrincipal.imprimirValores('local', 'floats')
	memPrincipal.imprimirValores('local', 'strings')
	memPrincipal.imprimirValores('local', 'bools')
	memPrincipal.imprimirValores('temp', 'ints')
	memPrincipal.imprimirValores('temp', 'floats')
	memPrincipal.imprimirValores('temp', 'strings')
	memPrincipal.imprimirValores('temp', 'bools')
	

