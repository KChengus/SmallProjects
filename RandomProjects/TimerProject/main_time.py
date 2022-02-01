import tkinter as tk
from time import time
from math import floor
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600

        # self.time_width = round(150 * self.px_to_text_unit_x)
        # self.time_height = round(120 * self.px_to_text_unit_y / 2)

        self.time_font = 30
        self.button_font = 10
        self.button_width = 000 #TODO Come up with width
        self.button_height = 60


        self.space_width = 30 #* self.px_to_text_unit_x
        self.space_height = 100 #* self.px_to_text_unit_y

        self.title_font = 20
        self.title_height = round(self.space_height / 2)

        self.colors = {"BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        self.speed = 50 # in miliseconds

class HandleTime:

    def __init__(self):
        # create variables accessble to all methods
        self.initial_time = time()
        # the timer will always be stopped at first
        self.stop = True
        self.text_stop_start = " Start "
        self.reset_time()


    def start_stop_time(self):
        if self.stop:
            self.initial_time = time()
        else: # the timer was on
            self.stop_seconds = self.total_seconds
        # create a switch each time this method is used
        self.stop = not self.stop
        if self.stop:
            self.text_stop_start = " Start "
        else:
            self.text_stop_start = "Stop"

    def add_zero_front(self):
        #length of a unit time can a length of either 1 or 2
        sec = str(self.seconds)
        minu = str(self.minutes)
        hours = str(self.hours)
        if len(sec) == 1:
            sec = '0' + sec
        if len(minu) == 1:
            minu = '0' + minu
        if len(hours) == 1:
            hours = '0' + hours
        return sec, minu, hours


    def calculate_time(self):

        self.seconds = self.total_seconds % 60
        if (self.total_seconds == self.destination):
            self.destination += 60
            # add minute
            self.minutes += 1
            if self.minutes % 60 == 0 and self.minutes != 0:
                self.minutes = 0
                self.hours += 1


    def time_tracker(self):
        if not self.stop:
            # the timer is on
            self.total_seconds = floor(time() - self.initial_time) + self.stop_seconds
            self.calculate_time()
            s_sec, s_minu, s_hours  = self.add_zero_front()
            self.display_time = f"{s_hours}:{s_minu}:{s_sec}"


    def reset_time(self):
        self.display_time = "00:00:00"
        self.total_seconds = 0
        self.stop_seconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.destination = 60 # next target in total_seconds
        self.initial_time = time()

    def complete_reset(self):
        self.reset_time()
        self.stop = True
        self.text_stop_start = " Start "

class Timer(Settings):

    def __init__(self):
        super().__init__()

        self.screen = tk.Tk()
        self.screen.configure(background="lightblue")
        self.screen.geometry(f"{self.screen_width}x{self.screen_height}")

        #   1   2   3
        #   4   5   6
        # create 6 objects of the class HandleTime
        self.handle_time1 = HandleTime()
        self.handle_time2 = HandleTime()
        self.handle_time3 = HandleTime()
        self.handle_time4 = HandleTime()
        self.handle_time5 = HandleTime()
        self.handle_time6 = HandleTime()

    def update(self):
        self.manage()
        self.configure_display()
        self.screen.after(self.speed, self.update)

    def main(self):
        self.screen.bind_all('<Key>', self.key) # responds to keypresses
        self.display()
        self.update()
        #tk.Label(self.screen, text="adfsd").place(relx = 0.1, rely= 0.1)
        self.screen.mainloop()

    def key(self, event):
        # event is a keypress
        if (event.char == '1'):
            self.handle_time1.start_stop_time()
        elif (event.char == '2'):
            self.handle_time2.start_stop_time()
        elif (event.char == '3'):
            self.handle_time3.start_stop_time()
        elif (event.char == '4'):
            self.handle_time4.start_stop_time()
        elif (event.char == '5'):
            self.handle_time5.start_stop_time()
        elif (event.char == '6'):
            self.handle_time6.start_stop_time()
        elif (event.char == 'r'):
            self.total_reset()
    def manage(self):
        self.handle_time1.time_tracker()
        self.handle_time2.time_tracker()
        self.handle_time3.time_tracker()
        self.handle_time4.time_tracker()
        self.handle_time5.time_tracker()
        self.handle_time6.time_tracker()

    def configure_display(self):
        self.b1_start_stop.config(text=self.handle_time1.text_stop_start)
        self.l1_timer.config(text=self.handle_time1.display_time)

        self.b2_start_stop.config(text=self.handle_time2.text_stop_start)
        self.l2_timer.config(text=self.handle_time2.display_time)

        self.b3_start_stop.config(text=self.handle_time3.text_stop_start)
        self.l3_timer.config(text=self.handle_time3.display_time)

        self.b4_start_stop.config(text=self.handle_time4.text_stop_start)
        self.l4_timer.config(text=self.handle_time4.display_time)

        self.b5_start_stop.config(text=self.handle_time5.text_stop_start)
        self.l5_timer.config(text=self.handle_time5.display_time)

        self.b6_start_stop.config(text=self.handle_time6.text_stop_start)
        self.l6_timer.config(text=self.handle_time6.display_time)

    def total_reset(self):
        self.handle_time1.complete_reset()
        self.handle_time2.complete_reset()
        self.handle_time3.complete_reset()
        self.handle_time4.complete_reset()
        self.handle_time5.complete_reset()
        self.handle_time6.complete_reset()

    def display(self):
        # time box and button box for upper row
        each_cell_width = self.screen_width // 3
        each_cell_height = self.screen_height // 2
        font_multiplier = 2.5
        # 1. ---------------------------------------------------------------------------------------------------------
        self.b1_start_stop = tk.Button(self.screen, bg="lightgreen", fg="white", text=self.handle_time1.text_stop_start,font=(None, self.button_font), command=self.handle_time1.start_stop_time)

        self.b1_start_stop.place(x=self.space_width, y=self.space_height + round(self.time_font * font_multiplier))

        self.l1_timer = tk.Label(self.screen, bg="lightgreen", fg="white",text=self.handle_time1.display_time, font=(None, self.time_font))

        self.l1_timer.place(x=self.space_width, y=self.space_height)

        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset", font=(None, self.button_font),
                  command=self.handle_time1.reset_time).place(x=self.space_width + self.time_font * 3,y=self.space_height + round(self.time_font * font_multiplier))

        tk.Label(self.screen, bg="lightgreen", fg="white", text="1. Communication", font=(None, self.title_font)).place(x=self.space_width, y=self.title_height)

        # 2.---------------------------------------------------------------------------------------------------------
        self.b2_start_stop =  tk.Button(self.screen, bg="lightgreen", fg="white", text=self.handle_time2.text_stop_start,font=(None, self.button_font), command=self.handle_time2.start_stop_time)

        self.b2_start_stop.place(x=self.space_width + each_cell_width, y=self.space_height + round(self.time_font * font_multiplier))

        self.l2_timer = tk.Label(self.screen, bg="lightgreen", fg="white", text=self.handle_time2.display_time, font=(None, self.time_font))

        self.l2_timer.place(x=self.space_width + each_cell_width, y=self.space_height)

        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset", font=(None, self.button_font),
                  command=self.handle_time2.reset_time).place(x=self.space_width + self.time_font * 3 + each_cell_width,
                  y=self.space_height + round(self.time_font * font_multiplier))

        tk.Label(self.screen, bg="lightgreen", fg="white", text="2. Homework", font=(None, self.title_font)).place(x=self.space_width + each_cell_width, y=self.title_height)

        # 3. ---------------------------------------------------------------------------------------------------------

        self.b3_start_stop = tk.Button(self.screen, bg="lightgreen", fg="white", text=self.handle_time3.text_stop_start, font=(None, self.button_font), command=self.handle_time3.start_stop_time)
        self.b3_start_stop.place(x=self.space_width + each_cell_width * 2, y=self.space_height + round(self.time_font * font_multiplier))

        self.l3_timer = tk.Label(self.screen, bg="lightgreen", fg="white", text=self.handle_time3.display_time, font=(None, self.time_font))
        self.l3_timer.place(x=self.space_width + each_cell_width * 2, y=self.space_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset", font=(None, self.button_font), command=self.handle_time3.reset_time).place(x=self.space_width + self.time_font * 3 + each_cell_width * 2,
                  y=self.space_height + round(self.time_font * font_multiplier))

        tk.Label(self.screen, bg="lightgreen", fg="white", text="3. Rest", font=(None, self.title_font)).place(x=self.space_width + each_cell_width * 2, y=self.title_height)

        # 4. ---------------------------------------------------------------------------------------------------------
        self.b4_start_stop = tk.Button(self.screen, bg="lightgreen", fg="white", text=self.handle_time4.start_stop_time , font=(None, self.button_font), command=self.handle_time4.start_stop_time)
        self.b4_start_stop.place(x=self.space_width, y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)

        self.l4_timer = tk.Label(self.screen, bg="lightgreen", fg="white", text=self.handle_time4.display_time, font=(None, self.time_font))
        self.l4_timer.place(x=self.space_width, y=self.space_height + each_cell_height)

        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset", font=(None, self.button_font), command=self.handle_time4.reset_time).place(x=self.space_width + self.time_font * 3, y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)

        tk.Label(self.screen, bg="lightgreen", fg="white", text="4. LearnC++", font=(None, self.title_font)).place(x=self.space_width, y=self.title_height + each_cell_height)


        # 5. ---------------------------------------------------------------------------------------------------------
        self.b5_start_stop = tk.Button(self.screen, bg="lightgreen", fg="white", text=self.handle_time5.text_stop_start , font=(None, self.button_font), command=self.handle_time5.start_stop_time)
        self.b5_start_stop.place(x=self.space_width + each_cell_width,y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)

        self.l5_timer = tk.Label(self.screen, bg="lightgreen", fg="white", text=self.handle_time5.display_time, font=(None, self.time_font))
        self.l5_timer.place(x=self.space_width + each_cell_width, y=self.space_height + each_cell_height)

        tk.Label(self.screen, bg="lightgreen", fg="white",
                 text="5. Programming", font=(None, self.title_font)).place(x=self.space_width + each_cell_width, y=self.title_height + each_cell_height)
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset",font=(None, self.button_font), command=self.handle_time5.reset_time).place(x=self.space_width + self.time_font * 3 + each_cell_width,y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)

        # 6. ---------------------------------------------------------------------------------------------------------
        self.b6_start_stop = tk.Button(self.screen, bg="lightgreen", fg="white", text=self.handle_time6.text_stop_start, font=(None, self.button_font), command=self.handle_time6.start_stop_time)
        self.b6_start_stop.place(x=self.space_width + each_cell_width * 2, y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)

        self.l6_timer = tk.Label(self.screen, bg="lightgreen", fg="white", text=self.handle_time6.display_time, font=(None, self.time_font))
        self.l6_timer.place(x=self.space_width + each_cell_width * 2, y=self.space_height + each_cell_height)

        tk.Label(self.screen, bg="lightgreen", fg="white", text="6. Other", font=(None, self.title_font)).place(x=self.space_width + each_cell_width * 2, y=self.title_height + each_cell_height)

        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset", font=(None, self.button_font), command=self.handle_time6.reset_time).place(x=self.space_width + self.time_font * 3 + each_cell_width * 2,y=self.space_height + round(self.time_font * font_multiplier) + each_cell_height)

        # all reset
        tk.Button(self.screen, bg="lightgreen", fg="white", text="Reset All", font=(None, self.button_font * 2), command=self.total_reset).place(relx=0.4, rely=0.4)

if __name__ == "__main__":
    Timer().main()