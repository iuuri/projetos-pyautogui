import pyautogui

#Print da tela inteira
pyautogui.screenshot('Tela.jpg')

#print parte da tela utilizando o mouseinfo
#sequencia dos paramentros de regiao = pos_esquerda, pos_direito, pos_baixo
pyautogui.screenshot('calculadora.jpg', region=(723,106,500,907))
