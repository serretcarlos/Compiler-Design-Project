import ply.lex as lex
import sys

p_reservadas = {
	'program' : 'PROGRAM',
	'main' : 'MAIN',
	'true' : 'TRUE',
	'false' : 'FALSE',
	'while' : 'WHILE',
	'if' : 'IF',
	'else' : 'ELSE',
	'elseif' : 'ELSEIF',
	'cread' : 'CREAD',
	'cwrite' : 'CWRITE',
	'void' : 'VOID',
	'return' : 'RETURN',
	'int' : 'INT',
	'float' : 'FLOAT',
	'bool' : 'BOOL',
	'string' : 'STRING',
	'list' : 'LIST'
}

tokens = [
	'ASIGNACION',
	'BOOLEANA',
	'CICLO',
	'CONDICION',
	'CONSTANTE',
	'CUERPO',
	'CUERPOFUNC',
	'CUERPORETORNO',
	'ESCRITURA',
	'ESTATUTO',
	'EXP',
	'EXPRESION',
	'FACTOR',
	'FUNC',
	'LECTURA',
	'LISTA',
	'LLAMADA',
	'LLAMADAF',
	'NUMERICA',
	'PROGRAMA',
	'RETORNO',
	'STRINGS',
	'TERMINO',
	'TIPO',
	'VARS',
	'VOIDFUNC',
	'ID',
	'SEMICOLON',
	'COMMA',
	'cteInt',
	'cteFloat',
	'cteString',
	'PLUS',
	'MINUS',
	'MULTIPLY',
	'DIVIDE',
	'EQUALS',# '='
	'LT',# less than
	'GT',# greater than
	'LE',# less than or equal to
	'GE',# greater than or equal to
	'NE',# not equal to '!='
	'ET',# eqaul to '=='
	'AND',# &&
	'OR',# ||
	'LEFT_PAR',
	'RIGHT_PAR',
	'LEFT_SB',
	'RIGHT_SB',
	'LEFT_CB',
	'RIGHT_CB',
	'LEFT_DBLQUOTES',
	'RIGHT_DBLQUOTES'
]

#tokens = tokens + p_reservadas.values()
tokens += p_reservadas.values()

#expresiones regulares tokens
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'='
t_LT = r'\<'
t_GT = r'\>'
t_LE = r'\<='
t_GE = r'\>='
t_NE = r'!='
t_ET = r'=='
t_AND = r'&&'
t_OR = r'\|\|'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'
t_LEFT_SB = r'\['
t_RIGHT_SB = r'\]'
t_LEFT_CB = r'\{'
t_RIGHT_CB = r'\}'
t_LEFT_DBLQUOTES = r'"'
t_RIGHT_DBLQUOTES = r'."'
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
	t.value = string(t.value)
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = 'ID'
	return t

def t_error(t):
	print("Caracteres ilegales")
	t.lexer.skip(1)

lexer = lex.lex()
