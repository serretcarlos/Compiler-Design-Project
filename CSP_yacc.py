import CSP_lex
tokens = CSP_lex.tokens
import ply.yacc as yacc



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
    EXPRESIONLOGICA_AUX: lt EXP
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
    p_LLAMADAF_AUX : comma EXPRESION LLAMADAF_AUX
                    | empty
    '''

def p_empty(p):
    '''
    empty :
    '''



yacc.yacc();
data = '''1+1'''
yacc.parse(data)























yacc.yacc()
