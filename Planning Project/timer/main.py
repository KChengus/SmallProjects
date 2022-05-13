from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import DragBehavior
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import DragBehavior

Config.set('graphics', 'multisamples', '0')
Builder.load_file("kfile.kv")

class ExerciseButton(Button):
    mouseDown = False
    def on_touch_down(self, touch):
        self.mouseDown = True
        return super().on_touch_down(touch)
       
    def on_touch_move(self, touch):
        
        if self.mouseDown and self.collide_point(*touch.pos):
            self.center_x = touch.x
            self.center_y = touch.y
        return super().on_touch_move(touch)
        
    def on_touch_up(self, touch):
        self.mouseDown = False
        return super().on_touch_up(touch)
       



class MainWidget(BoxLayout):
    number = NumericProperty(0)
     
    def __init__(self, **kwargs):
 
        # The super() builtin
        # returns a proxy object that
        # allows you to refer parent class by 'super'.
        super(MainWidget, self).__init__(**kwargs)
 
        # Create the clock and increment the time by .1 ie 1 second.
        Clock.schedule_interval(self.increment_time, .1)
 
    def increment_time(self, interval):

        self.number += 0.1

    def start(self):
         
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)
    
    def stop(self):
        Clock.unschedule(self.increment_time)

    def reset(self):
        pass

class PlanApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    PlanApp().run()