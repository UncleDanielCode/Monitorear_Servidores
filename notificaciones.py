import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_REMITENTE, EMAIL_DESTINATARIO, EMAIL_CONTRASENA, SMTP_SERVER, SMTP_PORT

def enviar_correo(servidor):
    """
    Envía un correo de alerta al administrador cuando un servidor no responde,
    incluyendo la fecha y hora exacta del evento.
    """
    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    asunto = f"🚨 Alerta Crítica: Problema de Conectividad en {servidor}"

    cuerpo = f"""
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
                background-color: #ffffff;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0px 0px 10px #cccccc;
                max-width: 600px;
                margin: auto;
            }}
            h2 {{
                color: #d9534f;
            }}
            p {{
                font-size: 14px;
                color: #333333;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #777777;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🚨 Alerta Crítica: Problema de Conectividad</h2>
            <p>Estimado Administrador,</p>
            <p>Se ha detectado un problema en el servidor <strong>{servidor}</strong>. Actualmente, el sistema de monitoreo no ha podido establecer comunicación con este servidor.</p>
            <p><strong>📅 Fecha y Hora:</strong> {fecha_hora_actual}</p>
            <p>Por favor, revise el estado del servidor lo antes posible para evitar posibles interrupciones en los servicios.</p>
            <p>Para más detalles, puede acceder al sistema de monitoreo en tiempo real.</p>
            <hr>
            <p class="footer">Este es un mensaje automático del sistema de monitoreo de servidores. No responda a este correo.</p>
        </div>
    </body>
    </html>
    """

    mensaje = MIMEMultipart()
    mensaje["From"] = EMAIL_REMITENTE
    mensaje["To"] = EMAIL_DESTINATARIO
    mensaje["Subject"] = asunto

    mensaje.attach(MIMEText(cuerpo, "html"))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as servidor_smtp:
            servidor_smtp.login(EMAIL_REMITENTE, EMAIL_CONTRASENA)
            servidor_smtp.sendmail(EMAIL_REMITENTE, EMAIL_DESTINATARIO, mensaje.as_string())

        print(f"📧 Alerta enviada a {EMAIL_DESTINATARIO} sobre {servidor} | Fecha y Hora: {fecha_hora_actual}")

    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
