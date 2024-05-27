import ply.lex as lex
tokens=('IF','LEFTBRACKET','RIGHTBRACKET','RIGHTBRACE','LEFTBRACE','ELSE','ID',
          
          'LESSER',
          'GREATER',
          'EQUALS',
          'NOT',
          'AND',
          'OR')
t_LEFTBRACKET = r'\('
t_RIGHTBRACKET=r'\)'
t_RIGHTBRACE=r'\}'
t_LEFTBRACE=r'\{'


def t_IF(t):
    r'if'
    return t

t_ignore = ' \t'

def t_ELSE(t):
    r'else'
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
