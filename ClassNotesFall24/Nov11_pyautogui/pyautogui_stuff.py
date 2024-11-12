import pyautogui

# Setup Documentation https://pyautogui.readthedocs.io/en/latest/install.html

# # Init Cursor Location
x, y = pyautogui.size()
print(x, y)
print(pyautogui.position())
pyautogui.moveTo(10, 10)

# # Trigger Spotlight Launch
# pyautogui.moveTo(1175, None)
# pyautogui.click()
# pyautogui.PAUSE = 3

# # Enter spotlight request & start applications
# pyautogui.write('https://letmegooglethat.com', interval=0.5) 
# pyautogui.press('enter') 
# pyautogui.PAUSE = 3

# # Let me google that for you
# pyautogui.write('How can I automate my life with python?', interval=0.5) 
# pyautogui.press(‘enter')