import ply.yacc as yacc
from next_lexer import tokens
from next_lexer import data
flag=0


def p_nextstmt(p):
    '''
    nextstmt :  IF  LBRACKET condition RBRACKET LFLOWER statements NEXT RFLOWER 
             |  FOR LBRACKET ID IN NUM COLON NUM RBRACKET LFLOWER NEXT statements RFLOWER
             |  FOR LBRACKET ID IN ID RBRACKET LFLOWER NEXT statements RFLOWER
             |  FOR LBRACKET ID IN NUM COLON NUM RBRACKET NEXT singleStatement
             |  FOR LBRACKET ID IN ID RBRACKET NEXT singleStatement
             |  WHILE LBRACKET condition RBRACKET LFLOWER NEXT statements RFLOWER
             |  WHILE LBRACKET condition RBRACKET  NEXT singleStatement 
    '''
    # if (len(p) == 8 and p[1]=='IF'):
    #     p[0] = (p[1],p[3],p[6],p[7])
    # elif (len(p)==13 and p[0]=='FOR'):
    #     p[0]=  (p[1],p[3],p[4],p[5],p[6],p[7],p[10],p[11])
    # elif len(p) == 9 and p[0]=='FOR':
    #     p[0] = (p[1], p[3], p[4], p[5], p[7],p[8])
    # elif len(p) == 11 and p[6] == ':' and p[0]=='FOR':
    #     p[0] = (p[1], p[3], p[4], p[5], p[6], p[7], p[9],p[10])
    # elif (p[1]=='FOR'):
    #     p[0] = (p[1], p[3], p[4], p[5], p[8],p[9])
    # elif len(p) == 9 and p[0]=='WHILE':
    #     p[0] = (p[1],p[3],p[6],p[7])
    # else:
    #     p[0] = (p[1],p[3],p[5],p[6])



    


def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    # if len(p) == 2:
    #     p[0] = (p[1],)
    # else:
    #     p[0] = p[1]+(p[2],)


def p_statement(p):
    '''
    statement : list 
             | nextstmt
             | empty
    '''
    # p[0] = (p[1],) if len(p) == 2 else p[1]

def p_singleStatement(p):
    '''
    singleStatement  : list 
                    | empty
                    | nextstmt
    '''
    # if len(p) == 3:
    #     p[0] = (p[1],)
    # else:
    #     p[0] = p[1]

def p_list(p):
    '''
    list : ID list 
         | ID
    '''
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = [p[1]] + p[2]

def p_empty(p):
    '''
    empty :
    '''
    # p[0] = None


def p_condition(p):
    '''
    condition : ID EQUALS ID 
                | ID GREATER ID 
                | ID LESSER ID 
                | ID GREATER EQUALS ID 
                | ID LESSER EQUALS ID 
                | ID NOT EQUALS ID
                | condition AND condition
                | condition OR condition
                | ID
    '''
    
    # if len(p) == 2:
    #     p[0] = ('condition',p[1])
    # else:
    #     p[0] = ('condition',(p[1],p[2],p[3]))

def p_error(p):
    print("Syntax error")
    global flag
    flag = 1




parser=yacc.yacc()



while True:
    flag=0
    try:
        s=input('enter the declaration:')
    except EOFError:
        break
    if not s:
        flag=0
        continue
    result=parser.parse(s)
    if flag==0:
        print("Result:",result)
        print("VALID SYNTAX")
