import CSP_lex
import sys
tokens = CSP_lex.tokens
import ply.yacc as yacc

scope = 'global'
dicFunciones = {}
dicVarGlobales = {}
dicVarLocales = {}
parametros = []
tipoActual = None
funcActual = None
tipoDatoStruct = None
idFunc = None
idVar = None
cteLista = None
structAnt = None


def p_PROGRAMA(p):
    '''
    PROGRAMA : program id semicolon PROGRAMA_VARS cambiarScope PROGRAMA_FUNC main CUERPO
    '''
    print('ok')
    print("tabla de funciones: %s" % dicFunciones)
    print(" \n\n")
    print("Tabla de variables globales: %s" % dicVarGlobales)
    print(" \n\n")
    print("Tabla de variables en main: %s" % dicVarLocales)

def p_cambiarScope(p):
    '''
    cambiarScope : empty
    '''
    global scope
    if scope == 'global':
        scope = 'local'
    elif scope == 'local':
        scope = 'global'



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
    VARS_LIST : list hacerLista TIPO VARS_LIST_AUX semicolon
    '''

def p_hacerLista(p):
    '''
    hacerLista : empty
    '''
    global tipoDatoStruct
    tipoDatoStruct = 'list'

def p_VARS_LIST_AUX(p):
    '''
    VARS_LIST_AUX : id agregarId left_sb cteInt agregarCteLista right_sb agregarDicVar
                  | VARS_LIST_AUX comma id agregarId left_sb cteInt agregarCteLista right_sb agregarDicVar
    '''

def p_agregarId(p):
    '''
    agregarId : empty
    '''
    global idVar
    idVar = p[-1]

def p_agregarCteLista(p):
    '''
    agregarCteLista : empty
    '''
    global cteLista
    cteLista = p[-1]

def p_agregarDicVar(p):
    '''
    agregarDicVar : empty
    '''
    global scope
    global idVar
    global cteLista
    global tipoActual
    global tipoDatoStruct

    if scope == 'global':
        AgregarDicVarGlobal(idVar, tipoActual, tipoDatoStruct, cteLista)
    else:
        AgregarDicVarLocal(idVar, tipoActual, tipoDatoStruct, cteLista)


def p_VARS_VAR(p):
    '''
    VARS_VAR : var hacerVar TIPO VARS_VAR_AUX semicolon
    '''
def p_hacerVar(p):
    '''
    hacerVar : empty
    '''
    global tipoDatoStruct
    tipoDatoStruct = p[-1]

def p_VARS_VAR_AUX(p):
    '''
    VARS_VAR_AUX : id agregarId agregarDicVar
                 | VARS_VAR_AUX comma id agregarId agregarDicVar
    '''

def p_TIPO(p):
    '''
    TIPO : int cambioTipoActual
         | float cambioTipoActual
         | bool cambioTipoActual
         | string cambioTipoActual
    '''

def p_cambioTipoActual(p):
    '''
    cambioTipoActual : empty
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
    CUERPOFUNC_AUX : CUERPOFUNC_VARS CUERPOFUNC_ESTATUTO
                   | CUERPOFUNC_AUX CUERPOFUNC_VARS CUERPOFUNC_ESTATUTO
    '''

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

######## ALOMEJOR NO VAMOS A UTILIZAR ESTA ########
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

######## TERMINA PARTE QUE ALOMJER SE OMITE ########

def p_RETORNO(p):
    '''
    RETORNO : return EXP semicolon
    '''

def p_FUNC(p):
    '''
    FUNC : TIPO cambioFuncActual id agregarIdFunc left_par FUNC_PARA right_par CUERPORETORNO cambiarScope
         | VOIDFUNC cambiarScope
    '''
    global idFunc
    global funcActual
    global parametros

    AgregarDicFunc(idFunc, funcActual, parametros)

    dicVarLocales.clear()
    parametros = []

def p_cambioFuncActual(p):
    '''
    cambioFuncActual : empty
    '''
    global funcActual
    global tipoActual
    funcActual = tipoActual

def p_agregarIdFunc(p):
    '''
    agregarIdFunc : empty
    '''
    global idFunc
    idFunc = p[-1]

def p_FUNC_PARA(p):
    '''
    FUNC_PARA : TIPO id agregarParametro
              | FUNC_PARA comma TIPO id agregarParametro
    '''

def p_agregarParametro(p):
    '''
    agregarParametro : empty
    '''
    global parametros
    global tipoActual
    global dicVarLocales
    idParametro = p[-1]

    AgregarDicVarLocal(idParametro, tipoActual, 'var', None)
    parametros.append(dicVarLocales[idParametro])


def p_VOIDFUNC(p):
    '''
    VOIDFUNC : void hacerVoid id agregarIdFunc left_par VOIDFUNC_PARA right_par left_cb CUERPOFUNC right_cb
    '''

def p_hacerVoid(p):
    '''
    hacerVoid : empty
    '''
    global funcActual
    funcActual = p[-1]



def p_VOIDFUNC_PARA(p):
    '''
    VOIDFUNC_PARA : TIPO id agregarParametro
                  | VOIDFUNC_PARA comma TIPO id agregarParametro
    '''

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
    CONDICION : if CONDICION_ELSEIF CONDICION_ELSE 
    '''

def p_CONDICION_ELSEIF(p):
    '''
    CONDICION_ELSEIF : left_par EXPRESION right_par CUERPO
                     | CONDICION_ELSEIF elseif left_par EXPRESION right_par CUERPO
    '''

def p_CONDICION_ELSE(p):
    '''
    CONDICION_ELSE : else CUERPO
                   | empty
    '''

def p_CICLO(p):
    '''
    CICLO : while left_par EXPRESION right_par CUERPO
    '''

def p_LECTURA(p):
    '''
    LECTURA : cread left_par id right_par semicolon
    '''

def p_ESCRITURA(p):
    '''
    ESCRITURA : cwrite left_par EXPRESION right_par semicolon
    '''

def p_LLAMADA(p):
    '''
    LLAMADA : left_par LLAMADA_EXPRESION right_par semicolon
    '''

def p_LLAMADA_EXPRESION(p):
    '''
    LLAMADA_EXPRESION : EXPRESION
                      | LLAMADA_EXPRESION comma EXPRESION
    '''

def p_EXPRESION (p):
    '''
    EXPRESION : EXPRESION_NOT EXPRESIONLOGICA EXPRESION_B
    '''

def p_EXPRESION_NOT (p):
    '''
    EXPRESION_NOT : not
                | empty
    '''
def p_EXPRESION_B (p):
	'''
	EXPRESION_B : and EXPRESION_NOT EXPRESIONLOGICA
	           | or EXPRESION_NOT EXPRESIONLOGICA
			   | empty
	'''

def p_EXPRESIONLOGICA(p):
    '''
    EXPRESIONLOGICA :  EXP EXPRESIONLOGICA_AUX
    '''

def p_EXPRESIONLOGICA_AUX(p):
    '''
    EXPRESIONLOGICA_AUX : lt EXP
                        | gt EXP
                        | ne EXP
                        | ge EXP
                        | le EXP
                        | et EXP
                        | empty
    '''

def p_EXP(p):
    '''
    EXP : TERMINO EXP_AUX
    '''

def p_EXP_AUX(p):
    '''
    EXP_AUX : plus EXP
            | minus EXP
            | empty
    '''


def p_TERMINO(p):
    '''
    TERMINO : FACTOR TERMINO_AUX
    '''

def p_TERMINO_AUX(p):
    '''
    TERMINO_AUX : multiply TERMINO
                | divide TERMINO
                | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : left_par EXPRESION right_par
            | CONSTANTE
            | LISTA
            | FACTOR_AUX
    '''

def p_FACTOR_AUX(p):
    '''
    FACTOR_AUX : id
                | id LLAMADA_F
    '''

def p_LLAMADAF(p):
    '''
    LLAMADA_F : left_par EXPRESION LLAMADAF_AUX right_par
    '''

def p_LLAMADAF_AUX(p):
    '''
    LLAMADAF_AUX : comma EXPRESION LLAMADAF_AUX
                    | empty
    '''

def p_LISTA(p):
    '''
    LISTA : id left_sb EXP right_sb
    '''

def p_CONSTANTE(p):
    '''
    CONSTANTE : NUMERICA
              | BOOLEANA
              | STRINGS
    '''

def p_NUMERICA(p):
    '''
    NUMERICA : NUMERICA_AUX
             | plus NUMERICA_AUX
             | minus NUMERICA_AUX
    '''

def p_NUMERICA_AUX(p):
    '''
    NUMERICA_AUX : cteInt
                 | cteFloat
    '''

def p_BOOLEANA(p):
    '''
    BOOLEANA : true
             | false
    '''

def p_STRINGS(p):
    '''
    STRINGS : cteString
    '''

def p_ASIGNACION(p):
    '''
    ASIGNACION : ASIGNACION_AUX equals EXPRESION semicolon
    '''

def p_ASIGNACION_AUX(p):
    '''
    ASIGNACION_AUX : id
                   | LISTA
    '''

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_error(p):
    if p:
        print("Error de Sintaxis en '%s'" % p)
    else:
        print("Error de Sintaxis en EOF")


def AgregarDicVarGlobal(IdVar, TipoActual, TipoDatoStruct, CteLista):
    global dicVarGlobales

    if TipoDatoStruct == 'list':
        if IdVar in dicVarGlobales.keys():
            print("Error, ya existe la lista!")
        else:
            diccLista = {}
            dicVarGlobales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':CteLista, 'lista':diccLista}
    else:
        if IdVar in dicVarGlobales.keys():
            print("Error, ya existe la variable!")
        else:
            dicVarGlobales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':None, 'lista':None}


def AgregarDicVarLocal(IdVar, TipoActual, TipoDatoStruct, CteLista):
    global dicVarLocales

    if TipoDatoStruct == 'list':
        if IdVar in dicVarLocales.keys():
            print("Error, ya existe la lista!")
        else:
            diccLista = {}
            dicVarLocales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':CteLista, 'lista':diccLista}
    else:
        if IdVar in dicVarLocales.keys():
            print("Error, ya existe la variable!")
        else:
            dicVarLocales[IdVar] = {'id':IdVar, 'tipo':TipoActual, 'struct':TipoDatoStruct, 'tam':None, 'lista':None}


def AgregarDicFunc(IdFunc, FuncActual, Parametros):
    global dicFunciones

    if IdFunc in dicFunciones.keys():
        print("Error, ya existia esa funcion")
    else:
        dicFunciones[IdFunc] = {'id':IdFunc, 'tipo':FuncActual, 'pars':Parametros}

yacc.yacc();


data = """program compilador; 
          var int a; 
          int perro(int a)
          { 
          var int h, c; 
          if (c){
          h = c;
          }
          return c; 
          } 
          main 
          {
          list int hola[4];
          }
          """
yacc.parse(data)



