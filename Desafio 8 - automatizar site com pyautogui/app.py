import webbrowser
import pyautogui
from time import sleep



# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open("https://cursoautomacao.netlify.app/")
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.click(4598,356, duration=0.5)
pyautogui.scroll(-500)
pyautogui.click(5474,1158, duration=0.5)
pyautogui.typewrite("Iuri")
# 3) Clique em alerta, para gerar a alerta
pyautogui.click(5436,1220,duration=0.5)
# 4) Feche a alerta
pyautogui.click(5298,302, duration=0.5)
# 5) Suba a página totalmente para cima
pyautogui.scroll(500)
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
pyautogui.scroll(-2000)
pyautogui.click(4587,1184, duration=0.5)
sleep(1)
pyautogui.click(4884,1154, duration=0.5)

# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='VOCÊ TERMINOU', title='Informativo')

