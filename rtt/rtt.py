import threading
import ping3
import time


class RTT(threading.Thread):
    __SAMPLING_TIME = 10

    def __init__(self, host):
        super().__init__()
        self.__is_active = False
        self.__host = host
        self.__mean = 0
        self.__num_samples = 0
        self.__var = 0

    def __update_data(self, value):
        self.__num_samples += 1
        self.__var = self.__var + ((self.__num_samples - 1) * (value - self.__mean) * (
            value - self.__mean) / self.__num_samples - self.__var) / self.__num_samples
        self.__mean = self.__mean + (value - self.__mean) / self.__num_samples

    def run(self):
        self.__is_active = True
        while self.__is_active:
            seconds = ping3.ping(self.__host)
            self.__update_data(seconds)
            time.sleep(RTT.__SAMPLING_TIME)

    def stop(self):
        self.__is_active = False

    def get_estimation(self):
        return self.__mean + 4 * self.__var**0.5
