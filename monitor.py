import time
from pythonping import ping
from config import (
    SERVIDORES, 
    TIEMPO_ESPERA_OK, 
    TIEMPO_ESPERA_ADVERTENCIA, 
    TIEMPO_ESPERA_CRITICO, 
    TIEMPO_NOTIFICACION
)
from notificaciones import notificar_error

# Diccionario para almacenar el estado de cada servidor
estado_servidores = {servidor: {"estado": "🟢", "ultima_alerta": 0} for servidor in SERVIDORES}

def obtener_estado(servidor):
    """
    Realiza un ping y determina el estado del servidor.
    """
    try:
        respuesta = ping(servidor, count=2, timeout=2)
        latencia = respuesta.rtt_avg_ms

        if not respuesta.success():
            return "🔴", "critico", f"Fallo de conexión con {servidor}."
        elif latencia > 200:
            return "🟡", "advertencia", f"Alta latencia en {servidor}: {latencia}ms"
        else:
            return "🟢", "ok", f"{servidor} responde correctamente."

    except Exception:
        return "🔴", "critico", f"Error crítico en {servidor}."

def monitorear_servidores():
    """
    Ejecuta el monitoreo aplicando la lógica del semáforo.
    """
    print("🔍 Iniciando monitoreo de servidores...\n")

    while True:
        for servidor in SERVIDORES:
            estado_actual, nivel_error, detalle_error = obtener_estado(servidor)
            tiempo_actual = time.time()

            # Mostrar siempre el estado del servidor en consola
            print(f"{estado_actual} {servidor}: {detalle_error}")

            # Si cambia de estado o se cumple el tiempo de notificación, enviar alerta
            if estado_actual != estado_servidores[servidor]["estado"] or (tiempo_actual - estado_servidores[servidor]["ultima_alerta"] > TIEMPO_NOTIFICACION):
                notificar_error(servidor, nivel_error, detalle_error)
                estado_servidores[servidor]["estado"] = estado_actual
                estado_servidores[servidor]["ultima_alerta"] = tiempo_actual

        time.sleep(TIEMPO_ESPERA_OK)  # Ajustar el tiempo de espera

# Aseguramos que el script solo se ejecute si es el archivo principal
if __name__ == "__main__":
    try:
        monitorear_servidores()
    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido por el usuario.")
