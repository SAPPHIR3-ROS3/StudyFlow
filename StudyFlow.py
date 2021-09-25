from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('StudyFlow')

        ScreenWidth = self.winfo_screenwidth()
        ScreenHeight = self.winfo_screenheight()
        Width = 800
        Height = 600
        StartX = ScreenWidth//2 - Width//2
        StartY = ScreenHeight//2 - Height//2
        self.geometry(f'{Width}x{Height}+{StartX}+{StartY}')

        self.Win = Frame(self)
        self.Win.place(anchor='n', relwidth = 1.0, relheight = 1.0, relx = 0.5)

        self.TimeFrames = [Frame(self), Frame(self), Frame(self), Frame(self), Frame(self)]
        TimeLabelSize = 14

        self.TimeFrames[0].place(anchor='nw',relwidth = 0.3333, relheight = 1.0, relx = 0)
        self.MinTime =\
        [
            Label(self.TimeFrames[0], text = 'Min. Time (minutes)', font = ('courier', TimeLabelSize)),
            Entry(self.TimeFrames[0], font = ('courier', 20))
        ]
        self.MinTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94)
        self.MinTime[1].place(anchor = 'n', relx = 0.5, rely = 0.06, relwidth = 0.5)
        self.TimeFrames[1].place(anchor='n',relwidth = 0.3333, relheight = 1.0, relx = 0.5)
        self.MaxTime =\
        [
            Label(self.TimeFrames[1], text = 'Max. Time (minutes)', font = ('courier', TimeLabelSize)),
            Entry(self.TimeFrames[1], font = ('courier', 20))
        ]
        self.MaxTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94)
        self.MaxTime[1].place(anchor = 'n', relx = 0.5, rely = 0.06, relwidth = 0.5)
        self.TimeFrames[2].place(anchor='ne',relwidth = 0.3333, relheight = 1.0, relx = 1.0)
        self.BreakTime =\
        [
            Label(self.TimeFrames[2], text = 'Break Time (minutes)', font = ('courier', TimeLabelSize)),
            Entry(self.TimeFrames[2], font = ('courier', 20))
        ]
        self.BreakTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94)
        self.BreakTime[1].place(anchor = 'n', relx = 0.5, rely = 0.06, relwidth = 0.5)
        self.TimeFrames[3].place(anchor='nw',relwidth = 0.5, relheight = 1.0, relx = 0, rely = 0.12)
        self.OverTime =\
        [
            Label(self.TimeFrames[3], text = 'OverTime (minutes)', font = ('courier', TimeLabelSize)),
            Entry(self.TimeFrames[3], font = ('courier', 20))
        ]
        self.OverTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94)
        self.OverTime[1].place(anchor = 'n', relx = 0.5, rely = 0.06, relwidth = 0.4)
        self.TimeFrames[4].place(anchor='ne',relwidth = 0.5, relheight = 1.0, relx = 1.0, rely = 0.12)
        self.Sessions =\
        [
            Label(self.TimeFrames[4], text = 'Sessions', font = ('courier', TimeLabelSize)),
            Entry(self.TimeFrames[4], font = ('courier', 20))
        ]
        self.Sessions[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94)
        self.Sessions[1].place(anchor = 'n', relx = 0.5, rely = 0.06, relwidth = 0.4)

        self.Timer = StringVar()
        self.Timer.set('00:00')
        self.TimerDisplay = Label(self, textvariable = self.Timer, font = ('courier', 160), fg = '#ffffff', bg = '#000000')
        self.TimerDisplay.place(anchor = 'n', relx = 0.5 , rely = 0.3)

    def update(self):
        pass

if __name__ == '__main__':
    Application = App()
    Application.mainloop()