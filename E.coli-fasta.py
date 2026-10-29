import requests
import os

print("Conectando con los servidores del NCBI...")

# ID de referencia real para el gen blaCTX-M-15
id_referencia = "NG_050503.1" 

url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={id_referencia}&rettype=fasta&retmode=text"

print(f"Descargando secuencia de referencia: {id_referencia}...")

respuesta = requests.get(url)

if len(respuesta.text.strip()) > 0 and ">" in respuesta.text:
    print("\n¡ÉXITO! Secuencia descargada.")
    
    # Obtener la ruta exacta
    ruta_actual = os.getcwd()
    nombre_archivo = "secuencia_blaCTX-M.fasta"
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)
    
    # Guardar en archivo
    with open(ruta_completa, "w") as archivo:
        archivo.write(respuesta.text)
        
    print(f"\n¡Archivo guardado exitosamente en esta ruta exacta!")
    print(f"--> {ruta_completa}")
    
    # Mostrar las letras
    lineas = respuesta.text.split('\n')
    print("\nPrimeras letras del ADN de la bacteria:")
    for linea in lineas:
        if not linea.startswith('>') and len(linea) > 0:
            print(linea[:150] + "...")
            break
else:
    print("El servidor no devolvió datos válidos.")