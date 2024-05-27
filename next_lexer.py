import ply.lex as lex

tokens = ('IF','FOR','WHILE',
        'LBRACKET','RBRACKET',
        'LESSER',
        'GREATER','NUM',
        'NOT',
        'AND',
        'OR',
        'EQUALS',
        'LFLOWER',
        'RFLOWER','NEXT','COLON',
        'ID','IN')
t_LBRACKET = r'\('
t_RBRACKET=r'\)'
t_RFLOWER=r'\}'
t_LFLOWER=r'\{'



def t_IF(t):
    r'if'
    return t

def t_FOR(t):
    r'for'
    return t

def t_COLON(t):
    r'\:'
    return t
    

def t_WHILE(t):
    r'while'
    return t

def t_NEXT(t):
    r'next'
    return t

def t_NUM(t):
    r'[0-9][0-9]*'
    return t

def t_IN(t):
    r'in'
    return t


t_ignore = ' \t'



def t_ID(t):
    r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b |\b(\d+)\b'
    return t

t_LESSER = r'<'
t_GREATER = r'>'
t_EQUALS = r'=(=)?'
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'

def t_error(t):
    print(f"Illegal character encountered {t.value[0]}")
    t.lexer.skip(1)

lexer=lex.lex()

data=input()
lexer.input(data)

while(1):
    tok=lexer.token()
    if not tok:
        break
    print(tok)




