

#!/usr/bin/env python

import time
import bot
import alert_listener
import threading
import queue

threads = []

q = queue.Queue()

if __name__ == "__main__":
    sb_thread = threading.Thread(target=bot.start_slackbot, args=(q,))
    threads.append(sb_thread)
    sb_thread.start()    
    
    al_thread = threading.Thread(target=alert_listener.start_alert_listener, args=(q,))
    threads.append(al_thread)
    al_thread.start()
    
    while sb_thread.isAlive() and al_thread.isAlive():
        time.sleep(0.5)