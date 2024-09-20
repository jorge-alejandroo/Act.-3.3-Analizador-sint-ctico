import ply.lex as lex

# Lista de tokens
tokens = (
    'FOR',
    'ID',
    'PR',
)

# Reglas de expresiones regulares para los tokens

def t_FORA(t):
    r'fora|FORA'
    t.type = 'ID'
    return t

def t_HOLA(t):
    r'hola|HOLA'
    t.type = 'ID'
    return t

def t_MUNDO(t):
    r'mundo|MUNDO'
    t.type = 'ID'
    return t

def t_FOR(t):
    r'for|FOR'
    t.type = 'PR'
    return t

# Regla para identificadores genéricos
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Manejo de saltos de línea para contar las líneas del código
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Crear el analizador léxico
def create_lexer():
    return lex.lex()

# Función de análisis léxico
def lexico(text):
    lexer = create_lexer()
    lexer.input(text)
    lexemes = []

    # Procesar cada token en el texto
    for tok in lexer:
        lexeme = {
            'linea': tok.lineno, 
            'tipo': tok.type, 
            'valor': tok.value
        }
        lexemes.append(lexeme)
    
    return lexemes






