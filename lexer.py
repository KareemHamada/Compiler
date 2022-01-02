import ply.lex as lex

ds = input("Enter datasourse path : ")
ds = ds.split('\\')
ds = ds[-1]
fileType = ds.split('.')
fileType = fileType[-1]



reserved = {
    'select': 'SELECT',
    'distinct':'DISTINCT',
    'from'  : 'FROM',
    'where' : 'WHERE',
    'inner' : 'INNER',
    'left'  : 'LEFT',
    'right' : 'RIGHT',
    'full'  : 'FULL',
    'join'  : 'JOIN',
    'on'    : 'ON',
    'group' : 'GROUP',
    'by'    : 'BY',
    'having': 'HAVING',
    'order' : 'ORDER',
    'desc'  : 'DESC',
    'asc'   : 'ASC',
    'limit' : 'LIMIT',
    'insert': 'INSERT',
    'into'  : 'INTO',
    'values': 'VALUES',
    'update': 'UPDATE',
    'set'   : 'SET',
    'delete': 'DELETE',

    'create': 'CREATE',
    'table' : 'TABLE',
    'alter' : 'ALTER',
    'drop'  : 'DROP',
    'show'  : 'SHOW',

    'as'    : 'AS',
    'and'   : 'AND',
    'or'    : 'OR',
    'in'    : 'IN',
    'like'  : 'LIKE',
    'between': 'BETWEEN',
    'is'    : 'IS',
    'not'   : 'NOT',
    'null'  : 'NULL',
    'count' : 'COUNT',
    'sum'   : 'SUM',
    'avg'   : 'AVG',
    'min'   : 'MIN',
    'max'   : 'MAX',
    'int'   : 'INT',
    'integer' :'INTEGER',
    'smallint':'SMALLINT',
    'tinyint' :'TINYINT',
    'mediumint':'MEDIUMINT',
    'bigint'  : 'BIGINT',
    'float' :'FLOAT',
    'double':'DOUBLE',
    'decimal': 'DECIMAL',
    'char'  :'CHAR',
    'varchar': 'VARCHAR',
    'add'   : 'ADD',
    'column':'COLUMN'
}

tokens = (
    'COMPARISON',
    'STRING',
    'NUMBER',
    'QSTRING',
    'END',
    'COMMA',
    'DATASOURCE'

) + tuple(set(reserved.values()))

literals = '(){}@%.*[]:-^'
t_COMPARISON = r'<>|!=|>=|<=|=|>|<'
t_END = r';'
t_COMMA = r','
t_ignore = ' \t\n'
t_DATASOURCE = r'\[[^,\]\[]+\]'


def t_STRING(t):
    r"[a-zA-Z][_a-zA-Z0-9]*"
    t.type = reserved.get(t.value.lower(), 'STRING')
    if t.type != 'STRING':
        t.value = t.value.upper()
    return t

def t_QSTRING(t):
    r"('[^']*')|(\"[^\"]*\")|(`[^`]*`)"
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = int(t.value)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
# Test it out
data = input('sql>')

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
