from CSP_Cubo import *
from Memoria import *

def inicializarMaquinaVIrtual(idPrograma, dicQuadruplos, dicFunciones, dicVarGlobales, dicVarLocales, dicConstantes, dicTemporales):

	memPrincipal = Memoria(idPrograma)

	memPrincipal.guardaConstantes(dicConstantes)
	quadCont = 0


	while dicQuadruplos[quadCont]['operador'] != 'END':
		op= dicQuadruplos[quadCont]['operador']

		if op == '-':
			print("hola")
