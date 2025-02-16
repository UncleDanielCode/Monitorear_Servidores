import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_REMITENTE, EMAIL_ADMIN, EMAIL_ANALISTA, EMAIL_CONTRASENA, SMTP_SERVER, SMTP_PORT

def enviar_correo(destinatario, asunto, mensaje):
    """
    Envía un correo de notificación a un destinatario específico.
    """
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_REMITENTE
        msg["To"] = destinatario
        msg["Subject"] = asunto
        msg.attach(MIMEText(mensaje, "html"))

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as servidor_smtp:
            servidor_smtp.login(EMAIL_REMITENTE, EMAIL_CONTRASENA)
            servidor_smtp.sendmail(EMAIL_REMITENTE, destinatario, msg.as_string())

        print(f"📧 Notificación enviada a {destinatario}: {asunto}")
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")

def notificar_error(servidor, nivel, detalle):
    """
    Envía una notificación detallada según el tipo de error.
    """
    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    colores = {
        "critico": "#d9534f",  # Rojo
        "advertencia": "#f0ad4e",  # Amarillo
        "ok": "#5cb85c"  # Verde
    }

    iconos = {
        "critico": "🚨",
        "advertencia": "⚠️",
        "ok": "✅"
    }

    titulos = {
        "critico": "ERROR CRÍTICO",
        "advertencia": "ADVERTENCIA",
        "ok": "SERVIDOR ESTABLE"
    }

    destinatario = EMAIL_ADMIN if nivel == "critico" else EMAIL_ANALISTA
    rol = "Administrador del Sistema" if nivel == "critico" else "Analista de Servidores"
    asunto = f"{iconos[nivel]} {titulos[nivel]} en {servidor}"

    mensaje = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                background-color: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0px 0px 10px #cccccc;
                max-width: 600px;
                margin: auto;
            }}
            h2 {{
                color: {colores[nivel]};
                text-align: left;
                border-bottom: 2px solid {colores[nivel]};
                padding-bottom: 5px;
            }}
            p {{
                font-size: 14px;
                color: #333;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #777;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>{iconos[nivel]} {titulos[nivel]}</h2>
            <p><strong>📅 Fecha y Hora:</strong> {fecha_hora_actual}</p>
            <p><strong>Servidor:</strong> {servidor}</p>
            <p><strong>Estado:</strong> {titulos[nivel]}</p>
            <p><strong>Detalles del problema:</strong> {detalle}</p>
            <p><strong>Destinatario:</strong> {rol} ({destinatario})</p>
            <hr>
            <p class="footer">Este mensaje es generado automáticamente por el sistema de monitoreo de servidores.</p>
        </div>
    </body>
    </html>
    """

    enviar_correo(destinatario, asunto, mensaje)
