import atexit

from apscheduler.schedulers.background import BackgroundScheduler


class Schedule(object):
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def tick(self):
        print('>>>>')

    def start(self):
        self.scheduler.add_job(self.tick, 'interval', seconds=3)
        self.scheduler.start()
        atexit.register(lambda: self.shutdown())

    def shutdown(self):
        print('stop')
        self.scheduler.shutdown(wait=False)