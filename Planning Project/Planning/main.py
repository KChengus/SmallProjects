from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import datetime

from pygments import highlight
Builder.load_file("main.kv")

class MainWindow(BoxLayout):
    active = False
    highlightWidgetId = ""
    l = []
    timeActivityIds = []
    tempIndex = 1
    now = datetime.datetime.now()


    def increment_time(self, interval):

        time = self.l[0]
        startingTimeHour, startingTimeMinute = map(int, time[0].split(":"))
        endingTimeHour, endingTimeMinute = map(int, time[1].split(":"))

        timeNow = datetime.datetime.now()
        if self.active:
            if (timeNow.hour == endingTimeHour and timeNow.minute >= endingTimeMinute) or timeNow.hour > endingTimeHour:
                self.active = False
                self.ids[self.highlightWidgetId].background_color = 0, 0, 0, 1
                self.l.pop(0)
                
                if len(self.l) <= 0:
                    App.get_running_app().stop()
                    Window.close()
                    return
            
        else:
            
            if (timeNow.hour == startingTimeHour and timeNow.minute >= startingTimeMinute) or timeNow.hour > startingTimeHour:
                self.active = True
                self.highlightWidgetId = self.timeActivityIds.pop(0)
                self.ids[self.highlightWidgetId].background_color = 0.6, .1, .1, 1
        
        self.ids.displayCurrentTime.text = datetime.datetime.now().strftime('%H : %M')


    def getTimeTextInput(self):

        # create for loop for each ids
        for ids in self.ids:
            if not ids.startswith("timetext"):
                continue

            self.timeActivityIds.append(ids)

            # split string time into hours and minutes
            text = self.ids[ids].text
            startingTime, hyphen, endingTime = text.split(" ")
            self.l.append((startingTime, endingTime))
            
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, 2)


class PlanApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    PlanApp().run()