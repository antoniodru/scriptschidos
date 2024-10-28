import ctypes
import pyautogui
import time

# Definir las constantes de SetThreadExecutionState
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

# Función para evitar que Windows entre en modo de suspensión o bloquee la pantalla
def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

# Función para simular la actividad del ratón con movimiento agresivo
def move_mouse_aggressively_and_click():
    # Mover el ratón en diferentes direcciones
    pyautogui.moveRel(100, 0, duration=0.2)  # Mueve 100 píxeles a la derecha
    pyautogui.click()  # Simula un clic
    time.sleep(0.5)  # Pausa breve para que el clic no se haga instantáneo

    pyautogui.moveRel(-100, 0, duration=0.2)  # Mueve 100 píxeles a la izquierda
    pyautogui.click()  # Simula otro clic
    time.sleep(0.5)  # Pausa

    pyautogui.moveRel(0, 100, duration=0.2)  # Mueve 100 píxeles hacia abajo
    pyautogui.click()  # Clic de nuevo
    time.sleep(0.5)  # Pausa

    pyautogui.moveRel(0, -100, duration=0.2)  # Mueve 100 píxeles hacia arriba
    pyautogui.click()  # Clic final
    time.sleep(0.5)  # Pausa

if __name__ == "__main__":
    try:
        while True:
            prevent_sleep()  # Evita que Windows entre en suspensión
            move_mouse_aggressively_and_click()  # Mueve el ratón y simula clics
            time.sleep(10)  # Espera 60 segundos antes de repetir el ciclo
    except KeyboardInterrupt:
        # Permitir la suspensión y el bloqueo cuando el script termine
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        print("Script detenido, Windows puede bloquearse nuevamente.")
