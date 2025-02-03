import time
from datetime import datetime
while True:   
    now = datetime.now()
    print (now.strftime("%m/%d/%Y %H:%M:%S"), end="\r")