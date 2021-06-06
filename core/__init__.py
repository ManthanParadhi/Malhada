import datetime
import subprocess
import inflect
import subprocess
from pynput.keyboard import Key, Controller
kb = Controller()


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
        return ans

    @ staticmethod
    def get_weather():
        return ans

    @ staticmethod
    def play_pause():
        if (('resso' in str(subprocess.check_output(('tasklist', '/fi', 'imagename eq resso.exe'))).lower()) or ('wmplayer' in str(subprocess.check_output(('tasklist', '/fi', 'imagename eq wmplayer.exe'))).lower())) == False:
            subprocess.Popen("start wmplayer.exe", shell=True)

        kb.press(Key.media_play_pause)
        kb.release(Key.media_play_pause)

    @ staticmethod
    def open_chrome():
        subprocess.Popen("start www.google.com", shell=True)
        return
