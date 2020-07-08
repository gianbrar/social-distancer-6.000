import os
import threading

def camfeed():
    os.system("python3 camfeed.py")
threading.Thread(target=camfeed).start()