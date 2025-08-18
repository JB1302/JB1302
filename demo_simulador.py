"""
DEMOSTRACIÓN DEL SIMULADOR DE ACTIVIDAD EN VM
Versión educativa que muestra la funcionalidad sin requerir una VM real

Este script demuestra cómo funciona el simulador sin ejecutar acciones reales,
útil para presentaciones y demostraciones educativas.
"""

import random
import time
import sys

# ================= CONFIGURACIÓN DE DEMOSTRACIÓN =================
DURACION_DEMO = 30                    # Duración en segundos para la demo
INTERVALO_MIN = 2                     # Mínimo segundos entre acciones
INTERVALO_MAX = 5                     # Máximo segundos entre acciones

# ================ FUNCIONES DE DEMOSTRACIÓN ================

def simular_movimiento_mouse():
    """Simula movimiento de mouse con coordenadas aleatorias"""
    x = random.randint(100, 800)
    y = random.randint(100, 600)
    duracion = random.uniform(0.3, 0.7)
    
    print(f"🖱️  Movimiento de mouse a ({x}, {y}) en {duracion:.1f}s")
    time.sleep(duracion)

def simular_click():
    """Simula clic de mouse"""
    boton = random.choice(['izquierdo', 'derecho'])
    print(f"🖱️  Clic {boton}")
    time.sleep(random.uniform(0.2, 0.5))

def simular_escritura():
    """Simula escritura de texto"""
    palabras = ["informe", "reunion", "analisis", "datos", "proyecto", 
                "tesis", "python", "script", "automatizacion", "empresa"]
    
    palabra = random.choice(palabras)
    
    # Simula errores humanos (20% de probabilidad)
    if random.random() > 0.8:
        palabra = palabra[:-1]  # Omite última letra
        print(f"⌨️  Escribiendo: '{palabra}' (con error tipográfico)")
    else:
        print(f"⌨️  Escribiendo: '{palabra}'")
    
    # Simula tiempo de escritura
    tiempo_escritura = len(palabra) * random.uniform(0.05, 0.2)
    time.sleep(tiempo_escritura)

def simular_navegacion():
    """Simula navegación por teclado"""
    teclas = ['TAB', 'ENTER', 'FLECHA ABAJO', 'FLECHA DERECHA', 'ESC', 'ESPACIO']
    tecla = random.choice(teclas)
    print(f"⌨️  Presionando: {tecla}")
    time.sleep(random.uniform(0.1, 0.3))

def simular_cambio_aplicacion():
    """Simula cambio entre aplicaciones"""
    print("🔄 Cambiando aplicación (Alt+Tab)")
    time.sleep(random.uniform(0.5, 1.5))

def simular_verificacion_ventana():
    """Simula verificación de que la VM sigue activa"""
    print("👁️  Verificando que la VM sigue activa...")
    time.sleep(0.5)

def accion_aleatoria(contador):
    """Ejecuta una acción aleatoria basada en las probabilidades del simulador real"""
    
    # Verificar cada 5 acciones si la VM sigue activa
    if contador % 5 == 0:
        simular_verificacion_ventana()
    
    # Selecciona una acción aleatoria con las mismas probabilidades del simulador real
    accion = random.randint(1, 10)
    
    if accion <= 3:  # 30% de probabilidad: movimiento + click
        simular_movimiento_mouse()
        simular_click()
        
    elif accion <= 6:  # 30%: escritura
        simular_movimiento_mouse()
        simular_escritura()
        
    elif accion <= 8:  # 20%: navegación con teclado
        simular_navegacion()
        
    else:  # 10%: cambio de aplicación
        simular_cambio_aplicacion()
    
    return contador + 1

def mostrar_estadisticas(contador, tiempo_transcurrido):
    """Muestra estadísticas de la simulación"""
    print(f"\n📊 ESTADÍSTICAS:")
    print(f"   • Acciones realizadas: {contador}")
    print(f"   • Tiempo transcurrido: {tiempo_transcurrido:.1f}s")
    print(f"   • Acciones por minuto: {(contador / tiempo_transcurrido) * 60:.1f}")

def mostrar_medidas_deteccion():
    """Muestra las medidas de detección que las empresas pueden implementar"""
    print(f"\n🛡️  MEDIDAS DE DETECCIÓN SUGERIDAS:")
    print(f"   1. Análisis de patrones de mouse:")
    print(f"      • Detectar movimientos demasiado regulares")
    print(f"      • Identificar velocidades constantes")
    print(f"      • Monitorear secuencias repetitivas")
    
    print(f"\n   2. Análisis de intervalos de tiempo:")
    print(f"      • Detectar pausas muy consistentes")
    print(f"      • Identificar patrones temporales")
    print(f"      • Monitorear horarios de actividad")
    
    print(f"\n   3. Análisis de comportamiento:")
    print(f"      • Detectar escritura sin errores humanos")
    print(f"      • Identificar navegación sistemática")
    print(f"      • Monitorear uso de aplicaciones")

# ================= EJECUCIÓN PRINCIPAL =================
if __name__ == "__main__":
    print("=" * 70)
    print("🎓 DEMOSTRACIÓN EDUCATIVA - SIMULADOR DE ACTIVIDAD EN VM")
    print("=" * 70)
    print("Este script demuestra cómo funciona el simulador sin ejecutar")
    print("acciones reales. Útil para presentaciones educativas.")
    print("=" * 70)
    
    print(f"\n⚙️  Configuración de la demostración:")
    print(f"   • Duración: {DURACION_DEMO} segundos")
    print(f"   • Intervalo entre acciones: {INTERVALO_MIN}-{INTERVALO_MAX} segundos")
    print(f"   • Distribución de acciones:")
    print(f"     - 30% Movimiento + clic de mouse")
    print(f"     - 30% Escritura de texto")
    print(f"     - 20% Navegación por teclado")
    print(f"     - 10% Cambio de aplicación")
    print(f"     - 10% Otras acciones")
    
    print(f"\n🚀 Iniciando demostración en 3 segundos...")
    for i in range(3, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
    
    print(f"\n🎬 DEMOSTRACIÓN INICIADA")
    print("=" * 50)
    
    tiempo_inicio = time.time()
    contador_acciones = 0
    
    try:
        # Bucle principal de demostración
        while (time.time() - tiempo_inicio) < DURACION_DEMO:
            contador_acciones = accion_aleatoria(contador_acciones)
            
            # Pausa variable entre acciones
            pausa = random.uniform(INTERVALO_MIN, INTERVALO_MAX)
            tiempo_restante = DURACION_DEMO - (time.time() - tiempo_inicio)
            
            print(f"✅ Acción #{contador_acciones} completada. Próxima en {pausa:.1f}s")
            print(f"⏰ Tiempo restante: {tiempo_restante:.1f}s")
            print("-" * 30)
            
            time.sleep(pausa)
            
    except KeyboardInterrupt:
        print("\n⏹️  Demostración detenida por el usuario")
    
    # Estadísticas finales
    tiempo_total = time.time() - tiempo_inicio
    mostrar_estadisticas(contador_acciones, tiempo_total)
    
    # Mostrar medidas de detección
    mostrar_medidas_deteccion()
    
    print(f"\n" + "=" * 70)
    print("🎓 DEMOSTRACIÓN COMPLETADA")
    print("=" * 70)
    print("Este simulador demuestra cómo los empleados podrían crear")
    print("actividad artificial en VMs. Las empresas deben implementar")
    print("medidas de detección para identificar este tipo de comportamiento.")
    print("=" * 70)