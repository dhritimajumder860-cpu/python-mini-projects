import time 
from plyer import notification
while True:
    print("You should drink some water .")
    notification.notify(title="Drink water",message="You need to drink some water")
    time.sleep(60*60)