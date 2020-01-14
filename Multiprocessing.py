# Give credit where credit is due
# Tutorial here: https://www.youtube.com/watch?v=fKl2JW_qrso

import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

def main():
    # Start and finish help us calculate how long the program ran for
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:    
        # Option 2 -------------
        results = [executor.submit(do_something, 1) for _ in range(10)]
        for f in concurrent.futures.as_completed(results):
            f.result()
        
        # Option 1 -------------
        """
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        f1.result()
        f2.result()
        """

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 3)} second(s)')
    


if __name__ == "__main__":    
    main()

    