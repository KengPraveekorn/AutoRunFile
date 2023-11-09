import os
import schedule
import time as tm
# from datetime import time, timedelta, datetime
# import messagebox as msg

## ---------------------------------------------------------------------------------------------------------------------------

# def sound1_ARM():
#     respone = os.startfile(r"I:\Media\08 Department\MT900\VDO Training\เสียงใหม่\พี่อาร์ม\VDO OK\ประชาสัมพันธ์อาร์ม.mp3")
#     print("ประชาสัมพันธ์อาร์ม --> ",respone)
    
# def sound2_ARM():
#     respone = os.startfile(r"I:\Media\08 Department\MT900\VDO Training\เสียงใหม่\พี่อาร์ม\VDO OK\พี่อาร์มแรปเปอร์.mp3")
#     print("พี่อาร์มแรปเปอร์ --> ",respone)

## ---------------------------------------------------------------------------------------------------------------------------

# def sound1_Peach():
#     respone = os.startfile(r"I:\Media\08 Department\MT900\VDO Training\เสียงใหม่\พีช\VDO OK\เสียงประชาสัมพันธ์พีชจี่.mp3")
#     print("เสียงประชาสัมพันธ์พีชจี่ --> ",respone)
    
# def sound2_Peach():
#     respone = os.startfile(r"I:\Media\08 Department\MT900\VDO Training\เสียงใหม่\พีช\VDO OK\พีชจี่แรปเปอร์.mp3")
#     print("พีชจี่แรปเปอร์ --> ",respone)
## ---------------------------------------------------------------------------------------------------------------------------

# def sound1_Muew():
#     respone = os.startfile(r"I:\Media\08 Department\MT900\VDO Training\เสียงใหม่\พี่หมิว\VDO OK\เสียงประชาสัมพันธ์พี่หมิว2.mp3")
#     print("เสียงประชาสัมพันธ์พี่หมิว2 --> ",respone)
    
# def sound2_Muew():
#     respone = os.startfile(r"I:\Media\08 Department\MT900\VDO Training\เสียงใหม่\พี่หมิว\VDO OK\พี่หมิวแรปเปอร์.mp3")
#     print("พี่หมิวแรปเปอร์ --> ",respone)
## ---------------------------------------------------------------------------------------------------------------------------

def sound3_Safety():
    respone = os.startfile(r"F:\MT900\900 Public\03 Safety\022 Training\คลิปเสียงโปรโมทการหาจุดเสี่ยง1.mp3")
    print("Safety --> ",respone)
## ---------------------------------------------------------------------------------------------------------------------------


# schedule.every().monday.at("07:02").do(sound1_ARM)
# schedule.every().monday.at("12:17").do(sound2_ARM)

# schedule.every().tuesday.at("07:02").do(sound1_Peach)
# schedule.every().tuesday.at("12:17").do(sound2_Peach)

# schedule.every().wednesday.at("07:02").do(sound1_Muew)
# schedule.every().wednesday.at("12:17").do(sound2_Muew)

# schedule.every().thursday.at("07:02").do(sound1_ARM)
# schedule.every().thursday.at("12:17").do(sound2_ARM)

# schedule.every().friday.at("07:02").do(sound1_Peach)
# schedule.every().friday.at("12:17").do(sound2_Peach)

# Safety sound-----------------------------------------------------
schedule.every().monday.at("09:18").do(sound3_Safety)
schedule.every().monday.at("14:08").do(sound3_Safety)
schedule.every().tuesday.at("09:18").do(sound3_Safety)
schedule.every().tuesday.at("14:08").do(sound3_Safety)
schedule.every().wednesday.at("09:18").do(sound3_Safety)
schedule.every().wednesday.at("14:08").do(sound3_Safety)
schedule.every().thursday.at("09:18").do(sound3_Safety)
schedule.every().thursday.at("14:08").do(sound3_Safety)
schedule.every().friday.at("09:18").do(sound3_Safety)
schedule.every().friday.at("14:08").do(sound3_Safety)

while True:
    schedule.run_pending()
    tm.sleep(1)
    
    