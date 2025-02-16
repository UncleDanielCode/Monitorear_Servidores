# Lista de servidores a monitorear
SERVIDORES = [
    "8.8.8.8",  # Google DNS
    "1.1.1.1",  # Cloudflare DNS
    "208.67.222.222",  # OpenDNS (Cisco)
    "8.26.56.26",  # Comodo Secure DNS
    "9.9.9.9",  # IBM Quad9
    "64.6.64.6",  # Verisign Public DNS
    "76.76.19.19",  # Control D DNS
    "4.2.2.2",  # Level 3 Communications
    "205.171.3.25",  # CenturyLink Public DNS
    "tuservidorfalso.com"  # 🔴 Servidor de prueba con error
]   

# Configuración de correos para alertas diferenciadas
EMAIL_ADMIN = "dolopez@itla.edu.do"  # Recibe alertas críticas (🔴 Rojo)
EMAIL_ANALISTA = "dlopez10@est.unibe.edu.do"  # Recibe alertas leves (🟡 Amarillo)

# Credenciales de correo
EMAIL_REMITENTE = "daniel23.dl15@gmail.com"
EMAIL_CONTRASENA = "qfny ditw iohd acmn"

# Configuración del servidor SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Intervalos de monitoreo en segundos
TIEMPO_ESPERA_OK = 60  # 🟢 Servidores OK → Ping cada 1 min
TIEMPO_ESPERA_ADVERTENCIA = 120  # 🟡 Advertencia → Ping cada 2 min
TIEMPO_ESPERA_CRITICO = 120  # 🔴 Error crítico → Ping cada 2 min

# Tiempo mínimo entre notificaciones de un mismo problema (en segundos)
TIEMPO_NOTIFICACION = 600  # 10 min