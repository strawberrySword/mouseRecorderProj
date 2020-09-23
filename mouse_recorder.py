<<<<<<< HEAD
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        sys.stdout.flush()
except KeyboardInterrupt:
    print("end")
=======
import pyautogui
#to set the mouse location use 
pyautogui.moveTo(100, 100, duration = 1)
print('hnun') mmkmkm
>>>>>>> cb9bba5a6eb9141469719a3c42c092957145dcd7
