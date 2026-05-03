def secuencia_collatz(n):
    """Genera la secuencia de Collatz para un número n hasta llegar a 1."""
    pasos = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos.append(n)
    return pasos

def verificar_rango(p, q):
    """Verifica la conjetura en el intervalo [p, q] con la regla q >= 100p."""
    # Validación de la regla impuesta en el examen
    if q < 100 * p:
        return f"Error: No se cumple la regla q >= 100p (Actual: {q} < {100*p})"
    
    print(f"Demostrando conjetura en el intervalo [{p}, {q}]...")
    for i in range(p, q + 1):
        secuencia = secuencia_collatz(i)
        # Formatear la salida como en el ejemplo del PDF
        flechas = " -> ".join(map(str, secuencia))
        print(f"n={i}: {flechas}")
    
    return "\nDemostrado..."

if __name__ == "__main__":
    print("--- Verificador de Conjetura de Collatz (UNEG) ---")
    try:
        p = int(input("Ingrese el límite inferior (p): "))
        q = int(input("Ingrese el límite superior (q): "))
        
        resultado = verificar_rango(p, q)
        print(resultado)
    except ValueError:
        print("Error: Por favor ingrese solo números enteros.")