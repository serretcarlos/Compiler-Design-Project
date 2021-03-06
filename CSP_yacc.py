import CSP_lex
from CSP_Cubo import *
from MaquinaVirtual2 import *
import sys
tokens = CSP_lex.tokens
import ply.yacc as yacc

scope = 'global'
dicFunciones = {}
dicVarGlobales = {}
dicVarLocales = {}
dicTemporales = {}
dicConstantes = {}
dicQuadruplos = {}
parametros = []
tipoActual = None
funcActual = None
tipoDatoStruct = None
idFunc = None
funcCall = None
idVar = None
cteLista = 0
structAnt = None
pOper = []
pilaO = []
pTipos = []
pSaltos = []
pDimensionadas = []
tCont = 0
quadCont = 0
funcQuad = None
paramCont = 0
sigNum = None
idPrograma = None

#memoria variables globales

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

def p_PROGRAMA(p):
    '''
    PROGRAMA : program id nt_pushJmpMain semicolon PROGRAMA_VARS nt_cambiarScope PROGRAMA_FUNC nt_cambiarScope main nt_ambienteMain CUERPO nt_endQuad
    '''


def p_nt_cambiarScope(p):
    '''
    nt_cambiarScope : empty
    '''
    global scope
    if scope == 'global':
        scope = 'local'
    elif scope == 'local':
        scope = 'global'

def p_nt_ambienteMain(p):
    '''
    nt_ambienteMain : nt_cambiarScope
    '''
    global dicQuadruplos
    global quadCont
    global dicFunciones

    dicFunciones['main']['inicio']= quadCont

    dicQuadruplos[0]['res'] = quadCont

def p_nt_endQuad(p):
    '''
    nt_endQuad : empty
    '''
    global quadCont
    global dicQuadruplos
    global dicVarLocales
    global dicTemporales
    global idPrograma
    global dicFunciones

    AgregarDicFunc2('main', dicVarLocales, dicTemporales)
    dicQuadruplos[quadCont]={'operador': 'END', 'izq': None, 'der': None, 'res':None}
    quadCont += 1

def p_nt_pushJmpMain(p):
    '''
    nt_pushJmpMain : empty
    '''
    global dicQuadruplos
    global quadCont
    global idPrograma
    global dicFunciones

    dicFunciones['main'] = {'id': 'main', 'tipo': 'void', 'inicio': None , 'pars': None, 'vars': None, 'cantVar': None, 'temps': None, 'dirRet': None}

    idPrograma = p[-1]
    dicQuadruplos[quadCont]={'operador': 'GoTo', 'izq': None, 'der': None, 'res': None}
    quadCont += 1

def p_PROGRAMA_VARS(p):
    '''
    PROGRAMA_VARS : VARS
                  | empty
    '''

def p_PROGRAMA_FUNC(p):
    '''
    PROGRAMA_FUNC : PROGRAMA_FUNC_AUX
                  | PROGRAMA_FUNC PROGRAMA_FUNC_AUX
    '''

def p_PROGRAMA_FUNC_AUX(p):
    '''
    PROGRAMA_FUNC_AUX : FUNC
                      | empty
    '''

def p_VARS(p):
    '''
    VARS : VARS_AUX
    '''

def p_VARS_AUX(p):
    '''
    VARS_AUX : VARS_LIST_VAR
             | VARS_AUX VARS_LIST_VAR
    '''

def p_VARS_LIST_VAR(p):
    '''
    VARS_LIST_VAR : VARS_LIST
                  | VARS_VAR
    '''

def p_VARS_LIST(p):
    '''
    VARS_LIST : list nt_hacerLista TIPO VARS_LIST_AUX semicolon
    '''

def p_nt_hacerLista(p):
    '''
    nt_hacerLista : empty
    '''
    global tipoDatoStruct
    tipoDatoStruct = 'list'

def p_VARS_LIST_AUX(p):
    '''
    VARS_LIST_AUX : id nt_agregarId left_sb cteInt nt_agregarCteLista right_sb nt_agregarDicVar
                  | VARS_LIST_AUX comma id nt_agregarId left_sb cteInt nt_agregarCteLista right_sb nt_agregarDicVar
    '''

def p_nt_agregarId(p):
    '''
    nt_agregarId : empty
    '''
    global idVar
    global dicVarLocales
    global dicVarGlobales

    idVar = p[-1]

    if idVar in dicVarGlobales.keys():
        print("Error, ya se habia declarado la variable '%s' en el scope global!" % idVar)
        exit()
    elif idVar in dicVarLocales.keys():
        print("Error, ya se habia declarado la variable '%s' en el scope local!" % idVar)
        exit()

def p_nt_agregarCteLista(p):
    '''
    nt_agregarCteLista : empty
    '''
    global cteLista
    cteLista = p[-1]
    if cteLista == 0:
        print("Error, no se puede declarar una lista con cero espacios!")
        exit()
    else:
        cteLista -= 1

def p_nt_agregarDicVar(p):
    '''
    nt_agregarDicVar : empty
    '''
    global scope
    global idVar
    global cteLista
    global tipoActual
    global tipoDatoStruct
    global dicMemorias

    if scope == 'global':
        llave = list(dicMemorias[scope][tipoActual].keys())[0]
        dirmem = dicMemorias[scope][tipoActual][llave]+llave
        dicMemorias[scope][tipoActual][llave] = dicMemorias[scope][tipoActual][llave] + cteLista + 1
        AgregarDicVarGlobal(idVar, tipoActual, tipoDatoStruct, cteLista, dirmem)
    else:
        llave = list(dicMemorias[scope][tipoActual].keys())[0]
        dirmem = dicMemorias[scope][tipoActual][llave]+llave
        dicMemorias[scope][tipoActual][llave] = dicMemorias[scope][tipoActual][llave] + cteLista + 1

        AgregarDicVarLocal(idVar, tipoActual, tipoDatoStruct, cteLista, dirmem)

def p_VARS_VAR(p):
    '''
    VARS_VAR : var nt_hacerVar TIPO VARS_VAR_AUX semicolon
    '''

def p_nt_hacerVar(p):
    '''
    nt_hacerVar : empty
    '''
    global tipoDatoStruct
    global cteLista
    tipoDatoStruct = p[-1]
    cteLista = 0

def p_VARS_VAR_AUX(p):
    '''
    VARS_VAR_AUX : id nt_agregarId nt_agregarDicVar
                 | VARS_VAR_AUX comma id nt_agregarId nt_agregarDicVar
    '''

def p_TIPO(p):
    '''
    TIPO : int nt_cambioTipoActual
         | float nt_cambioTipoActual
         | bool nt_cambioTipoActual
         | string nt_cambioTipoActual
    '''

def p_nt_cambioTipoActual(p):
    '''
    nt_cambioTipoActual : empty
    '''
    global tipoActual
    tipoActual = p[-1]

def p_CUERPO(p):
    '''
    CUERPO : left_cb CUERPO_AUX right_cb
    '''

def p_CUERPO_AUX(p):
    '''
    CUERPO_AUX : CUERPO_VARS CUERPO_ESTATUTO
               | CUERPO_AUX CUERPO_VARS CUERPO_ESTATUTO
    '''

def p_CUERPO_VARS(p):
    '''
    CUERPO_VARS : VARS
                | empty
    '''

def p_CUERPO_ESTATUTO(p):
    '''
    CUERPO_ESTATUTO : ESTATUTO
                    | empty
    '''

def p_CUERPOFUNC(p):
    '''
    CUERPOFUNC : CUERPOFUNC_AUX
    '''

def p_CUERPOFUNC_AUX(p):
    '''
    CUERPOFUNC_AUX : CUERPOFUNC_VARS nt_funcInicio CUERPOFUNC_ESTATUTO
                   | CUERPOFUNC_AUX CUERPOFUNC_VARS nt_funcInicio CUERPOFUNC_ESTATUTO
    '''
def p_nt_funcInicio(p):
    '''
    nt_funcInicio : empty
    '''
    global funcQuad
    global quadCont

    funcQuad = quadCont

def p_CUERPOFUNC_VARS(p):
    '''
    CUERPOFUNC_VARS : VARS 
                    | empty
    '''

def p_CUERPOFUNC_ESTATUTO(p):
    '''
    CUERPOFUNC_ESTATUTO : ESTATUTO
                        | empty
    '''

def p_CUERPORETORNO(p):
    '''
    CUERPORETORNO : left_cb CUERPORETORNO_AUX right_cb
    '''

def p_CUERPORETORNO_AUX(p):
    '''
    CUERPORETORNO_AUX : CUERPORETORNO_CF_AUX RETORNO
                      | CUERPORETORNO_AUX CUERPORETORNO_CF_AUX RETORNO
    '''

def p_CUERPORETORNO_CF_AUX(p):
    '''
    CUERPORETORNO_CF_AUX : CUERPOFUNC
                         | empty
    '''


def p_RETORNO(p):
    '''
    RETORNO : return EXP nt_checaRet semicolon
    '''

def p_nt_checaRet(p):
    '''
    nt_checaRet : empty
    '''
    global pilaO
    global pTipos
    global funcActual

    global dicQuadruplos
    global quadCont

    lastT = pTipos.pop()
    lastO = pilaO.pop()
    '''if lastO in dicVarLocales.keys():
        tipoLastO = dicVarLocales[lastO]['tipo']
    elif lastO in dicVarGlobales.keys():
        tipoLastO = dicVarGlobales[lastO]['tipo']
    elif lastO in dicVarConstantes.keys():
        tipoLastO = dicVarConstantes[lastO]['tipo']
    elif lastO in dicTemporales.keys():
        tipoLastO = dicTemporales[lastO]['tipo']
    else:
        print("Error, el valor que se va a retornar no existe!")
        exit()'''

    if lastT != funcActual:
        print("Error, el tipo del valor de retorno no es igual al de la funcion!")
        exit()
    else:
        dicQuadruplos[quadCont]={'operador': 'Return', 'izq': lastO, 'der': None, 'res': None}
        quadCont += 1
        pilaO.append(lastO)
        pTipos.append(lastT)

def p_FUNC(p):
    '''
    FUNC : TIPO nt_cambioFuncActual id nt_agregarIdFunc left_par FUNC_PARA right_par CUERPORETORNO nt_pushEndsub
         | VOIDFUNC nt_pushEndsub
    '''
    global idFunc
    global funcActual
    global parametros
    global dicVarLocales
    global funcQuad
    global dicTemporales
    global dicMemorias
    global tCont

    dLocales = dict(dicVarLocales)
    dTemps = dict(dicTemporales)


    AgregarDicFunc2(idFunc, dLocales, dTemps)

    
    dicVarLocales.clear()
    dicTemporales.clear()
    tCont = 0;

    parametros = []
    dicMemorias['local']['int'][5000] = 0
    dicMemorias['local']['float'][7000] = 0
    dicMemorias['local']['string'][9000] = 0
    dicMemorias['local']['bool'][11000] = 0

    dicMemorias['temp']['int'][13000] = 0
    dicMemorias['temp']['float'][15000] = 0
    dicMemorias['temp']['string'][17000] = 0
    dicMemorias['temp']['bool'][19000] = 0


def p_nt_pushEndsub(p):
    '''
    nt_pushEndsub : empty
    '''
    global quadCont
    global dicQuadruplos

    dicQuadruplos[quadCont]={'operador': 'EndSub', 'izq': None, 'der': None, 'res': None}
    quadCont += 1

def p_nt_cambioFuncActual(p):
    '''
    nt_cambioFuncActual : empty
    '''
    global funcActual
    global tipoActual

    funcActual = tipoActual



def p_nt_agregarIdFunc(p):
    '''
    nt_agregarIdFunc : empty
    '''
    global idFunc
    global dicFunciones
    global funcActual
    global dicVarGlobales
    global dicMemorias
    global quadCont

    idFunc = p[-1]
    if idFunc in dicFunciones.keys():
        print("Error, ya existe la funcion '" + idFunc + "'!")
        exit()
    else:
        if funcActual != 'void':
            llave = list(dicMemorias['global'][funcActual].keys())[0]
            dirmem = dicMemorias['global'][funcActual][llave]+llave
            dicMemorias['global'][funcActual][llave] += 1
            idRet = 'ret' + idFunc
            AgregarDicVarGlobal(idRet, funcActual, 'var',None, dirmem)
        else:
            dirmem = None
        dicFunciones[idFunc] = {'id':idFunc, 'tipo':funcActual, 'inicio':quadCont, 'pars':None, 'vars': None, 'cantVar':None, 'temps': None, 'dirRet': dirmem }

def p_FUNC_PARA(p):
    '''
    FUNC_PARA : TIPO id nt_agregarParametro
              | FUNC_PARA comma TIPO id nt_agregarParametro
              | empty
    '''
    global idFunc
    global dicFunciones
    global parametros

    dicFunciones[idFunc]['pars'] = parametros



def p_nt_agregarParametro(p):
    '''
    nt_agregarParametro : empty
    '''
    global parametros
    global tipoActual
    global dicVarLocales
    global dicMemorias
    global scope

    idParametro = p[-1]
    llave = list(dicMemorias[scope][tipoActual].keys())[0]
    dirmem = dicMemorias[scope][tipoActual][llave]+llave
    dicMemorias[scope][tipoActual][llave] += 1

    AgregarDicVarLocal(idParametro, tipoActual, 'var', None, dirmem)
    parametros.append({'id': idParametro, 'tipo': tipoActual, 'dir':dirmem})


def p_VOIDFUNC(p):
    '''
    VOIDFUNC : void nt_hacerVoid id nt_agregarIdFunc left_par VOIDFUNC_PARA right_par left_cb CUERPOFUNC right_cb
    '''

def p_nt_hacerVoid(p):
    '''
    nt_hacerVoid : empty
    '''
    global funcActual
    funcActual = p[-1]


def p_VOIDFUNC_PARA(p):
    '''
    VOIDFUNC_PARA : TIPO id nt_agregarParametro
                  | VOIDFUNC_PARA comma TIPO id nt_agregarParametro
                  | empty
    '''
    global idFunc
    global dicFunciones
    global parametros

    dicFunciones[idFunc]['pars'] = parametros

def p_ESTATUTO(p):
    '''
    ESTATUTO : ASIGNACION
             | CONDICION
             | CICLO
             | LECTURA
             | ESCRITURA
             | LLAMADA
    '''

def p_CONDICION(p):
    '''
    CONDICION : if CONDICION_AUX
    '''

def p_CONDICION_AUX(p):
    '''
    CONDICION_AUX : left_par EXPRESION nt_checarBool right_par CUERPO ELSE_ELIF nt_pushSalto
    '''
def p_ELSE_ELIF(p):
    '''
    ELSE_ELIF : ELSE
              | ELIF
              | empty
    '''

def p_ELSE(p):
    '''
    ELSE : else nt_pushElse CUERPO
    '''

def p_ELIF(p):
    '''
    ELIF : elseif nt_pushElse CONDICION_AUX
    '''

def p_nt_checarBool(p):
    '''
    nt_checarBool : empty
    '''
    global pTipos
    global pilaO
    global quadCont
    global dicQuadruplos
    global pSaltos

    if pTipos:
        tipo = pTipos.pop()
        if tipo == 'bool':
            result = pilaO.pop()
            dicQuadruplos[quadCont]={'operador': 'GoToF', 'izq': None, 'der': result, 'res': None}
            pSaltos.append(quadCont)
            quadCont += 1
        else:
            print("Error, la expresion no se evaluo como un booleano!")
            exit()
    else:
        print("Error, la pila de tipos esta vacia!")
        exit()

def p_nt_pushSalto(p):
    '''
    nt_pushSalto : empty
    '''
    global pSaltos
    global quadCont
    global dicQuadruplos

    if pSaltos:
        end = pSaltos.pop()
        dicQuadruplos[end]['res'] = quadCont

def p_nt_pushElse(p):
    '''
    nt_pushElse : empty
    '''
    global pSaltos
    global quadCont
    global dicQuadruplos

    if pSaltos:
        dicQuadruplos[quadCont]={'operador': 'GoTo', 'izq': None, 'der': None, 'res': None}
        false = pSaltos.pop()
        pSaltos.append(quadCont)
        quadCont += 1
        dicQuadruplos[false]['res'] = quadCont



def p_CICLO(p):
    '''
    CICLO : while nt_saltoLoop left_par EXPRESION nt_checarBool right_par CUERPO nt_pushLoop
    '''

def p_nt_saltoLoop(p):
    '''
    nt_saltoLoop : empty
    '''
    global quadCont
    global pSaltos

    pSaltos.append(quadCont)

def p_nt_pushLoop(p):
    '''
    nt_pushLoop : empty
    '''
    global quadCont
    global dicQuadruplos
    global pSaltos

    end = pSaltos.pop()
    ret = pSaltos.pop()
    dicQuadruplos[quadCont]={'operador': 'GoTo', 'izq': None, 'der': None, 'res': ret}
    quadCont += 1
    dicQuadruplos[end]['res']=quadCont

def p_LECTURA(p):
    '''
    LECTURA : cread left_par id nt_leer right_par semicolon
    '''

def p_nt_leer(p):
    '''
    nt_leer : empty
    '''
    global dicVarGlobales
    global dicVarLocales
    global quadCont
    global dicQuadruplos

    varLeer = p[-1]

    if varLeer in dicVarGlobales.keys():
        result = dicVarGlobales[varLeer]['dir']
        dicQuadruplos[quadCont]={'operador': 'cread', 'izq': None, 'der': None, 'res': result}
        quadCont += 1
    elif varLeer in dicVarLocales.keys():
        result = dicVarLocales[varLeer]['dir']
        dicQuadruplos[quadCont]={'operador': 'cread', 'izq': None, 'der': None, 'res': result}
        quadCont += 1
    else:
        print("Error, la variable '"+ varLeer + "' no se ha declarado!")
        exit()


def p_ESCRITURA(p):
    '''
    ESCRITURA : cwrite left_par EXPRESION nt_escribir right_par semicolon
    '''

def p_nt_escribir(p):
    '''
    nt_escribir : empty
    '''
    global pilaO
    global quadCont
    global dicQuadruplos

    if pilaO:
        escritura = pilaO.pop()
        dicQuadruplos[quadCont]={'operador': 'cwrite', 'izq': None, 'der': escritura, 'res': None}
        quadCont += 1
    else:
        print("Error, no se evaluo bien la expresion que se quiso imprimir!")


def p_LLAMADA(p):
    '''
    LLAMADA : id nt_verificaFuncIdLlamada left_par nt_pushPOper nt_startERA LLAMADA_EXPRESION nt_verificaUltimo right_par nt_popPOper semicolon nt_pushGoSub
    '''

def p_nt_verificaFuncIdLlamada(p):
    '''
    nt_verificaFuncIdLlamada : empty
    '''
    global dicFunciones
    global funcCall
    global idFunc

    nombre = p[-1]


    if nombre not in dicFunciones.keys():
        if nombre == idFunc:
            if dicFunciones[nombre]['tipo'] != 'void':
                print("Error, no se puede hacer una llamada usando la funcion '%s' porque no hay una variable para asignar su valor de retorno!" % nombre)
                exit()
            funcCall = nombre
        else:
            print("Error, no existe la funcion %s!" % nombre)
            exit()
    else:
        if dicFunciones[nombre]['tipo'] != 'void':
            print("Error, no se puede hacer una llamada usando la funcion '%s' porque no hay una variable para asignar su valor de retorno!" % nombre)
            exit()
        funcCall = nombre

def p_LLAMADA_EXPRESION(p):
    '''
    LLAMADA_EXPRESION : LLAMADA_EXPRESION_AUX
                      | empty
    '''

def p_LLAMADA_EXPRESION_AUX(p):
    '''
    LLAMADA_EXPRESION_AUX : EXPRESION nt_verifyArgType
                      | LLAMADA_EXPRESION_AUX comma nt_paramPP EXPRESION nt_verifyArgType
    '''

def p_EXPRESION (p):
    '''
    EXPRESION : EXPRESION_NOT EXPRESIONLOGICA nt_checaAndOrNot EXPRESION_B
    '''

def p_nt_checaAndOrNot(p):
    '''
    nt_checaAndOrNot : empty
    '''
    global pOper
    global pilaO
    global tCont
    global quadCont
    global dicQuadruplos
    global dicTemporales
    global dicMemorias

    if pOper:
        operator = pOper.pop()

        if operator == '&&' or operator == '||':
            right_operand = pilaO.pop()
            right_type = pTipos.pop()
            left_operand = pilaO.pop()
            left_type = pTipos.pop()
            result_type = buscarCubo(left_type, right_type, operator)
            if result_type != 'error':
                llave = list(dicMemorias['temp'][result_type].keys())[0]
                dirmem = dicMemorias['temp'][result_type][llave]+llave
                dicMemorias['temp'][result_type][llave] += 1
                result = 't' + str(tCont)
                dicTemporales[tCont]={'id':result, 'tipo': result_type, 'dir':dirmem}
                tCont += 1
                dicQuadruplos[quadCont]={'operador': operator, 'izq': left_operand, 'der': right_operand, 'res': dirmem}
                quadCont += 1
                pilaO.append(dirmem)
                pTipos.append(result_type)
            else:
                print("Error, los tipos de datos de las variables '" + left_operand +"' y '"+ right_operand + "' son incompatibles!" )
                exit()
        elif operator == '!':
            right_operand = pilaO.pop()
            right_type = pTipos.pop()


            if right_type == 'bool':
                llave = list(dicMemorias['temp']['bool'].keys())[0]
                dirmem = dicMemorias['temp']['bool'][llave]+llave
                dicMemorias['temp']['bool'][llave] += 1
                result = 't' + str(tCont)
                dicTemporales[tCont]={'id':result, 'tipo': right_type, 'dir': dirmem}
                tCont += 1
                dicQuadruplos[quadCont]={'operador': operator, 'izq': None, 'der': right_operand, 'res': dirmem}
                quadCont += 1
                pilaO.append(dirmem)
                pTipos.append('bool')
            else:
                print("La expresion que se va a negar no se evalua como un booleano")
                exit()

        else:
            pOper.append(operator)

def p_EXPRESION_NOT (p):
    '''
    EXPRESION_NOT : not nt_pushPOper
                | empty
    '''

def p_EXPRESION_B(p):
	'''
	EXPRESION_B : and nt_pushPOper EXPRESION
	           | or nt_pushPOper EXPRESION
			   | empty
	'''

def p_EXPRESIONLOGICA(p):
    '''
    EXPRESIONLOGICA :  EXP EXPRESIONLOGICA_AUX
    '''

def p_EXPRESIONLOGICA_AUX(p):
    '''
    EXPRESIONLOGICA_AUX : lt nt_pushPOper EXP nt_checarRelop
                        | gt nt_pushPOper EXP nt_checarRelop
                        | ne nt_pushPOper EXP nt_checarRelop
                        | ge nt_pushPOper EXP nt_checarRelop
                        | le nt_pushPOper EXP nt_checarRelop
                        | et nt_pushPOper EXP nt_checarRelop
                        | empty
    '''

def p_nt_checarRelop(p):
    '''
    nt_checarRelop : empty
    '''
    global pOper
    global pilaO
    global tCont
    global quadCont
    global dicQuadruplos
    global dicTemporales
    global dicMemorias

    if pOper:
        operator = pOper.pop()

        if operator == '>' or operator == '<' or operator == '!=' or operator == '>=' or operator == '<=' or operator == '==':
            right_operand = pilaO.pop()
            right_type = pTipos.pop()
            left_operand = pilaO.pop()
            left_type = pTipos.pop()
            result_type = buscarCubo(left_type, right_type, operator)
            if result_type != 'error':
                llave = list(dicMemorias['temp'][result_type].keys())[0]
                dirmem = dicMemorias['temp'][result_type][llave]+llave
                dicMemorias['temp'][result_type][llave] += 1
                result = 't' + str(tCont)
                dicTemporales[tCont]={'id':result, 'tipo': result_type, 'dir': dirmem}
                tCont += 1
                dicQuadruplos[quadCont]={'operador': operator, 'izq': left_operand, 'der': right_operand, 'res': dirmem}
                quadCont += 1
                pilaO.append(dirmem)
                pTipos.append(result_type)
            else:
                print("Error, los tipos de datos de las variables '" + left_operand +"' y '"+ right_operand + "' son incompatibles!" )
                exit()
        else:
            pOper.append(operator)

def p_EXP(p):
    '''
    EXP : TERMINO nt_checar_sumas EXP_AUX
    '''

def p_nt_checar_sumas(p):
    '''
    nt_checar_sumas : empty
    '''
    global pOper
    global pilaO
    global tCont
    global quadCont
    global dicQuadruplos
    global dicTemporales
    global dicMemorias

    if pOper:
        operator = pOper.pop()

        if operator == '+' or operator == '-':
            right_operand = pilaO.pop()
            right_type = pTipos.pop()
            left_operand = pilaO.pop()
            left_type = pTipos.pop()
            result_type = buscarCubo(left_type, right_type, operator)
            if result_type != 'error':
                llave = list(dicMemorias['temp'][result_type].keys())[0]
                dirmem = dicMemorias['temp'][result_type][llave]+llave
                dicMemorias['temp'][result_type][llave] += 1
                result = 't' + str(tCont)
                dicTemporales[tCont]={'id': result, 'tipo': result_type, 'dir': dirmem}
                tCont += 1
                dicQuadruplos[quadCont]={'operador': operator, 'izq': left_operand, 'der': right_operand, 'res': dirmem}
                quadCont += 1
                pilaO.append(dirmem)
                pTipos.append(result_type)
            else:
                print("Error, los tipos de datos de las variables '" + left_operand +"' y '"+ right_operand + "' son incompatibles!" )
                exit()
        else:
            pOper.append(operator)



def p_EXP_AUX(p):
    '''
    EXP_AUX : plus nt_pushPOper EXP
            | minus nt_pushPOper EXP
            | empty
    '''


def p_TERMINO(p):
    '''
    TERMINO : FACTOR nt_checar_multis TERMINO_AUX
    '''

def p_nt_checar_multis(p):
    '''
    nt_checar_multis : empty
    '''
    global pOper
    global pilaO
    global tCont
    global quadCont
    global dicQuadruplos
    global dicTemporales
    global dicMemorias

    if pOper:
        operator = pOper.pop()

        if operator == '*' or operator == '/':
            right_operand = pilaO.pop()
            right_type = pTipos.pop()
            left_operand = pilaO.pop()
            left_type = pTipos.pop()
            result_type = buscarCubo(left_type, right_type, operator)
            if result_type != 'error':
                llave = list(dicMemorias['temp'][result_type].keys())[0]
                dirmem = dicMemorias['temp'][result_type][llave]+llave
                dicMemorias['temp'][result_type][llave] += 1
                result = 't' + str(tCont)
                dicTemporales[tCont]={'id': result, 'tipo': result_type, 'dir': dirmem}
                tCont += 1
                dicQuadruplos[quadCont]={'operador': operator, 'izq': left_operand, 'der': right_operand, 'res': dirmem}
                quadCont += 1
                pilaO.append(dirmem)
                pTipos.append(result_type)
            else:
                print("Error, los tipos de datos de las variables '" + left_operand +"' y '"+ right_operand + "'' son incompatibles!" )
                exit()
        else:
            pOper.append(operator)


def p_TERMINO_AUX(p):
    '''
    TERMINO_AUX : multiply nt_pushPOper TERMINO
                | divide nt_pushPOper TERMINO
                | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : left_par nt_pushPOper EXPRESION right_par nt_popPOper
            | CONSTANTE
            | LISTA
            | FACTOR_AUX
    '''

def p_FACTOR_AUX(p):
    '''
    FACTOR_AUX : id nt_pushPilaO nt_verificaVar
                | id nt_verificaFuncId LLAMADA_F
    '''

def p_nt_verificaVar(p):
    '''
    nt_verificaVar : empty
    '''
    global dicVarGlobales
    global dicVarLocales

    simbolo = p[-2]
    if simbolo in dicVarGlobales.keys():
        if dicVarGlobales[simbolo]['struct'] == 'list':
            print("Error, la lista '%s' tiene que tener corchetes con una expression que se evalue a uno de sus indices!" % simbolo)
            exit()
    elif simbolo in dicVarLocales.keys():
        if dicVarLocales[simbolo]['struct'] == 'list':
            print("Error, la lista '%s' tiene que tener corchetes con una expression que se evalue a uno de sus indices!" % simbolo)
            exit()



def p_nt_verificaFuncId(p):
    '''
    nt_verificaFuncId : empty
    '''
    global dicFunciones
    global funcCall
    global idFunc

    nombre = p[-1]


    if nombre not in dicFunciones.keys():
        if nombre == idFunc:
            if dicFunciones[nombre]['tipo'] == 'void':
                print("Error, no se puede usar la funcion '%s' dentro de una expresion porque no tiene un valor de retorno!" % nombre)
                exit()
            funcCall = nombre
        else:
            print("Error, no existe la funcion %s!" % nombre)
            exit()
    else:
        if dicFunciones[nombre]['tipo'] == 'void':
            print("Error, no se puede usar la funcion '%s' dentro de una expresion porque no tiene un valor de retorno!" % nombre)
            exit()
        funcCall = nombre

def p_LLAMADAF(p):
    '''
    LLAMADA_F : left_par nt_pushPOper nt_startERA LLAMADAF_AUX nt_verificaUltimo right_par nt_popPOper nt_pushGoSub nt_asignarRet
    '''

def p_LLAMADAF_AUX(p):
    '''
    LLAMADAF_AUX : LLAMADAF_AUX2
                 | empty
    '''

def p_LLAMADAF_AUX2(p):
    '''
    LLAMADAF_AUX2 : EXPRESION nt_verifyArgType
                  | LLAMADAF_AUX2 comma nt_paramPP EXPRESION nt_verifyArgType
    '''

def p_nt_paramPP(p):
    '''
    nt_paramPP : empty
    '''
    global paramCont 
    paramCont += 1

def p_nt_startERA(p):
    '''
    nt_startERA : empty
    '''
    global funcCall
    global dicQuadruplos
    global quadCont
    global paramCont

    dicQuadruplos[quadCont]={'operador': 'ERA', 'izq': None, 'der': None, 'res':funcCall}
    quadCont += 1
    paramCont = 0

def p_nt_verifyArgType(p):
    '''
    nt_verifyArgType : empty
    '''
    global paramCont
    global dicFunciones
    global dicQuadruplos
    global quadCont
    global funcCall
    global pilaO
    global pTipos

    if paramCont < len(dicFunciones[funcCall]['pars']):
        argument = pilaO.pop()
        argumentType = pTipos.pop()
        compParam = dicFunciones[funcCall]['pars'][paramCont]['tipo']

        if argumentType == compParam:
            dicQuadruplos[quadCont] = {'operador':'Param', 'izq': argument, 'der': None, 'res': dicFunciones[funcCall]['pars'][paramCont]['dir']}
            quadCont += 1
        else:
            print("Error, el parametro numero '%s' en la llamada de la funcion '%s' no es del tipo '%s'." % (paramCont+1, funcCall, argumentType))
            exit()
    else:
        print("no entre")

def p_nt_verificaUltimo(p):
    '''
    nt_verificaUltimo : empty
    '''
    global paramCont
    global dicFunciones
    global funcCall

    tamPar = len(dicFunciones[funcCall]['pars'])
    if(tamPar != 0):
        tamPar -= 1;
    if paramCont < tamPar:
        print("Error, parametros insuficientes en llamada de funcion %s" % funcCall)
        exit()
    elif paramCont > tamPar:
        print("TESTA AQUIIII", paramCont, tamPar)
        print("Error, parametros de mas en llamada de funcion %s" % funcCall)
        exit()

def p_nt_pushGoSub(p):
    '''
    nt_pushGoSub : empty
    '''
    global dicQuadruplos
    global quadCont
    global funcCall
    global dicFunciones

    initAddress = dicFunciones[funcCall]['inicio']
    dicQuadruplos[quadCont]={'operador': 'GoSub', 'izq': funcCall, 'der': None, 'res':initAddress}
    quadCont += 1

def p_nt_asignarRet(p):
    '''
    nt_asignarRet : empty
    '''
    global dicQuadruplos
    global quadCont
    global funcCall
    global dicFunciones
    global dicTemporales
    global dicMemorias
    global tCont
    global pilaO
    global pTipos

    tipo = dicFunciones[funcCall]['tipo']
    dirRet = dicFunciones[funcCall]['dirRet']
    llave = list(dicMemorias['temp'][tipo].keys())[0]
    dirmem = dicMemorias['temp'][tipo][llave]+llave
    dicMemorias['temp'][tipo][llave] += 1
    result =  't' + str(tCont)
    dicTemporales[tCont]={'id':result, 'tipo':tipo, 'dir':dirmem}
    tCont += 1
    dicQuadruplos[quadCont]={'operador': '=', 'izq': None, 'der': dirRet, 'res': dirmem}
    quadCont += 1
    pilaO.append(dirmem)
    pTipos.append(tipo)

def p_LISTA(p):
    '''
    LISTA : id nt_verificarVarDim left_sb EXP nt_pushVer right_sb
    '''

def p_nt_verificaVarDim(p):
    '''
    nt_verificarVarDim : empty
    '''
    global pDimensionadas
    global dicVarLocales
    global dicVarGlobales
    global pOper

    nombre = p[-1]

    if nombre in dicVarGlobales.keys():
        if dicVarGlobales[nombre]['struct'] != 'list':
            print("Error, la variable %s no es una lista!" % nombre)
            exit()

    elif nombre in dicVarLocales.keys():
        if dicVarLocales[nombre]['struct'] != 'list':
            print("Error, la variable %s no es una lista!" % nombre)
            exit()
            
    else:
        print("Error, la variable %s no ha sido declarada!" % nombre)
        exit()
    pOper.append('(')


def p_nt_pushVer(p):
    '''
    nt_pushVer : empty
    '''
    global pilaO
    global pOper
    global dicQuadruplos
    global quadCont
    global dicVarLocales
    global dicVarGlobales
    global tCont
    global dicTemporales
    global dicMemorias
    global dicConstantes

    nombre = p[-4]

    if nombre in dicVarGlobales.keys():
        limSup = dicVarGlobales[nombre]['tam']
        base = dicVarGlobales[nombre]['dir']
    elif nombre in dicVarLocales.keys():
        limSup = dicVarLocales[nombre]['tam']
        base = dicVarLocales[nombre]['dir']
    else:
        print("Error, no se encontro la variable!")
        exit()

    topePila = pilaO.pop()
    pilaO.append(topePila)

    dicQuadruplos[quadCont] = {'operador': 'VER', 'izq': topePila, 'der': 0, 'res': limSup }
    quadCont += 1


    aux1 = pilaO.pop()
    aux1_type = pTipos.pop()
    result_type = buscarCubo(aux1_type, 'int', '+')
    if result_type != 'error':

        llave = list(dicMemorias['temp'][result_type].keys())[0]
        dirmem = dicMemorias['temp'][result_type][llave]+llave
        dicMemorias['temp'][result_type][llave] += 1
        result = 't' + str(tCont)
        dicTemporales[tCont]={'id': result, 'tipo': result_type, 'dir':dirmem}
        tCont += 1

        dirmemBase = None
        for a in dicConstantes:
            if dicConstantes[a]['val'] == base:
                dirmemBase = dicConstantes[a]['dir']
        if dirmemBase == None:
            llave = list(dicMemorias['const']['int'].keys())[0]
            dirmemBase = dicMemorias['const']['int'][llave]+llave
            dicMemorias['const']['int'][llave] += 1
            dicConstantes[dirmemBase] = {'val': base, 'tipo': 'int', 'dir': dirmemBase}

        dirmemS = "("+ str(dirmem) + ")"
        dicQuadruplos[quadCont]={'operador': '+', 'izq': aux1, 'der': dirmemBase, 'res': dirmem}
        quadCont += 1
        pilaO.append(dirmemS)
        pTipos.append(result_type)
        pOper.pop()
    else:
        print("Error, tipo de variable a verificar no es entero!")




def p_CONSTANTE(p):
    '''
    CONSTANTE : NUMERICA
              | BOOLEANA
              | STRINGS
    '''


def p_NUMERICA(p):
    '''
    NUMERICA : NUMERICA_AUX
             | plus nt_sigMas NUMERICA_AUX
             | minus nt_sigMenos NUMERICA_AUX
    '''

def p_nt_sigMas(p):
    '''
    nt_sigMas : empty
    '''
    global sigNum
    sigNum = '+'

def p_nt_sigMenos(p):
    '''
    nt_sigMenos : empty
    '''
    global sigNum
    sigNum = '-'

def p_NUMERICA_AUX(p):
    '''
    NUMERICA_AUX : cteInt nt_pushInt
                 | cteFloat nt_pushFloat
    '''

#_----------ALOMEJOR SE TIENE QUE REVISAR ESTO--------------
def p_nt_pushInt(p):
    '''
    nt_pushInt : empty
    '''
    global pilaO
    global pTipos
    global sigNum
    global dicConstantes
    global dicMemorias

    llave = list(dicMemorias['const']['int'].keys())[0]
    dirmem = dicMemorias['const']['int'][llave]+llave
    dicMemorias['const']['int'][llave] += 1

    if sigNum == None:
        dicConstantes[dirmem] = {'val': p[-1], 'tipo': 'int', 'dir': dirmem}
        pilaO.append(dirmem)
    elif sigNum == '-':
        num = p[-1] * -1
        dicConstantes[dirmem] = {'val': num, 'tipo': 'int', 'dir': dirmem}
        pilaO.append(dirmem)
        sigNum = None
    else:
        dicConstantes[dirmem] = {'val': p[-1], 'tipo': 'int', 'dir': dirmem}
        pilaO.append(dirmem)
        sigNum = None
    pTipos.append('int')

def p_nt_pushFloat(p):
    '''
    nt_pushFloat : empty
    '''
    global pilaO
    global pTipos
    global sigNum
    global dicConstantes
    global dicMemorias

    llave = list(dicMemorias['const']['float'].keys())[0]
    dirmem = dicMemorias['const']['float'][llave]+llave
    dicMemorias['const']['float'][llave] += 1

    if sigNum == None:
        dicConstantes[dirmem] = {'val': p[-1], 'tipo': 'float', 'dir': dirmem}
        pilaO.append(dirmem)
    elif sigNum == '-':
        num = p[-1] * -1
        dicConstantes[dirmem] = {'val': num, 'tipo': 'float', 'dir': dirmem}
        pilaO.append(dirmem)
        sigNum = None
    else:
        dicConstantes[dirmem] = {'val': p[-1], 'tipo': 'float', 'dir': dirmem}
        pilaO.append(dirmem)
        sigNum = None
    pTipos.append('float')

def p_BOOLEANA(p):
    '''
    BOOLEANA : True
             | False
    '''
    global pilaO
    global pTipos
    global dicConstantes
    global dicMemorias

    llave = list(dicMemorias['const']['bool'].keys())[0]
    dirmem = dicMemorias['const']['bool'][llave]+llave
    dicMemorias['const']['bool'][llave] += 1

    if p[1] == 'False':
        valor = False
    else:
        valor = True

    dicConstantes[dirmem] = {'val': valor, 'tipo': 'bool', 'dir': dirmem}
    pilaO.append(dirmem)
    pTipos.append('bool')

def p_STRINGS(p):
    '''
    STRINGS : cteString
    '''
    global pilaO
    global pTipos
    global dicConstantes
    global dicMemorias

    llave = list(dicMemorias['const']['string'].keys())[0]
    dirmem = dicMemorias['const']['string'][llave]+llave
    dicMemorias['const']['string'][llave] += 1

    dicConstantes[dirmem] = {'val': p[1], 'tipo': 'string', 'dir': dirmem}
    pilaO.append(dirmem)
    pTipos.append('string')

def p_ASIGNACION(p):
    '''
    ASIGNACION : ASIGNACION_AUX equals nt_pushPOper EXPRESION nt_checaEquals semicolon
    '''

def p_nt_checaEquals(p):
    '''
    nt_checaEquals : empty
    '''
    global pOper
    global pilaO
    global quadCont
    global dicQuadruplos

    if pOper:
        operator = pOper.pop()

        if operator == '=':
            right_operand = pilaO.pop()
            right_type = pTipos.pop()
            left_operand = pilaO.pop()
            left_type = pTipos.pop()
            result_type = buscarCubo(left_type, right_type, operator)
            if result_type != 'error':
                dicQuadruplos[quadCont]={'operador': operator, 'izq': None, 'der': right_operand, 'res': left_operand}
                quadCont += 1
            else:
                print("Error, los tipos de datos de las variables '" + left_operand +"' y '"+ right_operand + "'' son incompatibles!" )
                exit()
        else:
            pOper.append(operator)

def p_ASIGNACION_AUX(p):
    '''
    ASIGNACION_AUX : id nt_pushPilaO nt_checaStruct
                   | LISTA
    '''

def p_nt_checaStruct(p):
    '''
    nt_checaStruct : empty
    '''
    global dicVarGlobales
    global dicVarLocales

    simbolo = p[-2]

    if simbolo in dicVarGlobales.keys():
        if dicVarGlobales[simbolo]['struct'] == 'list':
            print("Error, la lista '%s' no contiene indice!" % simbolo)
            exit()
    elif simbolo in dicVarLocales.keys():
        if dicVarLocales[simbolo]['struct'] == 'list':
            print("Error, la lista '%s' no contiene indice!" % simbolo)
            exit()


def p_nt_pushPilaO(p):
    '''
    nt_pushPilaO : empty
    '''
    global dicVarGlobales
    global dicVarLocales
    global pilaO
    global pTipos

    simbolo = p[-1]
    if simbolo in dicVarGlobales.keys():
        pilaO.append(dicVarGlobales[simbolo]['dir'])
        pTipos.append(dicVarGlobales[simbolo]['tipo'])
    elif simbolo in dicVarLocales.keys():
        pilaO.append(dicVarLocales[simbolo]['dir'])
        pTipos.append(dicVarLocales[simbolo]['tipo'])
    else:
        print("Error, la variable '" + simbolo + "'' no existe!")
        exit()

def p_nt_pushPOper(p):
    '''
    nt_pushPOper : empty
    '''
    global pOper

    simbolo = p[-1]
    pOper.append(simbolo)

def p_nt_popPOper(p):
    '''
    nt_popPOper : empty
    '''
    global pOper
    simbolo = pOper.pop()

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_error(p):
    if p:
        print("Error de Sintaxis en '%s'" % p)
        exit()
    else:
        print("Error de Sintaxis en EOF")
        exit()


def AgregarDicVarGlobal(IdVar, TipoActual, TipoDatoStruct, CteLista, dirmem):
    global dicVarGlobales

    if TipoDatoStruct == 'list':
        if IdVar in dicVarGlobales.keys():
            print("Error, ya existe la lista global '"+ IdVar+"'!")
            exit()
        else:
            diccLista = {}
            dicVarGlobales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':CteLista, 'lista':diccLista, 'dir':dirmem}
    else:
        if IdVar in dicVarGlobales.keys():
            print("Error, ya existe la variable global '" + IdVar + "'!")
            exit()
        else:
            dicVarGlobales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':cteLista, 'lista':None, 'dir':dirmem}


def AgregarDicVarLocal(IdVar, TipoActual, TipoDatoStruct, CteLista, dirmem):
    global dicVarLocales

    if TipoDatoStruct == 'list':
        if IdVar in dicVarLocales.keys():
            print("Error, ya existe la lista '" + IdVar + "'!")
            exit()
        else:
            diccLista = {}
            dicVarLocales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':CteLista, 'lista':diccLista, 'dir': dirmem}
    else:
        if IdVar in dicVarLocales.keys():
            print("Error, ya existe la variable '" + IdVar + "'!")
            exit()
        else:
            dicVarLocales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':cteLista, 'lista':None, 'dir': dirmem}

def AgregarDicFunc2(idFunc, Vars, Temps):
    global dicFunciones
    dicFunciones[idFunc]['vars'] = Vars
    dicFunciones[idFunc]['cantVar'] = calcularTam(Vars, Temps)
    dicFunciones[idFunc]['temps']= Temps


def AgregarDicFunc(IdFunc, FuncActual, Parametros, Vars, Inicio, Temps, dirmem):
    global dicFunciones

    if IdFunc in dicFunciones.keys():
        print("Error, ya existe la funcion '" + IdFunc +"'!")
        exit()
    else:
        dicFunciones[IdFunc] = {'id':IdFunc, 'tipo':FuncActual, 'inicio':Inicio, 'pars':Parametros, 'vars': Vars, 'cantVar':calcularTam(Vars, Temps), 'temps': Temps, 'dirRet': dirmem }


def calcularTam(Vars, Temps):
    dicTam = {'i':0, 'f':0, 's':0, 'b':0, 'iT':0, 'fT':0, 'sT':0, 'bT':0}

    for a in Vars:
        tipo = Vars[a]['tipo']
        if Vars[a]['struct'] == 'list':
            if tipo == 'int':
                dicTam['i'] = dicTam['i'] + Vars[a]['tam'] + 1
            elif tipo == 'float':
                dicTam['f'] = dicTam['f'] + Vars[a]['tam'] + 1
            elif tipo == 'string':
                dicTam['s'] = dicTam['s'] + Vars[a]['tam'] + 1
            elif tipo == 'bool':
                dicTam['b'] = dicTam['b'] + Vars[a]['tam'] + 1
            else:
                print("El tipo no esta declarado!")
        else:
            if tipo == 'int':
                dicTam['i'] += 1
            elif tipo == 'float':
                dicTam['f'] += 1
            elif tipo == 'string':
                dicTam['s'] += 1
            elif tipo == 'bool':
                dicTam['b'] += 1
            else:
                print("El tipo no esta declarado!")

    for a in Temps:
        tipo = Temps[a]['tipo']
        if tipo == 'int':
            dicTam['iT'] += 1
        elif tipo == 'float':
            dicTam['fT'] += 1
        elif tipo == 'string':
            dicTam['sT'] += 1
        elif tipo == 'bool':
            dicTam['bT'] += 1
        else:
            print("El temporal no tiene tipo!")

    return dicTam


yacc.yacc();



data = """

          """
yacc.parse(data)

inicializarMaquinaVirtual(idPrograma, dicQuadruplos, dicFunciones, dicVarGlobales, dicVarLocales, dicConstantes, dicTemporales)



