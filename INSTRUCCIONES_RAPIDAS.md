# 🚀 Instrucciones Rápidas - Simulador de Actividad en VM

## ⚡ Inicio Rápido (5 minutos)

### 1. Instalación
```bash
# Instalar dependencias
pip install -r requirements.txt
```

### 2. Verificación
```bash
# Probar que todo funciona
python3 test_dependencias.py
```

### 3. Demostración (Sin VM)
```bash
# Ver cómo funciona sin necesidad de VM
python3 demo_simulador.py
```

### 4. Configuración (Con VM)
```bash
# Configurar para tu VM específica
python3 configuracion_vm.py
```

### 5. Ejecución
```bash
# Ejecutar el simulador
python3 simulador_actividad_vm.py
```

## 🎯 Para Presentaciones

### Demostración Educativa
```bash
# Ejecutar demo de 30 segundos
python3 demo_simulador.py
```

### Configuración Rápida
```bash
# Listar ventanas disponibles
python3 configuracion_vm.py
```

## 🛡️ Mecanismos de Seguridad

### Detener Emergencia
- **Mover mouse** a esquina superior izquierda (50x50 píxeles)
- **Ctrl+C** en terminal
- **Tiempo límite** automático (5 minutos por defecto)

### Restauración
- El mouse regresa automáticamente a su posición original
- No se guardan datos sensibles
- No se modifican archivos del sistema

## 📋 Checklist de Uso

### Antes de Usar
- [ ] VM ejecutándose y visible
- [ ] Aplicación abierta en VM (notepad, terminal, etc.)
- [ ] Dependencias instaladas
- [ ] Configuración completada

### Durante la Ejecución
- [ ] Monitorear la consola para logs
- [ ] Tener acceso a zona de emergencia
- [ ] Observar comportamiento en VM
- [ ] Documentar observaciones

### Después de Usar
- [ ] Verificar restauración del mouse
- [ ] Revisar logs de actividad
- [ ] Documentar hallazgos
- [ ] Analizar patrones detectados

## 🔧 Configuración Avanzada

### Variables Principales
```python
VM_WINDOW_TITLE = "Nombre de tu VM aquí"
DURACION_MINUTOS = 5
INTERVALO_MIN = 5
INTERVALO_MAX = 15
ZONA_SEGURA_X = 50
ZONA_SEGURA_Y = 50
```

### Personalización
- **Duración**: Cambiar `DURACION_MINUTOS`
- **Frecuencia**: Ajustar `INTERVALO_MIN` y `INTERVALO_MAX`
- **Zona segura**: Modificar `ZONA_SEGURA_X` y `ZONA_SEGURA_Y`
- **Palabras**: Editar lista en `escribir_texto_aleatorio()`

## 📊 Análisis de Resultados

### Métricas a Observar
- **Acciones por minuto**: Normal 10-15
- **Distribución de tipos**: 30% mouse, 30% escritura, 20% teclado, 10% apps
- **Intervalos**: Deben ser variables (5-15 segundos)
- **Errores tipográficos**: 20% de probabilidad

### Patrones de Detección
- **Movimientos regulares**: Sospechoso
- **Intervalos exactos**: Artificial
- **Sin errores**: Probable automatización
- **Actividad constante**: No natural

## 🎓 Para la Tesis

### Puntos Clave a Destacar
1. **Propósito educativo**: Solo para investigación
2. **Mecanismos de seguridad**: Múltiples capas
3. **Detección de patrones**: Herramientas para empresas
4. **Consideraciones éticas**: Uso responsable

### Métricas de Evaluación
- Efectividad de la simulación
- Capacidad de detección
- Impacto en sistemas de monitoreo
- Tiempo de identificación

## 🔍 Solución de Problemas

### Error: "No se encontró la ventana"
```bash
# Listar ventanas disponibles
python3 configuracion_vm.py
```

### Error: "pyautogui no está instalado"
```bash
# Reinstalar dependencias
pip install pyautogui pygetwindow
```

### Error: "Permission denied"
```bash
# En Linux, instalar tkinter
sudo apt-get install python3-tk
```

### La VM pierde el foco
- El script lo detecta automáticamente
- Re-activa la ventana
- Considera reducir frecuencia

## 📞 Soporte

### Archivos de Ayuda
- `README.md`: Documentación completa
- `DOCUMENTACION_TESIS.md`: Contexto académico
- `test_dependencias.py`: Diagnóstico de problemas

### Comandos Útiles
```bash
# Verificar sintaxis
python3 -m py_compile simulador_actividad_vm.py

# Ver versión de Python
python3 --version

# Listar paquetes instalados
pip list | grep pyautogui
```

---

**⚠️ Recordatorio**: Este software es para fines educativos únicamente. Úsalo responsablemente.