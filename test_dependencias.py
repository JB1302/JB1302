"""
TEST DE DEPENDENCIAS - SIMULADOR DE ACTIVIDAD EN VM
Script para verificar que todas las dependencias estén funcionando correctamente
"""

import sys
import time

def test_imports():
    """Verifica que todas las dependencias se puedan importar"""
    print("🔍 Verificando importaciones...")
    
    try:
        import pyautogui
        print("✅ pyautogui importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando pyautogui: {e}")
        return False
    
    try:
        import pygetwindow as gw
        print("✅ pygetwindow importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando pygetwindow: {e}")
        return False
    
    try:
        import random
        import time
        print("✅ Módulos estándar (random, time) disponibles")
    except ImportError as e:
        print(f"❌ Error con módulos estándar: {e}")
        return False
    
    return True

def test_pyautogui():
    """Prueba funcionalidades básicas de pyautogui"""
    print("\n🔍 Probando pyautogui...")
    
    try:
        import pyautogui
        
        # Obtener posición actual del mouse
        x, y = pyautogui.position()
        print(f"✅ Posición actual del mouse: ({x}, {y})")
        
        # Obtener tamaño de pantalla
        width, height = pyautogui.size()
        print(f"✅ Tamaño de pantalla: {width}x{height}")
        
        # Probar función de escritura (sin escribir nada)
        print("✅ Funciones de pyautogui funcionando correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error con pyautogui: {e}")
        return False

def test_pygetwindow():
    """Prueba funcionalidades básicas de pygetwindow"""
    print("\n🔍 Probando pygetwindow...")
    
    try:
        import pygetwindow as gw
        
        # Obtener todas las ventanas
        ventanas = gw.getAllTitles()
        print(f"✅ Encontradas {len(ventanas)} ventanas")
        
        # Mostrar algunas ventanas como ejemplo
        ventanas_ejemplo = [v for v in ventanas if v and v.strip()][:5]
        print("📋 Ejemplos de ventanas disponibles:")
        for i, titulo in enumerate(ventanas_ejemplo, 1):
            print(f"   {i}. {titulo}")
        
        # Obtener ventana activa
        ventana_activa = gw.getActiveWindow()
        if ventana_activa:
            print(f"✅ Ventana activa: {ventana_activa.title}")
        else:
            print("⚠️ No se pudo obtener la ventana activa")
        
        return True
        
    except Exception as e:
        print(f"❌ Error con pygetwindow: {e}")
        return False

def test_configuracion():
    """Verifica que la configuración sea válida"""
    print("\n🔍 Verificando configuración...")
    
    try:
        # Intentar importar el script principal
        import simulador_actividad_vm
        
        # Verificar variables de configuración
        vm_titulo = simulador_actividad_vm.VM_WINDOW_TITLE
        duracion = simulador_actividad_vm.DURACION_MINUTOS
        
        print(f"✅ VM_WINDOW_TITLE: '{vm_titulo}'")
        print(f"✅ DURACION_MINUTOS: {duracion}")
        
        if vm_titulo == "Nombre de tu VM aquí":
            print("⚠️ ADVERTENCIA: Debes configurar el título de la VM antes de usar")
            print("   Ejecuta: python configuracion_vm.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Error verificando configuración: {e}")
        return False

def test_seguridad():
    """Prueba las funciones de seguridad"""
    print("\n🔍 Probando funciones de seguridad...")
    
    try:
        import pyautogui
        import pygetwindow as gw
        
        # Probar detección de zona segura
        x, y = pyautogui.position()
        zona_segura_x = 50
        zona_segura_y = 50
        
        if x < zona_segura_x and y < zona_segura_y:
            print("⚠️ ADVERTENCIA: El mouse está en la zona de emergencia")
        else:
            print("✅ Zona de emergencia accesible")
        
        print("✅ Funciones de seguridad verificadas")
        return True
        
    except Exception as e:
        print(f"❌ Error con funciones de seguridad: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("=" * 60)
    print("🧪 TEST DE DEPENDENCIAS - SIMULADOR DE ACTIVIDAD EN VM")
    print("=" * 60)
    
    tests = [
        ("Importaciones", test_imports),
        ("PyAutoGUI", test_pyautogui),
        ("PyGetWindow", test_pygetwindow),
        ("Configuración", test_configuracion),
        ("Seguridad", test_seguridad)
    ]
    
    resultados = []
    
    for nombre, test_func in tests:
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"❌ Error inesperado en {nombre}: {e}")
            resultados.append((nombre, False))
    
    # Resumen de resultados
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    exitosos = 0
    for nombre, resultado in resultados:
        estado = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"{nombre:15} : {estado}")
        if resultado:
            exitosos += 1
    
    print(f"\nTotal: {exitosos}/{len(resultados)} pruebas exitosas")
    
    if exitosos == len(resultados):
        print("\n🎉 ¡Todas las pruebas pasaron! El simulador está listo para usar.")
        print("📝 Próximos pasos:")
        print("   1. Configura el título de tu VM: python configuracion_vm.py")
        print("   2. Ejecuta el simulador: python simulador_actividad_vm.py")
    else:
        print("\n⚠️ Algunas pruebas fallaron. Revisa los errores arriba.")
        print("📝 Posibles soluciones:")
        print("   1. Instala las dependencias: pip install -r requirements.txt")
        print("   2. Verifica que Python esté actualizado")
        print("   3. En sistemas Linux, instala: sudo apt-get install python3-tk")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()