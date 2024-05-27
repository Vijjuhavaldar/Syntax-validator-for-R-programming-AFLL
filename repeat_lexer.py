import ply.lex as lex

tokens = ('REPEAT',
        'LBRACKET','RBRACKET',
        'LESSER',
        'GREATER',
        'NOT',
        'AND',
        'OR',
        'EQUALS',
        'LFLOWER',
        'RFLOWER',
        'ID','BREAK','IF')
t_LBRACKET = r'\('
t_RBRACKET=r'\)'
t_RFLOWER=r'\}'
t_LFLOWER=r'\{'

def t_REPEAT(t):
    r'repeat'
    return t

def t_IF(t):
    r'if'
    return t

t_ignore = ' \t'

def t_BREAK(t):
    r'break'
    return t

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




