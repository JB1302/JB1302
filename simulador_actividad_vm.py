"""
SIMULADOR DE ACTIVIDAD ARTIFICIAL EN VM - DEMOSTRACIÓN ÉTICA
Version: 2.0 (Solo para fines educativos)

Descripción:
Este script simula actividad humana en una máquina virtual (VM) mediante:
- Movimientos y clics de mouse realistas
- Escritura con errores humanos
- Navegación entre aplicaciones
- Intervalos variables entre acciones

Mecanismos de seguridad:
- Zona de emergencia (esquina superior izquierda) para detener inmediatamente
- Tiempo máximo de ejecución predefinido
- Restauración de estado original al finalizar

Requisitos:
pip install pyautogui pygetwindow
"""

import pyautogui
import pygetwindow as gw
import random
import time
import sys

# ================= CONFIGURACIÓN =================
VM_WINDOW_TITLE = "Nombre de tu VM aquí"  # Ej: "Ubuntu - VMware" o "Windows 10 Pro - VirtualBox"
DURACION_MINUTOS = 5                      # Duración total de la simulación
ZONA_SEGURA_X = 50                        # Coordenada X para detener emergencia (esquina superior izquierda)
ZONA_SEGURA_Y = 50                        # Coordenada Y para detener emergencia
INTERVALO_MIN = 5                         # Mínimo segundos entre acciones
INTERVALO_MAX = 15                        # Máximo segundos entre acciones

# ================ FUNCIONES PRINCIPALES ================

def encontrar_ventana_vm():
    """
    Localiza la ventana de la VM por título.
    Si no la encuentra, lista todas las ventanas disponibles y termina la ejecución.
    """
    try:
        # Busca ventanas que contengan el título especificado
        ventanas = gw.getWindowsWithTitle(VM_WINDOW_TITLE)
        if not ventanas:
            raise IndexError
        return ventanas[0]  # Devuelve la primera coincidencia
    except IndexError:
        print(f"\nERROR: No se encontró la ventana con título: '{VM_WINDOW_TITLE}'")
        print("Ventanas disponibles:")
        for i, titulo in enumerate(gw.getAllTitles()):
            if titulo:  # Filtra títulos vacíos
                print(f"{i+1}. {titulo}")
        sys.exit(1)

def activar_ventana(ventana):
    """Asegura que la ventana de la VM esté activa y maximizada"""
    if not ventana.isActive:
        ventana.activate()
        time.sleep(1)  # Espera para que la ventana responda
    
    if not ventana.isMaximized:
        ventana.maximize()
        time.sleep(0.5)

def mover_mouse_aleatorio(ventana):
    """
    Mueve el mouse a una posición aleatoria dentro de la VM
    con velocidad variable para simular movimiento humano
    """
    # Calcula coordenadas dentro del área de la VM
    x = random.randint(ventana.left + 10, ventana.left + ventana.width - 10)
    y = random.randint(ventana.top + 10, ventana.top + ventana.height - 10)
    
    # Mueve el mouse con velocidad aleatoria (entre 0.3 y 0.7 segundos)
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.7))

def escribir_texto_aleatorio():
    """
    Simula escritura humana con:
    - Palabras comunes de oficina
    - Errores tipográficos ocasionales
    - Velocidad variable entre teclas
    """
    palabras = ["informe", "reunion", "analisis", "datos", "proyecto", 
                "tesis", "python", "script", "automatizacion", "empresa"]
    
    palabra = random.choice(palabras)
    
    # Simula errores humanos (20% de probabilidad)
    if random.random() > 0.8:
        palabra = palabra[:-1]  # Omite última letra
    
    # Escribe con velocidad variable entre teclas
    pyautogui.typewrite(palabra + " ", interval=random.uniform(0.05, 0.2))

def navegacion_basica():
    """
    Simula pulsaciones de teclas comunes para navegación:
    - Tabulador para cambiar campos
    - Flechas para moverse
    - Enter para confirmar
    """
    teclas = ['tab', 'enter', 'down', 'right', 'esc', 'space']
    pyautogui.press(random.choice(teclas))

def cambio_aplicacion():
    """
    Simula cambio entre aplicaciones usando Alt+Tab
    con tiempo de espera variable entre acciones
    """
    with pyautogui.hold('alt'):
        pyautogui.press('tab')
    time.sleep(random.uniform(0.5, 1.5))

def interaccion_compleja(ventana, contador_verificacion):
    """
    Realiza una secuencia aleatoria de acciones dentro de la VM
    Verifica periódicamente que la VM siga activa
    """
    # Verificar cada 5 acciones si la VM sigue activa
    if contador_verificacion % 5 == 0:
        ventana_activa = gw.getActiveWindow()
        if ventana_activa is None or ventana.title != ventana_activa.title:
            print("⚠️ Ventana de VM perdió el foco. Re-activando...")
            activar_ventana(ventana)
    
    # Selecciona una acción aleatoria
    accion = random.randint(1, 10)
    
    if accion <= 3:  # 30% de probabilidad: movimiento + click
        mover_mouse_aleatorio(ventana)
        pyautogui.click(button=random.choice(['left', 'right']))
        time.sleep(random.uniform(0.2, 0.5))
        
    elif accion <= 6:  # 30%: escritura
        mover_mouse_aleatorio(ventana)
        escribir_texto_aleatorio()
        
    elif accion <= 8:  # 20%: navegación con teclado
        navegacion_basica()
        
    else:  # 10%: cambio de aplicación
        cambio_aplicacion()
    
    return contador_verificacion + 1

def verificar_emergencia():
    """
    Detiene el script inmediatamente si el mouse entra en la zona segura
    (esquina superior izquierda de la pantalla)
    """
    x, y = pyautogui.position()
    if x < ZONA_SEGURA_X and y < ZONA_SEGURA_Y:
        print("\n🛑 EMERGENCIA: Ejecución detenida por movimiento a zona segura")
        sys.exit()

# ================= EJECUCIÓN PRINCIPAL =================
if __name__ == "__main__":
    # Confirmación de seguridad y advertencias
    print(f"""
    ⚠️ DEMOSTRACIÓN ÉTICA - SIMULADOR DE ACTIVIDAD EN VM ⚠️
    Configuración:
      - VM: '{VM_WINDOW_TITLE}'
      - Duración: {DURACION_MINUTOS} minutos
      - Zona de emergencia: Esquina superior izquierda ({ZONA_SEGURA_X}x{ZONA_SEGURA_Y})
    
    Instrucciones:
      1. Asegúrate de que la ventana de la VM está abierta y visible
      2. Para detener manualmente: Lleva el mouse a la esquina superior izquierda
      3. El sistema restaurará la posición original del mouse al finalizar
    
    Iniciando en 5 segundos...""")
    time.sleep(5)
    
    # Localizar y activar la ventana de la VM
    ventana_vm = encontrar_ventana_vm()
    print(f"✅ Ventana de VM encontrada: {ventana_vm.title}")
    activar_ventana(ventana_vm)
    
    # Guardar posición original del mouse
    start_x, start_y = pyautogui.position()
    
    try:
        tiempo_inicio = time.time()
        contador_acciones = 0
        print("\n🚀 Simulación iniciada...")
        
        # Bucle principal de ejecución
        while (time.time() - tiempo_inicio) < (DURACION_MINUTOS * 60):
            verificar_emergencia()
            contador_acciones = interaccion_compleja(ventana_vm, contador_acciones)
            
            # Pausa variable entre acciones
            pausa = random.uniform(INTERVALO_MIN, INTERVALO_MAX)
            print(f"Acción #{contador_acciones} completada. Próxima en {pausa:.1f}s")
            time.sleep(pausa)
            
    except KeyboardInterrupt:
        print("\n⏹️ Detenido por el usuario")
    finally:
        # Restaurar estado original
        pyautogui.moveTo(start_x, start_y, duration=0.5)
        print(f"✅ Simulación finalizada. Realizadas {contador_acciones} acciones.")