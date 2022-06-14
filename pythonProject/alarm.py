import time
import webbrowser


hour = int(input("Hour : "))
minute = int(input("Minute : "))

while True:
    suankisaat = time.localtime(time.time())
    if minute == suankisaat.tm_min and hour ==suankisaat.tm_hour:
        webbrowser.open_new("https://www.youtube.com/watch?v=KwkND9oghlI")
        break
    else:
        pass



