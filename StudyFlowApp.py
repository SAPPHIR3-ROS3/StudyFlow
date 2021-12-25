from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QPointF
from PySide6.QtCore import QSize
from PySide6.QtCore import QUrl
from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont
from PySide6.QtGui import QIntValidator
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLayout
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizeGrip
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from sys import exit as Exit

class App(QMainWindow):
    def __init__(self): # constructor
        super(App, self).__init__() # super constructor
        self.isMaximized = False # status of the window at the start of the application
        self.InSession = False # boolean to check if the user started the process
        self.InCore = False # boolean to check if the user is in the core part of session
        self.InPause = False # boolean to check if the user is in the pause
        self.InBreak = False # boolean to check if the user is in the break
        self.Counter = 0 # count the time (study part)
        self.BreakCounter = 0 # count the time (break part)
        self.ActiveMinTime = 0 # set minimum time
        self.ActiveMaxTime = 0 # set maximum time
        self.ActiveBreakTime = 0 # set break time
        self.ActiveOverTime = 0 # set over time
        self.ActiveSession = 0 # set sessions repetition
        self.TotalSessions = 0 # set the total session
        self.DragPos = QPointF(0, 0) # Start position of mouse for the Window
        self.GUI() # GUI initialization
        self.TitleBar.mouseMoveEvent = self.MoveWindow # allow the window to be moved and dragged around by the title bar
        self.setWindowFlag(Qt.FramelessWindowHint) # remove the title bar from the window
        self.setAttribute(Qt.WA_TranslucentBackground) # make the window transparent
        self.MinimizeButton.clicked.connect(lambda: self.showMinimized()) # link the minimize button to the minimize function
        self.MaximizeButton.clicked.connect(lambda: self.Maximize()) # link the minimize button to maximize function
        self.CloseButton.clicked.connect(lambda: self.close()) # link the close button to close function
        self.StartStopButton.clicked.connect(lambda: self.StartStop()) # link the start stop button to the start stop function
        self.PlayPauseButton.clicked.connect(lambda: self.PlayPause()) # link the play pause button to the play pause function
        self.SkipToBreakButton.clicked.connect(lambda: self.SkipToBreak()) # link the skip to break button to the skip to break function
        self.ClickSound = QSoundEffect(self) # Sound played when a button is clicked
        self.ClickSound.setSource(QUrl.fromLocalFile('./Media/click.wav')) # setting the click sound
        self.EndSound = QSoundEffect(self) # Sound played when a part ended
        self.EndSound.setSource(QUrl.fromLocalFile('./Media/endpart.wav')) # setting the end sound
        self.PassPhaseSound = QSoundEffect(self) # Sound played when you pass the min time
        self.PassPhaseSound.setSource(QUrl.fromLocalFile('./Media/passding.wav'))
        self.Timer = QTimer() # timer that manage the elapsing of tim in the application
        self.Timer.timeout.connect( lambda: self.Elapse()) # connect the timer to the timer function
        self.Timer.start(1000) # start the timer
        self.show() # show the window
        
    def GUI(self): # graphic initialization
        self.resize(800, 600)
        self.setMinimumSize(QSize(800, 600))
        self.WindowFrame = QWidget(self)
        self.WindowFrame.setObjectName("WindowFrame")
        self.WindowLayout = QVBoxLayout(self.WindowFrame)
        self.WindowLayout.setSpacing(0)
        self.WindowLayout.setObjectName("WindowLayout")
        self.WindowLayout.setContentsMargins(0, 0, 0, 0)
        self.AppFrame = QFrame(self.WindowFrame)
        self.AppFrame.setObjectName("AppFrame")
        self.AppFrame.setStyleSheet\
        (
            """
            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 250, 221, 255), stop:1 rgba(50, 122, 178, 255));
            border-radius: 15px
            """
        )
        self.AppFrame.setFrameShape(QFrame.NoFrame)
        self.AppFrame.setFrameShadow(QFrame.Raised)
        self.AppLayout = QVBoxLayout(self.AppFrame)
        self.AppLayout.setSpacing(0)
        self.AppLayout.setObjectName("AppLayout")
        self.AppLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QFrame(self.AppFrame)
        self.TitleBar.setObjectName("TitleBar")
        self.TitleBar.setMaximumSize(QSize(16777215, 40))
        self.TitleBar.setStyleSheet("background-color: none;")
        self.TitleBar.setFrameShape(QFrame.NoFrame)
        self.TitleBar.setFrameShadow(QFrame.Raised)
        self.TitleBarLayout = QHBoxLayout(self.TitleBar)
        self.TitleBarLayout.setSpacing(0)
        self.TitleBarLayout.setObjectName("TitleBarLayout")
        self.TitleBarLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleArea = QFrame(self.TitleBar)
        self.TitleArea.setObjectName("TitleArea")
        self.TitleArea.setFrameShape(QFrame.StyledPanel)
        self.TitleArea.setFrameShadow(QFrame.Raised)
        self.TitleLayout = QHBoxLayout(self.TitleArea)
        self.TitleLayout.setObjectName("TitleLayout")
        self.Title = QLabel(self.TitleArea)
        self.Title.setObjectName("Title")
        font = QFont()
        font.setFamilies(["Yu Gothic Light"])
        font.setPointSize(18)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color:rgb(108, 89, 255);")
        self.TitleLayout.addWidget(self.Title)
        self.TitleBarLayout.addWidget(self.TitleArea)
        self.TitleButtons = QFrame(self.TitleBar)
        self.TitleButtons.setObjectName("TitleButtons")
        self.TitleButtons.setMaximumSize(QSize(100, 16777215))
        self.TitleButtons.setFrameShape(QFrame.StyledPanel)
        self.TitleButtons.setFrameShadow(QFrame.Raised)
        self.TitleButtonsLayout = QHBoxLayout(self.TitleButtons)
        self.TitleButtonsLayout.setObjectName("TitleButtonsLayout")
        self.MaximizeButton = QPushButton(self.TitleButtons)
        self.MaximizeButton.setObjectName("MaximizeButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.MaximizeButton.sizePolicy().hasHeightForWidth())
        self.MaximizeButton.setSizePolicy(sizePolicy)
        self.MaximizeButton.setMinimumSize(QSize(16, 16))
        self.MaximizeButton.setMaximumSize(QSize(16, 16))
        self.MaximizeButton.setStyleSheet\
        (
            """
            QPushButton
            {
            	background-color: rgb(0, 255, 0);
            	border-radius: 8px;
            }
            QPushButton:hover
            {
            	background-color: rgba(0, 255, 0, 80);
            }
            """
        )
        self.TitleButtonsLayout.addWidget(self.MaximizeButton)
        self.MinimizeButton = QPushButton(self.TitleButtons)
        self.MinimizeButton.setObjectName("MinimizeButton")
        sizePolicy.setHeightForWidth(self.MinimizeButton.sizePolicy().hasHeightForWidth())
        self.MinimizeButton.setSizePolicy(sizePolicy)
        self.MinimizeButton.setMinimumSize(QSize(16, 16))
        self.MinimizeButton.setMaximumSize(QSize(16, 16))
        self.MinimizeButton.setStyleSheet\
        (
            """
            QPushButton
            {
            	background-color:rgb(255, 170, 0);
            	border-radius: 8px;
            }
            QPushButton:hover
            {
            	background-color: rgba(255,170, 0, 80);
            }
            """
        )
        self.TitleButtonsLayout.addWidget(self.MinimizeButton)
        self.CloseButton = QPushButton(self.TitleButtons)
        self.CloseButton.setObjectName("CloseButton")
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMinimumSize(QSize(16, 16))
        self.CloseButton.setMaximumSize(QSize(16, 16))
        self.CloseButton.setStyleSheet\
        (
            """
            QPushButton
            {
                background-color:rgb(255, 0, 0);
                border-radius: 8px;
            }
            QPushButton:hover
            {
                background-color: rgba(255, 0, 0, 80);
            }
            """
        )
        self.TitleButtonsLayout.addWidget(self.CloseButton)
        self.TitleBarLayout.addWidget(self.TitleButtons)
        self.AppLayout.addWidget(self.TitleBar)
        self.AppContentFrame = QFrame(self.AppFrame)
        self.AppContentFrame.setObjectName("AppContentFrame")
        self.AppContentFrame.setStyleSheet("background-color: none;")
        self.AppContentFrame.setFrameShape(QFrame.NoFrame)
        self.AppContentFrame.setFrameShadow(QFrame.Raised)
        self.AppContentLayout = QVBoxLayout(self.AppContentFrame)
        self.AppContentLayout.setSpacing(10)
        self.AppContentLayout.setObjectName("AppContentLayout")
        self.AppContentLayout.setContentsMargins(0, 0, 0, 0)
        self.SettingsFrame = QFrame(self.AppContentFrame)
        self.SettingsFrame.setObjectName("SettingsFrame")
        self.SettingsFrame.setFrameShape(QFrame.StyledPanel)
        self.SettingsFrame.setFrameShadow(QFrame.Raised)
        self.SettingFrameLayout = QVBoxLayout(self.SettingsFrame)
        self.SettingFrameLayout.setSpacing(10)
        self.SettingFrameLayout.setObjectName("SettingFrameLayout")
        self.SettingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.TimeSettingsFrame = QFrame(self.SettingsFrame)
        self.TimeSettingsFrame.setObjectName("TimeSettingsFrame")
        self.TimeSettingsFrame.setFrameShape(QFrame.StyledPanel)
        self.TimeSettingsFrame.setFrameShadow(QFrame.Raised)
        self.TimeSettingFrameLayout = QVBoxLayout(self.TimeSettingsFrame)
        self.TimeSettingFrameLayout.setSpacing(10)
        self.TimeSettingFrameLayout.setObjectName("TimeSettingFrameLayout")
        self.TimeSettingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.FirstRow = QFrame(self.TimeSettingsFrame)
        self.FirstRow.setObjectName("FirstRow")
        self.FirstRow.setFrameShape(QFrame.StyledPanel)
        self.FirstRow.setFrameShadow(QFrame.Raised)
        self.FirstRowLayout = QHBoxLayout(self.FirstRow)
        self.FirstRowLayout.setSpacing(10)
        self.FirstRowLayout.setObjectName("FirstRowLayout")
        self.FirstRowLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.FirstRowLayout.setContentsMargins(10, 0, 10, 0)
        self.MinTimeEntry = QLineEdit(self.FirstRow)
        self.MinTimeEntry.setObjectName("MinTimeEntry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MinTimeEntry.sizePolicy().hasHeightForWidth())
        self.MinTimeEntry.setSizePolicy(sizePolicy1)
        self.MinTimeEntry.setMinimumSize(QSize(380, 35))
        font1 = QFont()
        font1.setFamilies(["Yu Gothic"])
        font1.setPointSize(16)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.MinTimeEntry.setFont(font1)
        self.MinTimeEntry.setStyleSheet\
        (
            """
            color:rgb(85, 85, 127);
            background-color: rgba(38, 97, 139, 100);
            border-radius: 8px;
            """
        )
        self.MinTimeEntry.setInputMethodHints(Qt.ImhDigitsOnly)
        self.MinTimeEntry.setAlignment(Qt.AlignCenter)
        self.FirstRowLayout.addWidget(self.MinTimeEntry)
        self.MaxTimeEntry = QLineEdit(self.FirstRow)
        self.MaxTimeEntry.setObjectName("MaxTimeEntry")
        sizePolicy1.setHeightForWidth(self.MaxTimeEntry.sizePolicy().hasHeightForWidth())
        self.MaxTimeEntry.setSizePolicy(sizePolicy1)
        self.MaxTimeEntry.setMinimumSize(QSize(380, 35))
        self.MaxTimeEntry.setFont(font1)
        self.MaxTimeEntry.setStyleSheet\
        (
            """
            color:rgb(85, 85, 127);
            background-color: rgba(38, 97, 139, 100);
            border-radius: 8px;
            """
        )
        self.MaxTimeEntry.setInputMethodHints(Qt.ImhDigitsOnly)
        self.MaxTimeEntry.setAlignment(Qt.AlignCenter)
        self.FirstRowLayout.addWidget(self.MaxTimeEntry)
        self.TimeSettingFrameLayout.addWidget(self.FirstRow)
        self.MiddleRow = QFrame(self.TimeSettingsFrame)
        self.MiddleRow.setObjectName("MiddleRow")
        self.MiddleRow.setFrameShape(QFrame.StyledPanel)
        self.MiddleRow.setFrameShadow(QFrame.Raised)
        self.MiddleRowLayout = QHBoxLayout(self.MiddleRow)
        self.MiddleRowLayout.setSpacing(10)
        self.MiddleRowLayout.setObjectName("MiddleRowLayout")
        self.MiddleRowLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MiddleRowLayout.setContentsMargins(10, 0, 10, 0)
        self.BreakTimeEntry = QLineEdit(self.MiddleRow)
        self.BreakTimeEntry.setObjectName("BreakTimeEntry")
        sizePolicy1.setHeightForWidth(self.BreakTimeEntry.sizePolicy().hasHeightForWidth())
        self.BreakTimeEntry.setSizePolicy(sizePolicy1)
        self.BreakTimeEntry.setMinimumSize(QSize(380, 35))
        self.BreakTimeEntry.setFont(font1)
        self.BreakTimeEntry.setStyleSheet\
        (
                """
                color:rgb(85, 85, 127);
                background-color: rgba(38, 97, 139, 100);
                border-radius: 8px;
                """
        )
        self.BreakTimeEntry.setInputMethodHints(Qt.ImhDigitsOnly)
        self.BreakTimeEntry.setAlignment(Qt.AlignCenter)
        self.MiddleRowLayout.addWidget(self.BreakTimeEntry)
        self.OverTimeEntry = QLineEdit(self.MiddleRow)
        self.OverTimeEntry.setObjectName("OverTimeEntry")
        sizePolicy1.setHeightForWidth(self.OverTimeEntry.sizePolicy().hasHeightForWidth())
        self.OverTimeEntry.setSizePolicy(sizePolicy1)
        self.OverTimeEntry.setMinimumSize(QSize(380, 35))
        self.OverTimeEntry.setFont(font1)
        self.OverTimeEntry.setStyleSheet\
        (
            """
            color:rgb(85, 85, 127);
            background-color: rgba(38, 97, 139, 100);
            border-radius: 8px;
            """
        )
        self.OverTimeEntry.setInputMethodHints(Qt.ImhDigitsOnly)
        self.OverTimeEntry.setEchoMode(QLineEdit.Normal)
        self.OverTimeEntry.setAlignment(Qt.AlignCenter)
        self.MiddleRowLayout.addWidget(self.OverTimeEntry)
        self.TimeSettingFrameLayout.addWidget(self.MiddleRow)
        self.LastRow = QFrame(self.TimeSettingsFrame)
        self.LastRow.setObjectName("LastRow")
        self.LastRow.setFrameShape(QFrame.StyledPanel)
        self.LastRow.setFrameShadow(QFrame.Raised)
        self.LastRowLayout = QHBoxLayout(self.LastRow)
        self.LastRowLayout.setSpacing(0)
        self.LastRowLayout.setObjectName("LastRowLayout")
        self.LastRowLayout.setContentsMargins(10, 0, 10, 0)
        self.SessionsEntry = QLineEdit(self.LastRow)
        self.SessionsEntry.setObjectName("SessionsEntry")
        sizePolicy1.setHeightForWidth(self.SessionsEntry.sizePolicy().hasHeightForWidth())
        self.SessionsEntry.setSizePolicy(sizePolicy1)
        self.SessionsEntry.setMinimumSize(QSize(385, 35))
        self.SessionsEntry.setFont(font1)
        self.SessionsEntry.setStyleSheet\
        (
            """
            color:rgb(85, 85, 127);
            background-color: rgba(38, 97, 139, 100);
            border-radius: 8px;
            """
        )
        self.SessionsEntry.setInputMethodHints(Qt.ImhDigitsOnly)
        self.SessionsEntry.setAlignment(Qt.AlignCenter)
        self.LastRowLayout.addWidget(self.SessionsEntry)
        self.TimeSettingFrameLayout.addWidget(self.LastRow)
        self.SettingFrameLayout.addWidget(self.TimeSettingsFrame)
        self.ButtonSettings = QFrame(self.SettingsFrame)
        self.ButtonSettings.setObjectName("ButtonSettings")
        self.ButtonSettings.setFrameShape(QFrame.StyledPanel)
        self.ButtonSettings.setFrameShadow(QFrame.Raised)
        self.ButtonSettingsLayout = QHBoxLayout(self.ButtonSettings)
        self.ButtonSettingsLayout.setSpacing(10)
        self.ButtonSettingsLayout.setObjectName("ButtonSettingsLayout")
        self.ButtonSettingsLayout.setContentsMargins(10, 0, 10, 0)
        self.StartStopButton = QPushButton(self.ButtonSettings)
        self.StartStopButton.setObjectName("StartStopButton")
        sizePolicy1.setHeightForWidth(self.StartStopButton.sizePolicy().hasHeightForWidth())
        self.StartStopButton.setSizePolicy(sizePolicy1)
        self.StartStopButton.setMinimumSize(QSize(0, 120))
        self.StartStopButton.setStyleSheet\
        (
            """
            QPushButton
            {
                image: url(./Media/start.png);
                background-color:rgb(20, 147, 158);
            }
            QPushButton:hover
            {
                background-color:rgba(20, 147, 158, 150)
            }
            """
        )
        self.ButtonSettingsLayout.addWidget(self.StartStopButton)
        self.PlayPauseButton = QPushButton(self.ButtonSettings)
        self.PlayPauseButton.setObjectName("PlayPauseButton")
        sizePolicy1.setHeightForWidth(self.PlayPauseButton.sizePolicy().hasHeightForWidth())
        self.PlayPauseButton.setSizePolicy(sizePolicy1)
        self.PlayPauseButton.setMinimumSize(QSize(0, 120))
        self.PlayPauseButton.setStyleSheet\
        (
            """
            QPushButton
            {
                image: url(./Media/pause.png);
            	background-color:rgb(20, 147, 158);
            }
            QPushButton:hover
            {
            	background-color:rgba(20, 147, 158, 150)
            }
            """
        )
        self.ButtonSettingsLayout.addWidget(self.PlayPauseButton)
        self.SkipToBreakButton = QPushButton(self.ButtonSettings)
        self.SkipToBreakButton.setObjectName("SkipToBreakButton")
        sizePolicy1.setHeightForWidth(self.SkipToBreakButton.sizePolicy().hasHeightForWidth())
        self.SkipToBreakButton.setSizePolicy(sizePolicy1)
        self.SkipToBreakButton.setMinimumSize(QSize(0, 120))
        self.SkipToBreakButton.setStyleSheet\
        (
            """
            QPushButton
            {
                image: url(./Media/forward.png);
                background-color:rgb(20, 147, 158);
            }
                QPushButton:hover
            {
            	background-color:rgba(20, 147, 158, 150)
            }
            """
        )
        self.ButtonSettingsLayout.addWidget(self.SkipToBreakButton)
        self.SettingFrameLayout.addWidget(self.ButtonSettings)
        self.AppContentLayout.addWidget(self.SettingsFrame)
        self.TimeDisplayFrame = QFrame(self.AppContentFrame)
        self.TimeDisplayFrame.setObjectName("TimeDisplayFrame")
        self.TimeDisplayFrame.setFrameShape(QFrame.StyledPanel)
        self.TimeDisplayFrame.setFrameShadow(QFrame.Raised)
        self.TimeFrame = QVBoxLayout(self.TimeDisplayFrame)
        self.TimeFrame.setSpacing(0)
        self.TimeFrame.setObjectName("TimeFrame")
        self.TimeFrame.setContentsMargins(10, 0, 10, 0)
        self.TimeDisplay = QLabel(self.TimeDisplayFrame)
        self.TimeDisplay.setObjectName("TimeDisplay")
        sizePolicy1.setHeightForWidth(self.TimeDisplay.sizePolicy().hasHeightForWidth())
        self.TimeDisplay.setSizePolicy(sizePolicy1)
        self.TimeDisplay.setMinimumSize(QSize(0, 265))
        font2 = QFont()
        font2.setFamilies(["Yu Gothic Medium"])
        font2.setPointSize(190)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.TimeDisplay.setFont(font2)
        self.TimeDisplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.TimeDisplay.setStyleSheet\
        (
            """
            color: rgb(255, 255, 255);
            background-color: rgba(38, 97, 139, 100);
            """     
        )
        self.TimeDisplay.setAlignment(Qt.AlignCenter)
        self.TimeDisplay.setIndent(0)
        self.TimeFrame.addWidget(self.TimeDisplay)
        self.AppContentLayout.addWidget(self.TimeDisplayFrame)
        self.AppLayout.addWidget(self.AppContentFrame)
        self.CreditBarFrame = QFrame(self.AppFrame)
        self.CreditBarFrame.setObjectName("CreditBarFrame")
        self.CreditBarFrame.setMaximumSize(QSize(16777215, 30))
        self.CreditBarFrame.setStyleSheet("background-color: none;")
        self.CreditBarFrame.setFrameShape(QFrame.NoFrame)
        self.CreditBarFrame.setFrameShadow(QFrame.Raised)
        self.CreditBarLayout = QHBoxLayout(self.CreditBarFrame)
        self.CreditBarLayout.setSpacing(0)
        self.CreditBarLayout.setObjectName("CreditBarLayout")
        self.CreditBarLayout.setContentsMargins(0, 0, 0, 0)
        self.CreditFrame = QFrame(self.CreditBarFrame)
        self.CreditFrame.setObjectName("CreditFrame")
        self.CreditFrame.setFrameShape(QFrame.StyledPanel)
        self.CreditFrame.setFrameShadow(QFrame.Raised)
        self.InternalCreditFrame = QHBoxLayout(self.CreditFrame)
        self.InternalCreditFrame.setObjectName("InternalCreditFrame")
        self.Credit = QLabel(self.CreditFrame)
        self.Credit.setObjectName("Credit")
        font3 = QFont()
        font3.setFamilies(["Yu Gothic"])
        font3.setPointSize(10)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.Credit.setFont(font3)
        self.Credit.setStyleSheet("color: rgb(0, 0, 127);")
        self.InternalCreditFrame.addWidget(self.Credit)
        self.CreditBarLayout.addWidget(self.CreditFrame)
        self.Resize = QFrame(self.CreditBarFrame)
        self.Resize.setObjectName("Resize")
        self.Resize.setMaximumSize(QSize(30, 30))
        self.Resize.setStyleSheet("")
        self.Resize.setFrameShape(QFrame.StyledPanel)
        self.Resize.setFrameShadow(QFrame.Raised)
        self.ResizeGrip = QSizeGrip(self.Resize)
        self.ResizeGrip.setStyleSheet\
        (
            """
            width: 17px;
            height: 17px;
            background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.282486 rgba(0, 0, 0, 125), stop:0.511364 rgba(255, 255, 255, 0));
            margin: 5px;
            border-radius: 0px 0px 5px 5px;
            """
        )
        self.CreditBarLayout.addWidget(self.Resize)
        self.AppLayout.addWidget(self.CreditBarFrame)
        self.WindowLayout.addWidget(self.AppFrame)
        self.setCentralWidget(self.WindowFrame)
        Validator = QIntValidator()
        Validator.setBottom(0)
        self.MinTimeEntry.setValidator(Validator) # allow the user to enter digits only in the min time entry
        self.MaxTimeEntry.setValidator(Validator) # allow the user to enter digits only in the max time entry
        self.BreakTimeEntry.setValidator(Validator) # allow the user to enter digits only in the break time entry
        self.OverTimeEntry.setValidator(Validator) # allow the user to enter digits only in the over time entry
        self.SessionsEntry.setValidator(Validator) # allow the user to enter digits only in the sessions entry
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self): #set the the translatable text
        _translate = QCoreApplication.translate # translate function
        self.setWindowTitle(_translate("Window", "MainWindow")) # set the window title (window)
        self.Title.setText(_translate("Window", "StudyFlow")) # set the window title (internal)
        self.MinTimeEntry.setPlaceholderText(_translate("Window", "Min.Time (minutes)")) # set the placeholder text on the min time entry
        self.MaxTimeEntry.setPlaceholderText(_translate("Window", "Max.Time (minutes)")) # set the placeholder text on the max time entry
        self.BreakTimeEntry.setPlaceholderText(_translate("Window", "Break Time (minutes)")) # set the placeholder text on the break time entry
        self.OverTimeEntry.setPlaceholderText(_translate("Window", "Over Time (minutes)")) # set the placeholder text on the over time entry
        self.SessionsEntry.setPlaceholderText(_translate("Window", "Sessions")) # set the placeholder text on the sessions entry
        self.TimeDisplay.setText(_translate("Window", "00:00")) # set the initial value of the time display
        self.Credit.setText(_translate("Window", "by: Patrizio S. Onida")) # set the credit text

    def Maximize(self): # this function maximizes the window
        if not self.isMaximized: # check if the window is not maximized
            self.showMaximized() # maximize the window
            self.isMaximized = True # set the window state to maximized
        else: 
            self.showNormal() # unmaximize the window
            self.resize(800, 600) # resize the window to the minimum size
            self.isMaximized = False # set the window state to not maximized
            #self.SetWindowGeometry((800,600)) # resize the window to original size
    
    def MoveWindow(self, Event): # this function 
        if self.isMaximized: # check if the window is not maximized
            self.Maximize() # maximize the window

        if Event.buttons() == Qt.LeftButton: # check if the left button is pressed 
            Movement = QPointF(Event.globalPosition() - self.DragPos) # calculate the delta position of mouse movement
            self.move(self.x() + Movement.x(), self.y() + Movement.y()) # move the window
            self.DragPos = Event.globalPosition() # update the position of the click event

    def mousePressEvent(self, Event): # this function check if the mouse is pressed and save the position of the click event
        self.DragPos = Event.globalPosition() # update the position of the click event

    def ConvertedCounter(self, Counter):# this function convert the counter in time stamp MM:SS 
        Seconds = str(Counter % 60).zfill(2) # get the number of seconds forced to be always 2 digits 
        Minutes = str((Counter - int(Seconds)) // 60).zfill(2) # get the number of minutes forced to be always 2 digits

        return f'{Minutes}:{Seconds}'
    
    def StartStop(self, PlaySound = True): # this function start or stop the sessions the user requested
        if PlaySound: # check if the sound needs to be played
            self.ClickSound.play() # play the click sound

        print('StartStop called')

        if self.InSession: # check if the user is in session state
            self.StartStopButton.setStyleSheet\
            (
                """
                QPushButton
                {
                    image: url(./Media/start.png);
                    background-color:rgb(20, 147, 158);
                }
                QPushButton:hover
                {
                    background-color:rgba(20, 147, 158, 150)
                }
                """
            )
            self.InSession = False # exit the in session state
            self.InCore = False # exit the in core state
            self.InPause = False # exit the in pause state
            self.Counter = 0 # reset the counter
            self.BreakCounter = 0 # reset the break counter
            self.ActiveMinTime = 0 # set minimum time
            self.ActiveMaxTime = 0 # set maximum time
            self.ActiveBreakTime = 0 # set break time
            self.ActiveOverTime = 0 # set over time
            self.ActiveSession = 0 # set sessions repetition
            self.TotalSessions = 0 # set the total session
            self.TotalSessionTime = 0 # set the total time per session
            self.MinTimeEntry.setReadOnly(False) # set the min time entry as editable
            self.MinTimeEntry.setEnabled(True) # enable the focus (to be clicked) on the min time entry
            self.MinTimeEntry.clear() # clear the min time entry
            self.MaxTimeEntry.setReadOnly(False) # set the max time entry as editable
            self.MaxTimeEntry.setEnabled(True) # enable the focus (to be clicked) on the max time entry
            self.MaxTimeEntry.clear() # clear the max time entry
            self.BreakTimeEntry.setReadOnly(False) # set the break time entry as editable
            self.BreakTimeEntry.setEnabled(True) # enable the focus (to be clicked) on the break time entry
            self.BreakTimeEntry.clear() # clear the break time entry
            self.OverTimeEntry.setReadOnly(False) # set the over time entry as editable
            self.OverTimeEntry.setEnabled(True) # enable the focus (to be clicked) on the over time entry
            self.OverTimeEntry.clear() # clear the over time entry
            self.SessionsEntry.setReadOnly(False) # set the sessions entry as editable
            self.SessionsEntry.setEnabled(True) # enable the focus (to be clicked) on the sessions entry
            self.SessionsEntry.clear() # clear the sessions entry

            for _ in range(3):
                self.EndSound.play() # play the end sound
        else: # the user is not in the in session state
            if self.MinTimeEntry.text() != '' and self.MaxTimeEntry.text() != '' and \
            self.BreakTimeEntry.text() != '' and self.OverTimeEntry.text() != '' and self.SessionsEntry.text() != '': # check if the user fill all the required entries
                self.StartStopButton.setStyleSheet\
                (
                    """
                    QPushButton
                    {
                        image: url(./Media/stop.png);
                        background-color:rgb(20, 147, 158);
                    }
                    QPushButton:hover
                    {
                        background-color:rgba(20, 147, 158, 150)
                    }
                    """
                )
                self.InSession = True # set the user in the in session state
                self.InCore = True # set the user in the in core state
                self.Counter = 0 # set the counter to 0
                self.BreakCounter = 0 # set the break counter to 0
                self.ActiveMinTime = int(self.MinTimeEntry.text()) * 60 # set minimum time (in minutes)
                self.ActiveMaxTime = int(self.MaxTimeEntry.text()) * 60 # set maximum time (in minutes)
                self.ActiveMaxTime = self.ActiveMaxTime if self.ActiveMinTime < self.ActiveMaxTime else self.ActiveMinTime + self.ActiveMaxTime # set the max time bigger than the min time
                self.ActiveBreakTime = int(self.BreakTimeEntry.text()) * 60 # set break time (in minutes)
                self.ActiveOverTime = int(self.OverTimeEntry.text()) * 60 # set over time (in minutes)
                self.ActiveOverTime = self.ActiveMaxTime + self.ActiveOverTime if self.ActiveOverTime < self.ActiveMaxTime else self.ActiveOverTime # set the over time bigger than the max time
                self.ActiveSession = 1 # set the actual session
                self.TotalSessions = int(self.SessionsEntry.text()) # set the total session
                self.MinTimeEntry.setReadOnly(True) # make the min time entry read-only
                self.MinTimeEntry.setEnabled(False) # make the min time entry not clickable
                self.MaxTimeEntry.setReadOnly(True) # make the max time entry read-only
                self.MaxTimeEntry.setEnabled(False) # make the max time entry not clickable
                self.BreakTimeEntry.setReadOnly(True) # make the break time entry read-only
                self.BreakTimeEntry.setEnabled(False) # make the break time entry not clickable
                self.OverTimeEntry.setReadOnly(True) # make the over time entry read-only
                self.OverTimeEntry.setEnabled(False) # make the over time entry not clickable
                self.SessionsEntry.setReadOnly(True) # make the sessions entry read-only
                self.SessionsEntry.setEnabled(False) # make the sessions entry not clickable
        
        self.TimeDisplay.setStyleSheet\
        (
            """
            color: rgb(255, 255,255);
            background-color: rgba(38, 97, 139, 100);
            """  
        )
        self.TimeDisplay.setText('00:00') # set the time display as 0
    
    def PlayPause(self, PlaySound = True): # this function reverse the pause state
        if PlaySound: # check if the sound needs to be played
            self.ClickSound.play() # play the click sound
        
        print('PlayPause called')

        if self.InSession: # check if the user is in session
            self.InPause = not self.InPause # reverse the pause state
        
            if self.InPause: # check if the user paused the session
                self.PlayPauseButton.setStyleSheet\
                (
                    """
                    QPushButton
                    {
                        image: url(./Media/play.png);
                        background-color:rgb(20, 147, 158);
                    }
                    QPushButton:hover
                    {
                        background-color:rgba(20, 147, 158, 150)
                    }
                    """
                )
            else: # the user resumed the session
                self.PlayPauseButton.setStyleSheet\
                (
                    """
                    QPushButton
                    {
                        image: url(./Media/pause.png);
                        background-color:rgb(20, 147, 158);
                    }
                    QPushButton:hover
                    {
                        background-color:rgba(20, 147, 158, 150)
                    }
                    """
                )
    
    def SkipToBreak(self, PlaySound = True): # this function allow the user to skip to the break part
        if PlaySound: # check if the sound needs to be played
            self.ClickSound.play() # play the click sound
        
        print('SkipToBreak called')

        if self.InSession: # check if the user is in session state
            if not self.InCore: # check if the user is not in core state
                self.InPause = False # force the user out of the pause state

                if self.InBreak: # check if the user is in the break state
                    self.InBreak = False # force the user out of the break state
                    self.InCore = True # force the user in the core state
                    self.TimeDisplay.setStyleSheet\
                    (
                        """
                        color: rgb(255, 145, 0);
                        background-color: rgba(38, 97, 139, 100);
                        """
                    )
                else: # the user is in out of in break state
                    self.InBreak = True # force the user in the break state
                    self.Counter = 0
                    self.BreakCounter = 0
                    self.TimeDisplay.setStyleSheet\
                    (
                        """
                        color: rgb(79, 224, 0);
                        background-color: rgba(38, 97, 139, 100);
                        """
                    )

                self.TimeDisplay.setText('00:00') # reset the time display

    def Elapse(self): # this function elapse time while checking the state of the user
        if self.InSession: # check if the user is in session state
            if not self.InPause: # check if the user is not in pause state
                if self.Counter < self.ActiveOverTime and not self.InBreak: # check if the user is in the study part
                    self.Counter += 1 # increment the counter
                    if self.Counter == 1:
                        self.TimeDisplay.setStyleSheet\
                        (
                            """
                            color: rgb(255, 145, 0);
                            background-color: rgba(38, 97, 139, 100);
                            """
                        )
                    elif self.Counter == self.ActiveMinTime: # check if the counter is equal the min time (out of in core state)
                        self.InCore = False # set the user off the in core state (allow the user to skip to the break)
                        self.TimeDisplay.setStyleSheet\
                        (
                            """
                            color: rgb(255, 234, 0);
                            background-color: rgba(38, 97, 139, 100);
                            """     
                        )
                        self.PassPhaseSound.play()
                    elif self.Counter == self.ActiveMaxTime: # check if the counter is equal the max time 
                        self.InCore = False # set the user off the in core state (allow the user to skip to the break)
                        self.TimeDisplay.setStyleSheet\
                        (
                            """
                            color: rgb(158, 0, 0);
                            background-color: rgba(38, 97, 139, 100);
                            """     
                        )
                        self.EndSound.play()
                        self.EndSound.play()
                    elif self.Counter == self.ActiveOverTime: # check if the counter is equal the over time
                        self.EndSound.play()
                        self.EndSound.play()
                        self.SkipToBreak(False)
                    
                    self.TimeDisplay.setText(self.ConvertedCounter(self.Counter)) # convert the counter and display it
                else: # the user is in break state
                    if self.BreakCounter < self.ActiveBreakTime: # check if the break counter is greater than the break time
                        self.BreakCounter += 1 # increment the break counter
                        self.TimeDisplay.setText(self.ConvertedCounter(self.BreakCounter)) # convert the break counter and display it
                    else: # the user ended the study part and the break part (next session start)
                        self.ActiveSession += 1 # increment the session counter

                        if self.ActiveSession < self.TotalSessions: # check if the user has sessions to do
                            self.Counter = 0 # reset the counter
                            self.BreakCounter = 0 # reset the break counter
                            self.InCore = True # set the user on the in core state
                            self.Inbreak = False # set the user off the in break state
                            self.InPause = False # set the user on the in pause state
                            self.EndSound.play()
                        else: # the user ended all sessions
                            self.StartStop(False) # stop the program (ready to restart)

if __name__ == '__main__':
    StudyFlow = QApplication([])
    StudyFlow.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    StudyFlow.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    StudyFlowWindow = App()
    Exit(StudyFlow.exec())
