# Give credit where credit is due
# Tutorial here: https://www.youtube.com/watch?time_continue=1&v=5JSloPGocSY&feature=emb_logo
# python 3.7.6

import threading
import time

class PrintStuff(threading.Thread):
    def __init__(self):
        super(PrintStuff, self).__init__()

    def print_stuff(self):
        print("Printing stuff")
        #time.sleep(1)


# Start and finish help us calculate how long the program ran for
start = time.perf_counter()
thread_list = []
for _ in range(10):
    thread = PrintStuff()
    thread_list.append(thread.print_stuff())
    thread.start()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 3)} second(s)')
