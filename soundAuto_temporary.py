import os
import schedule
import time as tm

## ---------------------------------------------------------------------------------------------------------------------------

def sound_Ambassador():
    respone = os.startfile(r"I:\Media\08 Department\MT900\Sound Ambassador\MTL Ambassador_Final.mp3")
    print("Ambassador")

## ---------------------------------------------------------------------------------------------------------------------------

schedule.every().thursday.at("02:02").do(sound_Ambassador)
schedule.every().thursday.at("14:02").do(sound_Ambassador)

while True:
    schedule.run_pending()
    tm.sleep(1)