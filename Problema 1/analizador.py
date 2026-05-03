import re

def analizar_expresion(cadena):
    # Especificación de tokens basada en los requerimientos de la UNEG
    token_specification = [
        ('NUMERO',    r'\d+(\.\d+)?'),       # Enteros o reales con "."
        ('OPERADOR',  r'[\+\-\*/]'),        # + - * /
        ('PAREN_IZQ', r'\('),               # (
        ('PAREN_DER', r'\)'),               # )
        ('OPERANDO',  r'[a-zA-Z_][a-zA-Z0-9_]*'), # No inicia con número, sin espacios[cite: 1]
        ('SKIP',      r'\s+'),               # Ignorar espacios
        ('ERROR',     r'.'),                 # Cualquier otro caracter[cite: 1]
    ]
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    parentesis = 0

    for mo in re.finditer(tok_regex, cadena):
        kind = mo.lastgroup
        value = mo.group()
        
        if kind == 'SKIP':
            continue
        elif kind == 'PAREN_IZQ':
            parentesis += 1
        elif kind == 'PAREN_DER':
            parentesis -= 1
        
        tokens.append(f"{kind} {value}")

    resultado = " ".join(tokens)
    
    # Verificación de balanceo de paréntesis[cite: 1]
    if parentesis == 0:
        resultado += " PARÉNTESIS BALANCEADOS."
    else:
        resultado += " PARÉNTESIS NO BALANCEADOS."
        
    return resultado

# --- Bloque para interacción con el usuario ---
if __name__ == "__main__":
    print("--- Analizador Léxico (Prueba Diagnóstica UNEG) ---")
    print("Escribe 'salir' para terminar el programa.")
    
    while True:
        entrada = input("\nIngrese la expresión a analizar: ")
        
        if entrada.lower() == 'salir':
            print("Saliendo del programa...")
            break
            
        if not entrada.strip():
            continue
            
        print("Salida:")
        print(analizar_expresion(entrada))