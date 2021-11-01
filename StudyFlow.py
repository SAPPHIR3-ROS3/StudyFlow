from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk
from tkinter.ttk import Button
from tkinter.ttk import Entry

class App(Tk):
    def __init__(self):
        super().__init__() # super class initialization
        self.title('StudyFlow') # app title
        self.Position() # positioning the window at center of the screen
        self.GraphicInit() # UI of app
        self.ResetValues() # set the entries to default values
        self.InSession = False # boolean to check if the user started the process
        self.InCore = False # boolean to check if the user is in the core part of session
        self.InPause = False # boolean to check if the user pause the timer
        self.InBreak = False # boolean to check if the user is in break time (after the core time)
        self.Counter = 0 # count the time
        self.ActiveMinTime = 0 # set minimum time
        self.ActiveMaxTime = 0 #set maximum time
        self.ActiveBreakTime = 0 #set break time
        self.ActiveOverTime = 0 #set over time
        self.ActiveSession = 0 #set sessions repetition

    def Position(self, Width = 800, Height = 600, StartX = -1, StartY = -1): # this function set dimensions and osition of the app
        if StartX == -1 or StartY == -1 or (StartX == -1 and StartY == -1): # chechk if parameter are not set
            StartX = self.winfo_screenwidth()//2 - Width//2 # x center position
            StartY = self.winfo_screenheight()//2 - Height//2 # y center position

        self.geometry(f'{Width}x{Height}+{StartX}+{StartY}') #placing the window

    def GraphicInit(self): # this function draws the graphics
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

        self.TimerValue = StringVar(self.Win, '00:00') # label string for display the time
        self.TimerDisplay = Label(self.Win, textvariable = self.TimerValue, font = ('courier', 160), fg = '#ffffff', bg = '#000000') #timer label
        self.TimerDisplay.place(anchor = 'n', relx = 0.5 , rely = 0.27, relwidth = 0.95) # placing the timer label

        self.StartStopButton = Button(self.Win, text = 'Start/Stop', command = lambda : self.StartStop()) # start/stop button to initiate/finish the sequence
        self.StartStopButton.place(anchor = 'n', relx = 0.175, rely = 0.7, relwidth = 0.3, relheight = 0.1) # placing the start/stop button
        self.PlayPauseButton = Button(self.Win, text = 'Play/Pause', command = lambda : self.PlayPause()) # play/pause button to control the sequences
        self.PlayPauseButton.place(anchor = 'n', relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.1) # placing the play/pause button
        self.ResetButton = Button(self.Win, text = 'Reset values', command = lambda : self.ResetValues()) # reset button to reset the entries to default
        self.ResetButton.place(anchor = 'n', relx = 0.825, rely = 0.7, relwidth = 0.3, relheight = 0.1) # placing the reset button
        self.StartBreakButton = Button(self.Win, text = 'Skip to break time', command = lambda : self.SkipToBreak()) # TODO implement lambdas to make the button work
        self.StartBreakButton.place(anchor = 'n', relx = 0.175, rely = 0.825, relwidth = 0.3, relheight = 0.1) # placing the skip button
        self.EndSessionButton = Button(self.Win, text = 'End current session', command = lambda : self.EndSession()) # button to end the current session (break time included)
        self.EndSessionButton.place(anchor = 'n', relx = 0.5, rely = 0.825, relwidth = 0.3, relheight = 0.1) # placing the end button
        self.NextSessionButton = Button(self.Win, text = 'Go to next session', command = lambda : self.NextSession())
        self.NextSessionButton.place(anchor = 'n', relx = 0.825, rely = 0.825, relwidth = 0.3, relheight = 0.1) # placing the

    def ConvertedCounter(self):
        Seconds = str(self.Counter % 60).zfill(2)
        Minutes = str((self.Counter - int(Seconds)) // 60).zfill(2)

        return f'{Minutes}:{Seconds}'

    def StartStop(self): # this function start/stop the sessions of study
        if self.InSession: # check if the session is already active
            self.Counter = 0 # reset the timer
            self.TimerValue.set('00:00') # reset the displayed timer
            self.InSession = False # reset session boolean
            self.ActiveMinTime = 0 # reset minimum time
            self.MinTime[1].config(state = 'enabled') # enabling input on min time field
            self.ActiveMaxTime = 0 # reset mmaximum time
            self.MaxTime[1].config(state = 'enabled') # enabling input on max time field
            self.ActiveBreakTime = 0 # reset minimum time
            self.BreakTime[1].config(state = 'enabled') # enabling input on break time field
            self.ActiveOverTime = 0 # reset minimum time
            self.OverTime[1].config(state = 'enabled') # enabling input on over time field
            self.ActiveSession = 0 # reset minimum time
            self.Sessions[1].config(state = 'enabled') # enabling input on session field
            self.InSession = False # reset the user to not in session
            self.InCore = False # reset the user to nt in core part of session
            self.InPause = False # reset the user to not in pause during session
            self.InBreak = False # reset the user to not in break part

        else:
            self.InSession = True # set the user in session mode
            self.ActiveMinTime = int(self.MinTime[1].get()) * 60 # convert the user given input to minutes as min time
            self.MinTime[1].config(state = 'disabled') # disable the change of input in the entrybox of min time
            self.ActiveMaxTime = int(self.MaxTime[1].get()) * 60 # convert the user given input to minutes as max time
            self.MaxTime[1].config(state = 'disabled') # disable the change of input in the entrybox of max time
            self.ActiveBreakTime = int(self.BreakTime[1].get()) * 60 # convert the user given input to minutes as break time
            self.BreakTime[1].config(state = 'disabled') # disable the change of input in the entrybox of break time
            self.ActiveOverTime = int(self.OverTime[1].get()) * 60 # convert the user given input to minutes as over time
            self.OverTime[1].config(state = 'disabled') # disable the change of input in the entrybox of over time
            self.ActiveSession = 1 # set the use in the first session
            self.Sessions[1].config(state = 'disabled') # disable the change of input in the entrybox of number of sessions
            self.InSession = True # set the user in session
            self.InCore = True # put the user in core part of the session
            self.TimeCount() # start the timer

    def PlayPause(self): # this function play or pause the timer
        if self.InSession or (self.InBreak and not self.InSession): # check if user is in session or in break
            if self.InPause: # check if the user is in pause
                self.InPause = False # reverse the pause state
            else: # if the user is not in pause
                self.InPause = True # reverse the pause state

    def TimeCount(self):
        if self.InSession:
            if not self.InPause:
                if self.Counter > self.ActiveMinTime:
                    self.InCore = False

                self.Counter += 1
                self.TimerValue.set(self.ConvertedCounter())

                if self.Counter < self.ActiveMaxTime + self.ActiveOverTime:
                    self.after(1000, self.TimeCount)
                else:
                    self.InSession = False
                    self.Counter = 0

        if self.InBreak and not self.InSession:
            if not self.InPause:
                self.Counter += 1

                if self.Counter < self.ActiveBreakTime:
                    self.TimerValue.set(self.ConvertedCounter())
                    self.after(1000, self.TimeCount)
                else:
                    self.InBreak = False
                    self.Counter = 0

        if not self.InSession and not self.InSession:
            self.after(1000, self.TimeCount())


    def ResetValues(self): # this function reset values to defalut
        self.MinTime[1].delete(0,'end')
        self.MinTime[1].insert(0, '40')
        self.MaxTime[1].delete(0,'end')
        self.MaxTime[1].insert(0, '60')
        self.BreakTime[1].delete(0,'end')
        self.BreakTime[1].insert(0, '25')
        self.OverTime[1].delete(0,'end')
        self.OverTime[1].insert(0, '10')
        self.Sessions[1].delete(0,'end')
        self.Sessions[1].insert(0, '3')

    def SkipToBreak(self):
        if not self.InCore:
            self.InSession = False
            self.InBreak = True
            self.Counter = 0

    def EndSession(self):
        pass

    def NextSession(self):
        pass

if __name__ == '__main__':
    Application = App()
    Application.mainloop()