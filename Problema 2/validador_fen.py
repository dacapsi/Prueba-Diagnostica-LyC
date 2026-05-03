import re

class ValidadorFEN:
    @staticmethod
    def es_valido(cadena):
        partes = cadena.split()
        if len(partes) != 6: 
            return "ERROR: Faltan campos (deben ser 6)."
        
        # Usamos r'' (raw strings) para evitar el error de \s y otros escapes
        reglas = [
            r'^([rnbqkpRNBQKP1-8]{1,8}/){7}[rnbqkpRNBQKP1-8]{1,8}$', # Piezas
            r'^[wb]$',                                               # Turno[cite: 1]
            r'^(K?Q?k?q?|-)$',                                       # Enroque[cite: 1]
            r'^([a-h][36]|-)$',                                      # Al paso[cite: 1]
            r'^\d+$',                                                # Reloj[cite: 1]
            r'^\d+$'                                                 # Jugadas[cite: 1]
        ]
        
        for i, seccion in enumerate(partes):
            if not re.match(reglas[i], seccion):
                return f"ERROR en campo {i+1}: '{seccion}' no es válido."
        
        return "LA CADENA ES NOTACIÓN FEN VALIDA."

if __name__ == "__main__":
    print("--- Validador de Notacion FEN (Problema 2) ---")
    while True:
        try:
            entrada = input("\nIngrese la cadena FEN (o 'salir'): ")
            if entrada.lower() == 'salir': break
            print(ValidadorFEN.es_valido(entrada))
        except EOFError: # Evita el error al cerrar la terminal inesperadamente
            break