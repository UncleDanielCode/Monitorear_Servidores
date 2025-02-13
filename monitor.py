import time
from pythonping import ping
from config import SERVIDORES
from notificaciones import enviar_correo

servidores_fallidos = {}

def hacer_ping(servidor):
    """
    Realiza un ping al servidor y devuelve True si responde, False si no.
    """
    try:
        respuesta = ping(servidor, count=2, timeout=2)
        return respuesta.success()
    except Exception as e:
        print(f"⚠️ Error al hacer ping a {servidor}: {e}")
        return False

def monitorear_servidores():
    """
    Monitorea los servidores y envía alertas por correo cuando un servidor cae,
    pero solo una vez por cada falla. Luego, espera 30 minutos antes de volver a intentarlo.
    """
    print("🔍 Iniciando monitoreo de servidores...\n")
    
    while True:
        for servidor in SERVIDORES:
            tiempo_actual = time.time()
            
            if servidor in servidores_fallidos:
                tiempo_ultima_alerta = servidores_fallidos[servidor]
                if tiempo_actual - tiempo_ultima_alerta < 1800:  
                    print(f"⏳ {servidor} sigue caído. Próxima verificación en {int(1800 - (tiempo_actual - tiempo_ultima_alerta))} segundos.")
                    continue

            if hacer_ping(servidor):
                print(f"✅ {servidor} responde correctamente.")
                if servidor in servidores_fallidos:
                    del servidores_fallidos[servidor]
            else:
                print(f"❌ ALERTA: {servidor} NO responde ⚠️")
                if servidor not in servidores_fallidos:
                    enviar_correo(servidor)
                servidores_fallidos[servidor] = tiempo_actual

        time.sleep(30)  

if __name__ == "__main__":
    monitorear_servidores()
