import pyautogui as auto
import subprocess
import os


def buscar(texto):
    subprocess.call(
        ['google-chrome', 'www.google.com/search?q={0}'.format(texto)])


def cerrarVentana():
    auto.hotkey('alt', 'f4')

  
def scrollDown():
    auto.scroll(-10)
    # auto.press('j')


def scrollUp():
    auto.scroll(10)
    # auto.press('k')


def acercar():
    auto.hotkey('ctrl', '+')


def alejar():
    auto.hotkey('ctrl', '-')


def nuevo():
    auto.hotkey('ctrl', 'n')

def foto():
    auto.hotkey('ctrl', 'p')

def enter():
    auto.hotkey('enter')

def siguienteChat():
    auto.hotkey('ctrl', 'tab')

def buscarChat():
    auto.hotkey('ctrl', 'f')

def anteriorChat():
    auto.hotkey('ctrl', 'shift', 'tab')


def escribir(texto):
    texto = replace(texto)
    auto.typewrite(texto)


def minimizar():
    auto.hotkey('win', 'm')


def restaurar():
    auto.hotkey('win', 'shift', 'm')

def abrir():   
    os.system('WhatsApp.exe')

def abrir1():
    os.system('WhatsApp.exe')


def escape():
    auto.press('esc')

def borrar():
    auto.hotkey('ctrl', 'backspace')

def borrarTexto():
    auto.hotkey('backspace')

def borrarTodo():
    auto.hotkey('ctrl', 'a')    
    auto.hotkey('backspace')

def replace(texto):
    texto = texto.replace("á","a")
    texto = texto.replace("é","e")
    texto = texto.replace("í","i")
    texto = texto.replace("ó","o")
    texto = texto.replace("ú","u")
    return texto