import CSP_lex
tokens = CSP_lex.tokens

import ply.yacc as yacc

def p_PROGRAMA(p):
	'''
	PROGRAMA : program ID SEMICOLON PROGRAMA_VARS PROGRAMA_FUNC main CUERPO
	'''
	print('Nombre programa: ', p[2])

def p_PROGRAMA_VARS(p):
	'''
	PROGRAMA_VARS : VARS
	              | empty
	'''
	p[0] = p[1]

def p_PROGRAMA_FUNC(p):
	'''
	PROGRAMA_FUNC : FUNC FUNC
	              | FUNC
	              | empty
	'''
	p[0] = p[1]

