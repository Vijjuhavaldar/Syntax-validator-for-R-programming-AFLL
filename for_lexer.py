import ply.lex as lex

tokens = ('FOR',  
        'LBRACE',
        'COLON',
        'IN',
        'RBRACE',
        'LFLOWER',
        'RFLOWER',
        'ID',
        'NUM',
        )  
# token is tuple that defines all the token that is recongnised by the lexer

def t_FOR(t):
    r'for'
    return t
# This function defines a token rule for the 'FOR' keyword. It uses a regular expression pattern (r'for') to match the string 'for' in the input.

def t_IN(t):
    r'in'
    return t

t_LBRACE = r'\('
t_RBRACE = r'\)'
t_LFLOWER = r'\{'
t_RFLOWER = r'\}'

def t_COLON(t):
    r'\:'
    return t

def t_ID(t):
    r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b'
    return t

def t_NUM(t):
    r'[0-9][0-9]*'
    return t

t_ignore = ' \t'
#  This line defines characters to be ignored by the lexer. In this case, spaces and tabs will be ignored.

def t_error(t):
    print(f"Illegal character found {t.value[0]}")
    t.lexer.skip(1)
# skip the illegal chratcer and display the error msg in that case

lexer = lex.lex()
# This line creates an instance of the lexer.

data = input()

lexer.input(data)
# This line sets the input for the lexer to the provided data.

while(1):
    tok = lexer.token()
    # This line retrieves the next token from the lexer.
    if not tok:
        break
    print(tok)