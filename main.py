import datetime
import pandas as pd
import threading
from multiprocessing import Process

li1 = [x for x in range(0, 9999999)]


def write_to_csv():
    df = pd.DataFrame({'numbers': li1})
    df.to_csv('numbers.csv')


def write_to_csv2():
    df = pd.DataFrame({'numbers': li1})
    df.to_csv('numbers.csv')


if __name__ == "__main__":
    # ----------------------------------------------------------------------------------------------------------
    # by one process
    # ----------------------------------------------------------------------------------------------------------
    time_start = datetime.datetime.now()
    write_to_csv()
    time_finish = datetime.datetime.now()
    print(f'by one process {time_finish - time_start}')
    # -----------------------------------------------------------------------------------------------------------
    # by two streams
    # -----------------------------------------------------------------------------------------------------------
    thread1 = threading.Thread(target=write_to_csv)
    thread2 = threading.Thread(target=write_to_csv)
    time_start = datetime.datetime.now()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    time_finish = datetime.datetime.now()
    print(f'by two streams {time_finish - time_start}')
    # ------------------------------------------------------------------------------------------------------------
    # by two process
    # ------------------------------------------------------------------------------------------------------------
    process1 = Process(target=write_to_csv)
    process2 = Process(target=write_to_csv)
    time_start = datetime.datetime.now()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    time_finish = datetime.datetime.now()
    print(f'by two process {time_finish - time_start}')
    # ------------------------------------------------------------------------------------------------------------
    # by two process with def in every process
    # ------------------------------------------------------------------------------------------------------------
    process1 = Process(target=write_to_csv)
    process2 = Process(target=write_to_csv2)
    time_start = datetime.datetime.now()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    time_finish = datetime.datetime.now()
    print(f'by two process with def in every process {time_finish - time_start}')