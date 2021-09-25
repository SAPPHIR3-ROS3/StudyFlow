from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk
from tkinter.ttk import Button
from tkinter.ttk import Entry

class App(Tk):
    def __init__(self):
        super().__init__() # super class initialization
        self.title('StudyFlow') #app title
        self.Position() # positioning the window at center of the screen
        self.Win = Frame(self) # root container
        self.Win.place(anchor='n', relwidth = 1.0, relheight = 1.0, relx = 0.5) #placing the root container

        self.TimeFrames = [Frame(self.Win), Frame(self.Win), Frame(self.Win), Frame(self.Win), Frame(self.Win)] #containers for labels and entries
        TimeLabelSize = 14 # font size of label above entries
        LabelEntryDistance = 0.04 # distance between label and entry (percentage)
        # MIN TIME
        self.TimeFrames[0].place(anchor='nw',relwidth = 0.3333, relheight = 1.0, relx = 0) # min time frame (row 1 place 1)
        self.MinTime =\
        [
            Label(self.TimeFrames[0], text = 'Min. Time (minutes)', font = ('courier', TimeLabelSize)), # min time label
            Entry(self.TimeFrames[0], font = ('courier', 20)) # min time entry
        ]
        self.MinTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94) # placing the min time label
        self.MinTime[1].place(anchor = 'n', relx = 0.5, rely = LabelEntryDistance, relwidth = 0.82) # placing the min rim entry
        # MAX TIME
        self.TimeFrames[1].place(anchor='n',relwidth = 0.3333, relheight = 1.0, relx = 0.5) # max time frame (row 1 place 2)
        self.MaxTime =\
        [
            Label(self.TimeFrames[1], text = 'Max. Time (minutes)', font = ('courier', TimeLabelSize)), # max time label
            Entry(self.TimeFrames[1], font = ('courier', 20)) # max time entry
        ]
        self.MaxTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94) # placing the max time label
        self.MaxTime[1].place(anchor = 'n', relx = 0.5, rely = LabelEntryDistance, relwidth = 0.82) # placing the max time entry
        # BREAK TIME
        self.TimeFrames[2].place(anchor='ne',relwidth = 0.3333, relheight = 1.0, relx = 1.0) # break time frame
        self.BreakTime =\
        [
            Label(self.TimeFrames[2], text = 'Break Time (minutes)', font = ('courier', TimeLabelSize)), # break time label
            Entry(self.TimeFrames[2], font = ('courier', 20)) # break time entry
        ]
        self.BreakTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94) # placing the break time label
        self.BreakTime[1].place(anchor = 'n', relx = 0.5, rely = LabelEntryDistance, relwidth = 0.82) # placing the break time entry
        # OVER TIME
        self.TimeFrames[3].place(anchor='nw',relwidth = 0.5, relheight = 1.0, relx = 0, rely = 0.11) # over time frame
        self.OverTime =\
        [
            Label(self.TimeFrames[3], text = 'OverTime (minutes)', font = ('courier', TimeLabelSize)), # over time label
            Entry(self.TimeFrames[3], font = ('courier', 20)) # over time entry
        ]
        self.OverTime[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94) # placing the over time label
        self.OverTime[1].place(anchor = 'n', relx = 0.5, rely = LabelEntryDistance, relwidth = 0.5) # placing the over time entry
        # SESSION
        self.TimeFrames[4].place(anchor='ne',relwidth = 0.5, relheight = 1.0, relx = 1.0, rely = 0.11) # session frame
        self.Sessions =\
        [
            Label(self.TimeFrames[4], text = 'Sessions', font = ('courier', TimeLabelSize)), # session label
            Entry(self.TimeFrames[4], font = ('courier', 20)) # session entry
        ]
        self.Sessions[0].place(anchor = 'n', relx = 0.5, relwidth = 0.94) # placing the session label
        self.Sessions[1].place(anchor = 'n', relx = 0.5, rely = LabelEntryDistance, relwidth = 0.5) # placingthe session entry

        self.Timer = StringVar(self.Win, '00:00') # label string for display the time
        self.TimerDisplay = Label(self, textvariable = self.Timer, font = ('courier', 160), fg = '#ffffff', bg = '#000000') #timer label
        self.TimerDisplay.place(anchor = 'n', relx = 0.5 , rely = 0.27) # placing the timer label

        self.StartStop = Button(self, text = 'Start/Stop') # start/stop button to initiate/finish the sequence #TODO implement lambdas to make the button work
        self.StartStop.place(anchor = 'n', relx = 0.25, rely = 0.7, relwidth = 0.3, relheight = 0.1) # placing the start/stop button
        self.StartStop = Button(self, text = 'Play/Pause') # play/pause button to control the sequences #TODO implement lambdas to make the button work
        self.StartStop.place(anchor = 'n', relx = 0.75, rely = 0.7, relwidth = 0.3, relheight = 0.1) # placing the play/pause button
        self.Reset = Button(self, text = 'Reset') #TODO implement lambdas to make the button work
        self.Reset.place(anchor = 'n', relx = 0.5, rely = 0.85, relwidth = 0.8, relheight = 0.1) # placing the reset button

    def Position(self, Width = 800, Height = 600, StartX = -1, StartY = -1): # this function set dimensions and osition of the app
        if StartX == -1 or StartY == -1 or (StartX == -1 and StartY == -1): # chechk if parameter are not set
            StartX = self.winfo_screenwidth()//2 - Width//2 # x center position
            StartY = self.winfo_screenheight()//2 - Height//2 # y center position

        self.geometry(f'{Width}x{Height}+{StartX}+{StartY}') #placing the window

if __name__ == '__main__':
    Application = App()
    Application.mainloop()