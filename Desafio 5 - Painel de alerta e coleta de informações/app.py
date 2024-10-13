import pyautogui

email = pyautogui.prompt(text='Digite seu email', title='Informações obrigatorias')
senha = pyautogui.password(text='Digite sua senha', title='Informações obrigadorias', mask='*')

pyautogui.moveTo(1116,494, duration=1)
pyautogui.click(duration=1)
pyautogui.typewrite(email)
pyautogui.hotkey('Enter')
pyautogui.typewrite(senha)

resposta = pyautogui.confirm(text='As informações estão correta?', title='Confirmação', buttons=['Sim', 'Não'])

if resposta == 'Sim':
    print('Dados salvos com sucesso')
else:
    print('Execute o programa novamente e preencha os dados corretamente.')

