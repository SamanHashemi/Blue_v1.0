import datetime
import random


class Time:
    def __init__(self):
        # Trigger words from time
        self.trigger_words = ["time"]
        self.priority = 1

    def time(self) -> str:
        now = datetime
        hour = now.hour
        minute = now.minute
        responses = ["Oh, right now it's", "It's", ]
        if hour > 12:
            time = str(hour-12) + ":" + str(minute) + "PM"
        elif hour == 12:
            time = str(12) + ":" + str(minute) + "PM"
        elif hour == 0:
            time = str(12) + ":" + str(minute) + "AM"
        elif hour < 12:
            time = str(hour) + ":" + str(minute) + "AM"

        responses = ["Oh, right now it's " + time, "It's " + time, time + " Is the time"]
        return str(responses[random.randint(0, len(responses)-1)])