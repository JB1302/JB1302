"""
CONFIGURADOR PARA SIMULADOR DE ACTIVIDAD EN VM
Script auxiliar para configurar fácilmente los parámetros del simulador
"""

import pygetwindow as gw
import sys

def listar_ventanas_disponibles():
    """Lista todas las ventanas disponibles para ayudar a identificar la VM"""
    print("\n=== VENTANAS DISPONIBLES ===")
    ventanas = gw.getAllTitles()
    
    for i, titulo in enumerate(ventanas):
        if titulo and titulo.strip():  # Filtra títulos vacíos
            print(f"{i+1:2d}. {titulo}")
    
    print(f"\nTotal: {len([t for t in ventanas if t and t.strip()])} ventanas encontradas")

def buscar_vm_sugeridas():
    """Busca ventanas que podrían ser VMs basándose en nombres comunes"""
    palabras_clave_vm = [
        'vmware', 'virtualbox', 'vm', 'virtual', 'ubuntu', 'centos', 
        'debian', 'fedora', 'windows', 'linux', 'kali', 'parrot'
    ]
    
    print("\n=== VENTANAS QUE PODRÍAN SER VMs ===")
    ventanas = gw.getAllTitles()
    encontradas = []
    
    for titulo in ventanas:
        if titulo and titulo.strip():
            titulo_lower = titulo.lower()
            for palabra in palabras_clave_vm:
                if palabra in titulo_lower:
                    encontradas.append(titulo)
                    break
    
    if encontradas:
        for i, titulo in enumerate(encontradas):
            print(f"{i+1:2d}. {titulo}")
    else:
        print("No se encontraron ventanas que parezcan VMs")
    
    return encontradas

def generar_configuracion():
    """Genera un archivo de configuración personalizado"""
    print("\n=== CONFIGURADOR DE SIMULADOR ===")
    
    # Listar ventanas disponibles
    listar_ventanas_disponibles()
    buscar_vm_sugeridas()
    
    print("\n=== CONFIGURACIÓN ===")
    
    # Solicitar título de la VM
    vm_titulo = input("\nIngresa el título exacto de la ventana de tu VM: ").strip()
    
    if not vm_titulo:
        print("❌ Error: Debes especificar un título de ventana")
        return
    
    # Verificar que la ventana existe
    ventanas = gw.getWindowsWithTitle(vm_titulo)
    if not ventanas:
        print(f"⚠️ Advertencia: No se encontró una ventana con el título '{vm_titulo}'")
        continuar = input("¿Deseas continuar de todas formas? (s/n): ").lower()
        if continuar != 's':
            return
    
    # Solicitar otros parámetros
    try:
        duracion = int(input("Duración de la simulación en minutos (default: 5): ") or "5")
        intervalo_min = int(input("Intervalo mínimo entre acciones en segundos (default: 5): ") or "5")
        intervalo_max = int(input("Intervalo máximo entre acciones en segundos (default: 15): ") or "15")
    except ValueError:
        print("❌ Error: Los valores deben ser números enteros")
        return
    
    # Generar archivo de configuración
    config_content = f'''# Configuración generada automáticamente
VM_WINDOW_TITLE = "{vm_titulo}"
DURACION_MINUTOS = {duracion}
INTERVALO_MIN = {intervalo_min}
INTERVALO_MAX = {intervalo_max}
ZONA_SEGURA_X = 50
ZONA_SEGURA_Y = 50
'''
    
    # Guardar configuración
    with open('config_vm.py', 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print(f"\n✅ Configuración guardada en 'config_vm.py'")
    print(f"📝 Para usar esta configuración, copia estas líneas al inicio de simulador_actividad_vm.py:")
    print("\n" + "="*50)
    print(config_content)
    print("="*50)

if __name__ == "__main__":
    generar_configuracion()