import pyautogui
import pyperclip

#função criada para digitar frases com pontuações especiais
def frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.moveTo(903,486, duration=1)
pyautogui.click()
frase('Automação é Incrivel!')
