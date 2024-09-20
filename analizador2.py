import ply.yacc as yacc
from tarealex import tokens, lexico  # Asegúrate de que los tokens estén correctamente importados

# Reglas para el analizador sintáctico
def p_statement_for(p):
    '''statement : PR'''
    p[0] = ('for', 'Correcto')

def p_statement_hola_mundo(p):
    '''statement : ID'''
    if p[1].lower() == 'hola' or p[1].lower() == 'mundo':  # .lower() para manejar mayúsculas y minúsculas
        p[0] = (p[1], 'ID')  # Aquí asignamos "ID" cuando es "HOLA" o "MUNDO"
    else:
        p[0] = (p[1], 'Incorrecto')  # Para cualquier otro identificador

# Regla para manejar errores de sintaxis
def p_error(p):
    print(f"Error de sintaxis en: {p.value if p else 'EOF'}")

# Crear el parser
parser = yacc.yacc()

# Función para realizar el análisis sintáctico
def analizar_sintaxis(entrada):
    resultado = []
    try:
        # Usamos el análisis léxico de 'lexico'
        tokens = lexico(entrada)
        parser.parse(entrada)  # Aquí se realiza el análisis sintáctico

        for token in tokens:
            if token['valor'].lower() == 'for':
                resultado.append({'linea': token['linea'], 'tipo': 'for', 'escritura': 'Correcto'})
            elif token['valor'].lower() == 'hola' or token['valor'].lower() == 'mundo':
                resultado.append({'linea': token['linea'], 'tipo': 'ID', 'escritura': f"{token['valor']} es un ID"})
            else:
                resultado.append({'linea': token['linea'], 'tipo': token['valor'], 'escritura': 'Incorrecto'})
    except Exception as e:
        print(f"Error de sintaxis: {e}")
        resultado.append({'linea': '-', 'tipo': '-', 'escritura': 'Error de sintaxis'})
    
    return resultado














