import datetime
import inflect


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        ans = "The time now is {} {} {} {} {} {}".format(
            now.hour, inflect.engine().singular_noun("hours", now.hour),
            now.minute, inflect.engine().singular_noun("minutes", now.minute),
            now.second, inflect.engine().singular_noun("seconds", now.second))
        return ans

    @ staticmethod
    def get_date():
        now = datetime.datetime.now()
        ans = "Today is {} {} {}".format(
            inflect.engine().ordinal(now.day), now.strftime('%B'), now.year)
        print(ans)
        return ans

    @ staticmethod
    def get_weather():
        now = datetime.datetime.now()
        month = []
        ans = 1
        return ans


ans = SystemInfo.get_time()
print(ans)
