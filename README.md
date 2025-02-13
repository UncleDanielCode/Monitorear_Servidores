🖥️ Monitoreo de Servidores en Tiempo Real
📌 Descripción
Este proyecto es un **Sistema de Monitoreo de Servidores en Tiempo Real** desarrollado en **Python**. Su objetivo es supervisar la disponibilidad de servidores mediante pings automáticos y enviar **notificaciones por correo electrónico** cuando un servidor deja de responder. 

🚀 Características principales
- ✅ Monitoreo automático de múltiples servidores.
- ✅ Notificaciones por correo cuando un servidor cae.
- ✅ Espera inteligente de 30 minutos** antes de volver a notificar sobre un servidor caído (evita spam).
- ✅ Soporte para múltiples servidores simultáneamente.
- ✅ Código modular y fácil de extender.

⚙️ Tecnologías utilizadas
Python 3.11+
pythonping (para realizar pings)
smtplib y email (para envíos de correo SMTP)
Estructura de archivos organizada y modular.

📜 Cómo usar
1. Clona el repositorio  
   ```bash
   git clone https://github.com/UncleDanielCode/Monitorear_Servidores.git
   cd monitoreo-servidores
   ```
2. Instala las dependencias necesarias  
   ```bash
   pip install pythonping
   ```
3. Configura los servidores y el correo en `config.py`
4. Ejecuta el monitor  
   ```bash
   python monitor.py
   ```

📧 Ejemplo de Notificación
Cuando un servidor falla, recibirás un correo con este formato:
```
🚨 Alerta Crítica: Problema de Conectividad en servidor.com
📅 Fecha y Hora: 2025-02-12 15:30:45
Detalles: El servidor ha dejado de responder y requiere atención inmediata.
```

🌟 Contribuciones
¡Cualquier mejora o sugerencia es bienvenida! Puedes abrir un **issue** o enviar un **pull request**.

📝 Licencia
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo, modificarlo y distribuirlo libremente. 🚀
