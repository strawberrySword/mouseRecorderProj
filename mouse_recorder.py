import pyautogui, sys
import mouse
import keyboard


events = []                   
keyboard.wait('escape')
events.append(pyautogui.position())

print(events)
