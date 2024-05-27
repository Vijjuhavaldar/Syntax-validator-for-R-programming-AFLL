import ply.yacc as yacc
from for_lexer import tokens

flag = 0
#  global variable used to indicate whether a syntax error has occurred during parsing.

def p_while(p):
    '''
    for_statement : FOR LBRACE ID IN NUM COLON NUM RBRACE LFLOWER statements RFLOWER
      | FOR LBRACE ID IN ID RBRACE LFLOWER statements RFLOWER
      | FOR LBRACE ID IN NUM COLON NUM RBRACE singleStatement
      | FOR LBRACE ID IN ID RBRACE singleStatement
    '''
    # if len(p) == 12:
    #     p[0] = (p[1], p[3], p[4], p[5], p[6], p[7], p[10])  
    # elif len(p) == 8:
    #     p[0] = (p[1], p[3], p[4], p[5], p[7])
    # elif len(p) == 10 and p[6] == ':':
    #     p[0] = (p[1], p[3], p[4], p[5], p[6], p[7], p[9])
    # else:
    #     p[0] = (p[1], p[3], p[4], p[5], p[8])

        
def p_statements(p):
    '''
    statements  : statements statement
                | statement
    '''
    if len(p) == 2:
        p[0] = (p[1],)
    else:
        p[0] = p[1]+(p[2],)

def p_statement(p):
    '''
    statement   : list 
                | for_statement
                | empty
    '''

def p_singleStatement(p):
    '''
    singleStatement : list
                    | empty
                    | for_statement
    '''
 

def p_list(p):
    '''
    list    : ID list
            | ID
    '''

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None




def p_error(p):
    print("Syntax error",p)
    global flag 
    flag = 1


print("Welcome,You are entering for loop declaration")
parser = yacc.yacc()
while True:
   flag = 0
   try:
       s = input('enter the conditional statement:')
   except EOFError:
       break
   if not s: 
            flag = 0
            continue
   result = parser.parse(s)
   if flag == 0:
        print("Valid syntax")
        print("Result:", result)