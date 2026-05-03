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
            r'^[wb]$',                                               # Turno
            r'^(K?Q?k?q?|-)$',                                       # Enroque
            r'^([a-h][36]|-)$',                                      # Al paso
            r'^\d+$',                                                # Reloj
            r'^\d+$'                                                 # Jugadas
        ]
        
        for i, seccion in enumerate(partes):
            if not re.match(reglas[i], seccion):
                return f"ERROR en campo {i+1}: '{seccion}' no es valido."
        
        return "LA CADENA ES NOTACION FEN VALIDA."

if __name__ == "__main__":
    print("--- Validador de Notacion FEN ---")
    while True:
        try:
            entrada = input("\nIngrese la cadena FEN (o 'salir'): ")
            if entrada.lower() == 'salir': break
            print(ValidadorFEN.es_valido(entrada))
        except EOFError: # Evita el error al cerrar la terminal inesperadamente
            break