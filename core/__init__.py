import datetime


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        ans = "The time now is {} {} {} {}".format(
            now.hour, "hour"if now.hour == 1 else"hours", now.minute, "minute"if now.minute == 1 else"minutes")
        return ans

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        ans = "The date is {} {} {}".format(
            now.day, now.month, now.year)
        return ans
