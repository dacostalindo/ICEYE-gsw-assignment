import threading, time, signal
from datetime import timedelta
import xkcd as xkcd_class

WAIT_TIME_SECONDS = 3600
MAX_COMICS = 2355

class ProgramKilled(Exception):
    pass

def save_xkcd_comics():
    xkcd_object = xkcd_class.XKCD_SERVICE(MAX_COMICS)
    xkcd_object.save_comic()
    print('New image added at: {} '.format(time.ctime()))


def signal_handler(signum, frame):
    raise ProgramKilled

class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
                self.stopped.set()
                self.join()
    def run(self):
            while not self.stopped.wait(self.interval.total_seconds()):
                self.execute(*self.args, **self.kwargs)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=save_xkcd_comics)
    job.start()

    while True:
          try:
              time.sleep(1)
          except ProgramKilled:
              print ("Program killed: running cleanup code")
              job.stop()
              break
