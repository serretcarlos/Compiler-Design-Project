import ply.lex as lex
import sys

palabras_reservadas = {
	'program' : 'program',
	'main' : 'main',
	'true' : 'true',
	'false' : 'false',
	'while' : 'while',
	'if' : 'if',
	'else' : 'else',
	'elseif' : 'elseif',
	'cread' : 'cread',
	'cwrite' : 'cwrite',
	'void' : 'void',
	'return' : 'return',
	'int' : 'int',
	'float' : 'float',
	'bool' : 'bool',
	'string' : 'string',
	'list' : 'list',
	'var' : 'var'
}

tokens = [
#	'ASIGNACION',
#	'BOOLEANA',
#	'CICLO',
#	'CONDICION',
#	'CONSTANTE',
#	'CUERPO',
#	'CUERPOFUNC',
#	'CUERPORETORNO',
#	'ESCRITURA',
#	'ESTATUTO',
#	'EXP',
#	'EXPRESION',
#	'FACTOR',
#	'FUNC',
#	'LECTURA',
#	'LISTA',
#	'LLAMADA',
#	'LLAMADAF',
#	'NUMERICA',
#	'PROGRAMA',
#	'RETORNO',
#	'STRINGS',
#	'TERMINO',
#	'TIPO',
#	'VARS',
#	'VOIDFUNC',
	'id',
	'semicolon',
	'comma',
	'cteInt',
	'cteFloat',
	'cteString',
	'plus',
	'minus',
	'multiply',
	'divide',
	'equals',# '='
	'lt',# less than
	'gt',# greater than
	'le',# less than or equal to
	'ge',# greater than or equal to
	'ne',# not equal to '!='
	'not',# not
	'et',# equal to '=='
	'and',# &&
	'or',# ||
	'left_par',
	'right_par',
	'left_sb',
	'right_sb',
	'left_cb',
	'right_cb',
	'left_dblquotes',
	'right_dblquotes'
]

tokens += palabras_reservadas.values()

#expresiones regulares tokens
t_semicolon = r'\;'
t_comma = r'\,'
t_plus = r'\+'
t_minus = r'\-'
t_multiply = r'\*'
t_divide = r'\/'
t_equals = r'='
t_lt = r'\<'
t_gt = r'\>'
t_le = r'\<='
t_ge = r'\>='
t_ne = r'!='
t_not = r'!'
t_et = r'=='
t_and = r'&&'
t_or = r'\|\|'
t_left_par = r'\('
t_right_par = r'\)'
t_left_sb = r'\['
t_right_sb = r'\]'
t_left_cb = r'\{'
t_right_cb = r'\}'
t_left_dblquotes = r'"'
t_right_dblquotes = r'."'
t_ignore = ' \t'

def t_cteFloat(t):
	r'\d\.\d+'
	t.value = float(t.value)
	return t

def t_cteInt(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_cteString(t):
	r'\".*\"'
	t.value = str(t.value)
	return t

def t_id(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in palabras_reservadas:
		t.type = palabras_reservadas[t.value]
	return t

def t_newline(t):
	r'\n'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print("Caracteres ilegales '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()
