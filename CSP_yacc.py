import CSP_lex
tokens = CSP_lex.tokens
import ply.yacc as yacc

def p_PROGRAMA(p):
    '''
    PROGRAMA : program id semicolon PROGRAMA_VARS PROGRAMA_FUNC main CUERPO
    '''

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
    VARS_LIST : list TIPO VARS_LIST_AUX semicolon
    '''

def p_VARS_LIST_AUX(p):
    '''
    VARS_LIST_AUX : id left_sb cteInt right_sb
                  | VARS_LIST_AUX comma id left_sb cteInt right_sb
    '''

def p_VARS_VAR(p):
    '''
    VARS_VAR : var TIPO VARS_VAR_AUX semicolon
    '''

def p_VARS_VAR_AUX(p):
    '''
    VARS_VAR_AUX : id
                 | VARS_VAR_AUX comma id
    '''

def p_TIPO(p):
    '''
    TIPO : int
         | float
         | bool
         | string
    '''

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
    RETORNO : return EXP
    '''

def p_FUNC(p):
    '''
    FUNC : TIPO id left_par FUNC_PARA right_par CUERPORETORNO
         | VOIDFUNC
    '''

def p_FUNC_PARA(p):
    '''
    FUNC_PARA : TIPO id
              | FUNC_PARA comma TIPO id
    '''

def p_VOIDFUNC(p):
    '''
    VOIDFUNC : void id left_par VOIDFUNC_PARA right_par left_cb CUERPOFUNC right_cb
    '''

def p_VOIDFUNC_PARA(p):
    '''
    VOIDFUNC_PARA : TIPO id
                  | VOIDFUNC_PARA comma TIPO id
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



yacc.yacc();
data = '''1+1'''
yacc.parse(data)


