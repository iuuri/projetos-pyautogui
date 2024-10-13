import pyautogui

captcha = pyautogui.locateOnScreen('captcha.png')
pyautogui.click(captcha, duration=2)