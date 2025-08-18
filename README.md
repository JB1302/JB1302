# Simulador de Actividad Artificial en VM - Demostración Ética

## 📋 Descripción

Este proyecto forma parte de una tesis académica que demuestra cómo los empleados pueden utilizar scripts de Python para crear actividad artificial en máquinas virtuales (VMs). El propósito es **exclusivamente educativo y ético**, para mostrar a las empresas los riesgos potenciales y cómo implementar medidas de detección.

## ⚠️ Advertencia Legal y Ética

- **SOLO PARA FINES EDUCATIVOS**: Este software está diseñado únicamente para investigación académica
- **NO USAR EN PRODUCCIÓN**: No debe utilizarse en entornos de trabajo reales
- **RESPONSABILIDAD**: El usuario es responsable del uso ético y legal de este software
- **CONSENTIMIENTO**: Solo usar en sistemas propios o con autorización explícita

## 🚀 Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Una máquina virtual ejecutándose (VMware, VirtualBox, etc.)

### Instalación de Dependencias

```bash
# Instalar las dependencias necesarias
pip install -r requirements.txt
```

### Dependencias Instaladas
- `pyautogui`: Para control de mouse y teclado
- `pygetwindow`: Para gestión de ventanas

## 🔧 Configuración

### Opción 1: Configuración Automática (Recomendada)

```bash
# Ejecutar el configurador interactivo
python configuracion_vm.py
```

El configurador te ayudará a:
- Listar todas las ventanas disponibles
- Identificar ventanas que podrían ser VMs
- Configurar el título exacto de tu VM
- Establecer duración e intervalos

### Opción 2: Configuración Manual

Edita directamente las variables en `simulador_actividad_vm.py`:

```python
VM_WINDOW_TITLE = "Nombre de tu VM aquí"  # Ej: "Ubuntu - VMware"
DURACION_MINUTOS = 5                      # Duración total
ZONA_SEGURA_X = 50                        # Zona de emergencia X
ZONA_SEGURA_Y = 50                        # Zona de emergencia Y
INTERVALO_MIN = 5                         # Mínimo segundos entre acciones
INTERVALO_MAX = 15                        # Máximo segundos entre acciones
```

## 🎯 Uso

### Preparación
1. **Asegúrate de que tu VM esté ejecutándose** y visible en pantalla
2. **Configura el título de la ventana** de la VM correctamente
3. **Ten una aplicación abierta** en la VM donde se pueda escribir (notepad, terminal, etc.)

### Ejecución

```bash
# Ejecutar el simulador
python simulador_actividad_vm.py
```

### Mecanismos de Seguridad

#### 🛑 Zona de Emergencia
- **Ubicación**: Esquina superior izquierda de la pantalla (50x50 píxeles)
- **Función**: Mover el mouse a esta zona detiene inmediatamente la ejecución
- **Uso**: En caso de emergencia, mueve rápidamente el mouse a la esquina superior izquierda

#### ⏹️ Detención Manual
- **Ctrl+C**: Detiene la ejecución de forma segura
- **Restauración**: El mouse regresa automáticamente a su posición original

#### ⏰ Límite de Tiempo
- **Configurable**: Duración máxima predefinida (default: 5 minutos)
- **Seguridad**: El script se detiene automáticamente al alcanzar el límite

## 🔍 Funcionalidades del Simulador

### Actividades Simuladas

1. **Movimientos de Mouse Realistas**
   - Posiciones aleatorias dentro de la VM
   - Velocidades variables (0.3-0.7 segundos)
   - Clics izquierdos y derechos

2. **Escritura Humana**
   - Palabras comunes de oficina
   - Errores tipográficos ocasionales (20% probabilidad)
   - Velocidad variable entre teclas (0.05-0.2 segundos)

3. **Navegación por Teclado**
   - Tabulador, Enter, flechas
   - Escape, espacio
   - Cambio entre aplicaciones (Alt+Tab)

4. **Intervalos Variables**
   - Pausas aleatorias entre acciones (5-15 segundos)
   - Simula comportamiento humano real

### Distribución de Acciones
- **30%**: Movimiento + clic de mouse
- **30%**: Escritura de texto
- **20%**: Navegación por teclado
- **10%**: Cambio de aplicación
- **10%**: Otras acciones

## 📊 Monitoreo y Logs

El script proporciona información en tiempo real:
- Número de acción actual
- Tiempo hasta la próxima acción
- Estado de la ventana de VM
- Alertas de seguridad

## 🛡️ Medidas de Detección Sugeridas

Para las empresas que quieran detectar este tipo de actividad:

### 1. Análisis de Patrones
- **Movimientos de mouse**: Detectar patrones demasiado regulares
- **Intervalos de tiempo**: Identificar pausas muy consistentes
- **Secuencias de teclas**: Detectar repeticiones exactas

### 2. Monitoreo de Actividad
- **Horarios**: Actividad fuera de horarios normales
- **Frecuencia**: Actividad constante sin pausas naturales
- **Aplicaciones**: Uso simultáneo de múltiples aplicaciones

### 3. Herramientas de Detección
- **Software de monitoreo**: Time tracking con análisis de patrones
- **Análisis de comportamiento**: Machine learning para detectar anomalías
- **Auditoría de logs**: Revisión de eventos del sistema

## 📁 Estructura del Proyecto

```
├── simulador_actividad_vm.py    # Script principal
├── configuracion_vm.py          # Configurador interactivo
├── requirements.txt             # Dependencias
├── README.md                    # Este archivo
└── config_vm.py                 # Configuración generada (se crea automáticamente)
```

## 🔧 Solución de Problemas

### Error: "No se encontró la ventana"
- Verifica que la VM esté ejecutándose y visible
- Usa `configuracion_vm.py` para listar ventanas disponibles
- Asegúrate de que el título coincida exactamente

### Error: "pyautogui no está instalado"
```bash
pip install pyautogui pygetwindow
```

### El script no responde a la zona de emergencia
- Verifica que las coordenadas de la zona segura sean correctas
- Asegúrate de que el mouse esté realmente en la esquina superior izquierda
- Usa Ctrl+C como alternativa

### La VM pierde el foco constantemente
- El script detecta automáticamente cuando la VM pierde el foco
- Re-activa la ventana automáticamente
- Considera reducir la frecuencia de acciones

## 📚 Referencias Académicas

Este proyecto puede ser útil para investigaciones sobre:
- Seguridad informática en entornos corporativos
- Detección de actividad artificial
- Automatización y sus implicaciones éticas
- Herramientas de monitoreo de empleados

## 🤝 Contribuciones

Para contribuciones académicas:
1. Mantén el enfoque educativo
2. Documenta claramente el propósito
3. Incluye advertencias de seguridad
4. Respeta las consideraciones éticas

## 📄 Licencia

Este software está destinado únicamente para fines educativos y de investigación. El uso comercial o malicioso está estrictamente prohibido.

---

**⚠️ Recordatorio**: Este software es para demostración educativa únicamente. Úsalo responsablemente y solo en sistemas propios o con autorización explícita.

