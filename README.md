
### 📌 **README.md - Monitoreo de Servidores con Semáforo**
```markdown
# 🚦 Monitoreo de Servidores con Semáforo

Este proyecto es una **extensión** del sistema de monitoreo de servidores en tiempo real. Se ha implementado un **sistema de semáforo** para categorizar los estados de los servidores y notificar de manera eficiente a los administradores y analistas de sistemas.

## 📌 Características Principales
✔️ **Monitoreo en tiempo real** de servidores mediante `ping`.  
✔️ **Clasificación por estados de semáforo**:
   - 🟢 **Servidor en línea (OK)**
   - 🟡 **Latencia alta (Advertencia)**
   - 🔴 **Servidor caído (Error Crítico)**  
✔️ **Notificaciones automáticas** por correo electrónico según la severidad.  
✔️ **Optimización en el envío de alertas** para evitar spam.  
✔️ **Historial de monitoreo en la consola** para seguimiento continuo.

## 🔧 Instalación y Configuración
### 1️⃣ Clonar el Repositorio
```sh
git clone -b semaforo https://github.com/tu-usuario/Monitorear_Servidores.git
cd Monitorear_Servidores
```
### 2️⃣ Instalar Dependencias
```sh
pip install -r requirements.txt
```

### 3️⃣ Configurar Variables de Entorno  
Edita el archivo `config.py` con tu información:
```python
EMAIL_ADMIN = "admin@example.com"  # Correo para alertas críticas
EMAIL_ANALISTA = "analista@example.com"  # Correo para alertas leves

SERVIDORES = [
    "8.8.8.8",  # Google DNS
    "1.1.1.1",  # Cloudflare DNS
    "tuservidorfalso.com"  # 🔴 Servidor con fallo intencional para pruebas
]

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_REMITENTE = "tucorreo@gmail.com"
EMAIL_CONTRASENA = "tu_contraseña_de_aplicacion"
```
📌 **Recuerda usar una contraseña de aplicación para Gmail.**

### 4️⃣ Ejecutar el Monitoreo
```sh
python monitor.py
```

## 📊 Funcionamiento del Semáforo
| Estado  | Descripción | Acción |
|---------|------------|--------|
| 🟢 **OK** | Servidor en línea | No se envía alerta |
| 🟡 **Advertencia** | Latencia alta (>200ms) | Notificación al analista |
| 🔴 **Error Crítico** | No responde al `ping` | Notificación al administrador |

📌 **Optimización del sistema:**  
✔️ Se evita enviar múltiples correos en un corto periodo de tiempo.  
✔️ Un error crítico solo se notifica cada **30 minutos** si persiste.  
✔️ Los servidores con latencia se verifican **cada 2 minutos**.  
✔️ Se sigue monitoreando en consola sin spam de notificaciones.  

## 📩 Notificaciones por Correo
Los correos se envían con un formato profesional y detallado, como este:

> **🔴 ERROR CRÍTICO**  
> - 📅 Fecha y Hora: `YYYY-MM-DD HH:MM:SS`  
> - 🌍 Servidor: `205.171.3.25`  
> - ⚠️ Estado: **No responde**  
> - 📌 Detalle: No se puede acceder al servidor. Puede estar fuera de línea o sin conectividad.  
> - 📧 Destinatario: Administrador del Sistema  

## 🔄 Próximos Mejoras
- 📜 **Registro de logs** de estados de servidores.
- 📊 **Interfaz web para visualizar en tiempo real**.
- 📱 **Notificaciones SMS** como alternativa al correo.

## 🛠 Tecnologías Utilizadas
- **Python 3.x**
- `pythonping` para hacer `ping` a los servidores.
- `smtplib` para el envío de correos.
- `email.mime` para formateo de correos en HTML.

## 🤝 Contribuciones
Si deseas mejorar el código, haz un `fork` y envía un `pull request`.  

```sh
git checkout -b nueva_mejora
git commit -m "Añadí X funcionalidad"
git push origin nueva_mejora
```

📧 Para dudas, contacta al equipo de desarrollo.

---
🚀 **Proyecto en desarrollo - Versión Beta 🚦**
```

---

## 📌 **¿Qué sigue ahora?**
✅ **Añade este archivo como `README.md` en la rama `semaforo`**  
```sh
git add README.md
git commit -m "Añadido README con detalles del semáforo"
git push origin semaforo
```
📌 Luego ve a GitHub y verifica que el archivo se haya subido correctamente.

