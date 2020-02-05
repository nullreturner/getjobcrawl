from random import random
import threading
import time

result = None
result_available = threading.Event()

def background_calculation():
    time.sleep(random() * 5 * 5)

    global result
    result = 42
    result_available.set()

    time.sleep(10)

def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

    # while result is None:
    #     time.sleep(5)

    # thread.join()

    result_available.wait()

    print('The result is', result)

if __name__ == '__main__':
    main()