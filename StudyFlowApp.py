from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QFile
from PySide6.QtGui import QFont
from PySide6.QtGui import QScreen
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QPointF
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
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
from sys import exc_info
import traceback

class App(QMainWindow):
    def __init__(self): # constructor
        super(App, self).__init__() # super constructor
        self.isMaximized = False
        self.DragPos = QPointF(0, 0) # Start position of mouse for the Window
        self.Screen = QScreen()
        self.GUI() # GUI initialization
        self.TitleBar.mouseMoveEvent = self.MoveWindow
        self.ResizeGrip = QSizeGrip(self.Resize)
        #self.ResizeGrip.setStyle(QStyleFactory['Fusion'])
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
        self.setWindowFlag(Qt.FramelessWindowHint) # remove the title bar from the window
        self.setAttribute(Qt.WA_TranslucentBackground) # make the window transparent
        self.CloseButton.clicked.connect(lambda: self.close()) # link the close button to close function
        self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        self.MaximizeButton.clicked.connect(lambda: self.Maximize()) # link the minimize button to minimize function
        self.show() # show the window

    def SetWindowGeometry(self, Size = tuple(), Position = (-1, -1)): # set the window position and size
        if Position == (-1, -1): # check if position is default(centered)
            Screen = QScreen().availableSize() # get the screen size
            self.resize(Size) # resize the window
            #self.setGeometry((Screen.width() - Size[0])//2, (Screen.height() - Size[1])//2, Size[0], Size[1]) # resize the window
        else:
            self.setGeometry(Position[0], Position[1], Size[0], Size[1]) # resize the window
        
    def GUI(self):
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
        self.TimeSettingFrameLayout.setSpacing(5)
        self.TimeSettingFrameLayout.setObjectName("TimeSettingFrameLayout")
        self.TimeSettingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.FirstRow = QFrame(self.TimeSettingsFrame)
        self.FirstRow.setObjectName("FirstRow")
        self.FirstRow.setFrameShape(QFrame.StyledPanel)
        self.FirstRow.setFrameShadow(QFrame.Raised)
        self.FirstRowLayout = QHBoxLayout(self.FirstRow)
        self.FirstRowLayout.setSpacing(5)
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
        self.MIddleRowLayout = QHBoxLayout(self.MiddleRow)
        self.MIddleRowLayout.setSpacing(5)
        self.MIddleRowLayout.setObjectName("MIddleRowLayout")
        self.MIddleRowLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MIddleRowLayout.setContentsMargins(10, 0, 10, 0)
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
        self.MIddleRowLayout.addWidget(self.BreakTimeEntry)
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
        self.MIddleRowLayout.addWidget(self.OverTimeEntry)
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
        self.TimeDysplayFrame = QFrame(self.AppContentFrame)
        self.TimeDysplayFrame.setObjectName("TimeDysplayFrame")
        self.TimeDysplayFrame.setFrameShape(QFrame.StyledPanel)
        self.TimeDysplayFrame.setFrameShadow(QFrame.Raised)
        self.TimeFrame = QVBoxLayout(self.TimeDysplayFrame)
        self.TimeFrame.setSpacing(0)
        self.TimeFrame.setObjectName("TimeFrame")
        self.TimeFrame.setContentsMargins(10, 0, 10, 0)
        self.TimeDysplay = QLabel(self.TimeDysplayFrame)
        self.TimeDysplay.setObjectName("TimeDysplay")
        sizePolicy1.setHeightForWidth(self.TimeDysplay.sizePolicy().hasHeightForWidth())
        self.TimeDysplay.setSizePolicy(sizePolicy1)
        self.TimeDysplay.setMinimumSize(QSize(0, 265))
        font2 = QFont()
        font2.setFamilies(["Yu Gothic Medium"])
        font2.setPointSize(190)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.TimeDysplay.setFont(font2)
        self.TimeDysplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.TimeDysplay.setStyleSheet\
        (
            """
            color: rgb(255, 255, 255);
            background-color: rgba(38, 97, 139, 100);
            """     
        )
        self.TimeDysplay.setAlignment(Qt.AlignCenter)
        self.TimeDysplay.setIndent(0)
        self.TimeFrame.addWidget(self.TimeDysplay)
        self.AppContentLayout.addWidget(self.TimeDysplayFrame)
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
        self.CreditBarLayout.addWidget(self.Resize)
        self.AppLayout.addWidget(self.CreditBarFrame)
        self.WindowLayout.addWidget(self.AppFrame)
        self.setCentralWidget(self.WindowFrame)
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
        self.TimeDysplay.setText(_translate("Window", "00:00")) # set the initial value of the time display
        self.Credit.setText(_translate("Window", "by: Patrizio S. Onida")) # set the credit text

    def Maximize(self): # this function maximizes the window
        print('Maximizing window')
        if not self.isMaximized: # check if the window is not maximized
            self.showMaximized() # maximize the window
            self.isMaximized = True # set the window state to maximized
        else: 
            self.showNormal() # unmaximize the window
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

if __name__ == '__main__':
    StudyFlow = QApplication([])
    StudyFlow.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    StudyFlow.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    StudyFlowWindow = App()
    Exit(StudyFlow.exec())
