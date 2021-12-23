from types import LambdaType
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QFile
from PySide6.QtGui import QFont
from PySide6.QtCore import QIODevice
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from sys import exit as Exit

class App(QMainWindow):
    def __init__(self): # constructor
        super(App, self).__init__() # super constructor
        print('super initialized')
        self.isMaximized = False
        self.GUI()
        # self.setWindowFlag(Qt.FramelessWindowHint) # remove the title bar from the window
        # self.setAttribute(Qt.WA_TranslucentBackground) # make the window transparent
        # print('Window set')
        self.CloseButton.clicked.connect(lambda: self.close())
        self.MaximizeButton.clicked.connect(lambda: self.Maximize())
        # self.TitleBar.mouseMoveEvent = self.MoveWindow
        self.show() # show the window

    def SetWindowGeometry(self, Size = tuple(), Position = (-1, -1)): # set the window position and size
        if Position == (-1, -1):
            Screen = self.primaryScreen().size()
            self.setGeometry((Screen.width() - Size[0])//2, (Screen.height() - Size[1])//2, Size[0], Size[1])
        else:
            self.setGeometry(Position[0], Position[1], Size[0], Size[1])
        
    def GUI(self):
        self.setObjectName("Window")
        self.resize(800, 600)
        self.setMinimumSize(QSize(800, 600))
        self.WindowFrame = QWidget(self)
        self.WindowFrame.setObjectName("WindowFrame")
        self.WindowLayout = QVBoxLayout(self.WindowFrame)
        self.WindowLayout.setContentsMargins(0, 0, 0, 0)
        self.WindowLayout.setSpacing(0)
        self.WindowLayout.setObjectName("WindowLayout")
        self.AppFrame = QFrame(self.WindowFrame)
        self.AppFrame.setStyleSheet\
            (
                """
                background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 250, 221, 255), stop:1 rgba(50, 122, 178, 255));
                border-radius: 15px
                """
            )
        self.AppFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.AppFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.AppFrame.setObjectName("AppFrame")
        self.AppLayout = QVBoxLayout(self.AppFrame)
        self.AppLayout.setContentsMargins(0, 0, 0, 0)
        self.AppLayout.setSpacing(0)
        self.AppLayout.setObjectName("AppLayout")
        self.TitleBar = QFrame(self.AppFrame)
        self.TitleBar.setMaximumSize(QSize(16777215, 40))
        self.TitleBar.setStyleSheet("background-color: none;")
        self.TitleBar.setFrameShape(QFrame.Shape.NoFrame)
        self.TitleBar.setFrameShadow(QFrame.Shadow.Raised)
        self.TitleBar.setObjectName("TitleBar")
        self.TitleBarLayout = QHBoxLayout(self.TitleBar)
        self.TitleBarLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBarLayout.setSpacing(0)
        self.TitleBarLayout.setObjectName("TitleBarLayout")
        self.TitleArea = QFrame(self.TitleBar)
        self.TitleArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.TitleArea.setFrameShadow(QFrame.Shadow.Raised)
        self.TitleArea.setObjectName("TitleArea")
        self.TitleLayout = QHBoxLayout(self.TitleArea)
        self.TitleLayout.setObjectName("TitleLayout")
        self.Title = QLabel(self.TitleArea)
        font = QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(18)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color:rgb(108, 89, 255);")
        self.Title.setObjectName("Title")
        self.TitleLayout.addWidget(self.Title)
        self.TitleBarLayout.addWidget(self.TitleArea)
        self.TitleButtons = QFrame(self.TitleBar)
        self.TitleButtons.setMaximumSize(QSize(100, 16777215))
        self.TitleButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.TitleButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.TitleButtons.setObjectName("TitleButtons")
        self.TitleButtonsLayout = QHBoxLayout(self.TitleButtons)
        self.TitleButtonsLayout.setObjectName("TitleButtonsLayout")
        self.MaximizeButton = QPushButton(self.TitleButtons)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
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
                    border-radius: 8px
                }
                QPushButton:hover
                {
                    background-color: rgba(0, 255, 0, 80);
                }
                """
            )
        self.MaximizeButton.setText("")
        self.MaximizeButton.setObjectName("MaximizeButton")
        self.TitleButtonsLayout.addWidget(self.MaximizeButton)
        self.MinimizieButton = QPushButton(self.TitleButtons)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.MinimizieButton.sizePolicy().hasHeightForWidth())
        self.MinimizieButton.setSizePolicy(sizePolicy)
        self.MinimizieButton.setMinimumSize(QSize(16, 16))
        self.MinimizieButton.setMaximumSize(QSize(16, 16))
        self.MinimizieButton.setStyleSheet\
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
        self.MinimizieButton.setText("")
        self.MinimizieButton.setObjectName("MinimizieButton")
        self.TitleButtonsLayout.addWidget(self.MinimizieButton)
        self.CloseButton = QPushButton(self.TitleButtons)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
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
        self.CloseButton.setText("")
        self.CloseButton.setObjectName("CloseButton")
        self.TitleButtonsLayout.addWidget(self.CloseButton)
        self.TitleBarLayout.addWidget(self.TitleButtons)
        self.AppLayout.addWidget(self.TitleBar)
        self.AppContentFrame = QFrame(self.AppFrame)
        self.AppContentFrame.setStyleSheet("background-color: none;")
        self.AppContentFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.AppContentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.AppContentFrame.setObjectName("AppContentFrame")
        self.AppContentLayout = QVBoxLayout(self.AppContentFrame)
        self.AppContentLayout.setContentsMargins(0, 0, 0, 0)
        self.AppContentLayout.setSpacing(10)
        self.AppContentLayout.setObjectName("AppContentLayout")
        self.SettingsFrame = QFrame(self.AppContentFrame)
        self.SettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.SettingsFrame.setObjectName("SettingsFrame")
        self.SettingFrameLayout = QVBoxLayout(self.SettingsFrame)
        self.SettingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.SettingFrameLayout.setSpacing(10)
        self.SettingFrameLayout.setObjectName("SettingFrameLayout")
        self.TimeSettingsFrame = QFrame(self.SettingsFrame)
        self.TimeSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.TimeSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.TimeSettingsFrame.setObjectName("TimeSettingsFrame")
        self.TimeSettingFrameLayout = QVBoxLayout(self.TimeSettingsFrame)
        self.TimeSettingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.TimeSettingFrameLayout.setSpacing(5)
        self.TimeSettingFrameLayout.setObjectName("TimeSettingFrameLayout")
        self.FirstRow = QFrame(self.TimeSettingsFrame)
        self.FirstRow.setFrameShape(QFrame.Shape.StyledPanel)
        self.FirstRow.setFrameShadow(QFrame.Shadow.Raised)
        self.FirstRow.setObjectName("FirstRow")
        self.FirstRowLayout = QHBoxLayout(self.FirstRow)
        self.FirstRowLayout.setContentsMargins(10, 0, 10, 0)
        self.FirstRowLayout.setSpacing(5)
        self.FirstRowLayout.setObjectName("FirstRowLayout")
        self.MinTimeEntry = QLineEdit(self.FirstRow)
        self.MinTimeEntry.setMinimumSize(QSize(380, 35))
        font = QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.MinTimeEntry.setFont(font)
        self.MinTimeEntry.setStyleSheet\
            (
                """
                color:rgb(85, 85, 127);
                background-color: rgba(38, 97, 139, 100);
                border-radius: 8px;
                """
            )
        self.MinTimeEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MinTimeEntry.setObjectName("MinTimeEntry")
        self.FirstRowLayout.addWidget(self.MinTimeEntry)
        self.MaxTimeEntry = QLineEdit(self.FirstRow)
        self.MaxTimeEntry.setMinimumSize(QSize(380, 35))
        font = QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.MaxTimeEntry.setFont(font)
        self.MaxTimeEntry.setStyleSheet\
            (
                """
                color:rgb(85, 85, 127);
                background-color: rgba(38, 97, 139, 100);
                border-radius: 8px;
                """
            )
        self.MaxTimeEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MaxTimeEntry.setObjectName("MaxTimeEntry")
        self.FirstRowLayout.addWidget(self.MaxTimeEntry)
        self.TimeSettingFrameLayout.addWidget(self.FirstRow)
        self.MIddleRow = QFrame(self.TimeSettingsFrame)
        self.MIddleRow.setFrameShape(QFrame.Shape.StyledPanel)
        self.MIddleRow.setFrameShadow(QFrame.Shadow.Raised)
        self.MIddleRow.setObjectName("MIddleRow")
        self.MIddleRowLayout = QHBoxLayout(self.MIddleRow)
        self.MIddleRowLayout.setContentsMargins(10, 0, 10, 0)
        self.MIddleRowLayout.setSpacing(5)
        self.MIddleRowLayout.setObjectName("MIddleRowLayout")
        self.BreakTimeEntry = QLineEdit(self.MIddleRow)
        self.BreakTimeEntry.setMinimumSize(QSize(380, 35))
        font = QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.BreakTimeEntry.setFont(font)
        self.BreakTimeEntry.setStyleSheet\
            (
                """
                color:rgb(85, 85, 127);
                background-color: rgba(38, 97, 139, 100);
                border-radius: 8px;
                """
            )
        self.BreakTimeEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BreakTimeEntry.setObjectName("BreakTimeEntry")
        self.MIddleRowLayout.addWidget(self.BreakTimeEntry)
        self.OverTimeEntry = QLineEdit(self.MIddleRow)
        self.OverTimeEntry.setMinimumSize(QSize(380, 35))
        font = QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.OverTimeEntry.setFont(font)
        self.OverTimeEntry.setStyleSheet\
            (
                """
                color:rgb(85, 85, 127);
                background-color: rgba(38, 97, 139, 100);
                border-radius: 8px;
                """
            )
        self.OverTimeEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.OverTimeEntry.setObjectName("OverTimeEntry")
        self.MIddleRowLayout.addWidget(self.OverTimeEntry)
        self.TimeSettingFrameLayout.addWidget(self.MIddleRow)
        self.LastRow = QFrame(self.TimeSettingsFrame)
        self.LastRow.setFrameShape(QFrame.Shape.StyledPanel)
        self.LastRow.setFrameShadow(QFrame.Shadow.Raised)
        self.LastRow.setObjectName("LastRow")
        self.LastRowLayout = QHBoxLayout(self.LastRow)
        self.LastRowLayout.setContentsMargins(0, 0, 0, 0)
        self.LastRowLayout.setSpacing(5)
        self.LastRowLayout.setObjectName("LastRowLayout")
        self.SessionsEntry = QLineEdit(self.LastRow)
        self.SessionsEntry.setMinimumSize(QSize(385, 35))
        self.SessionsEntry.setMaximumSize(QSize(385, 35))
        font = QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.SessionsEntry.setFont(font)
        self.SessionsEntry.setStyleSheet\
            (
                """
                color:rgb(85, 85, 127);
                background-color: rgba(38, 97, 139, 100);
                border-radius: 8px;
                """
            )
        self.SessionsEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SessionsEntry.setObjectName("SessionsEntry")
        self.LastRowLayout.addWidget(self.SessionsEntry)
        self.TimeSettingFrameLayout.addWidget(self.LastRow)
        self.SettingFrameLayout.addWidget(self.TimeSettingsFrame)
        self.ButtonSettings = QFrame(self.SettingsFrame)
        self.ButtonSettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.ButtonSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.ButtonSettings.setObjectName("ButtonSettings")
        self.ButtonSettingsLayout = QHBoxLayout(self.ButtonSettings)
        self.ButtonSettingsLayout.setContentsMargins(10, 0, 10, 0)
        self.ButtonSettingsLayout.setSpacing(10)
        self.ButtonSettingsLayout.setObjectName("ButtonSettingsLayout")
        self.StartStopButton = QPushButton(self.ButtonSettings)
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
                    background-color:rgba(20, 147, 158, 150);
                }
                """
            )
        self.StartStopButton.setText("")
        self.StartStopButton.setObjectName("StartStopButton")
        self.ButtonSettingsLayout.addWidget(self.StartStopButton)
        self.PlayPauseButton = QPushButton(self.ButtonSettings)
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
                    background-color:rgba(20, 147, 158, 150);
                }
                """
            )
        self.PlayPauseButton.setText("")
        self.PlayPauseButton.setObjectName("PlayPauseButton")
        self.ButtonSettingsLayout.addWidget(self.PlayPauseButton)
        self.SkipToBreakButton = QPushButton(self.ButtonSettings)
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
                    background-color:rgba(20, 147, 158, 150);
                }
                """
            )
        self.SkipToBreakButton.setText("")
        self.SkipToBreakButton.setObjectName("SkipToBreakButton")
        self.ButtonSettingsLayout.addWidget(self.SkipToBreakButton)
        self.SettingFrameLayout.addWidget(self.ButtonSettings)
        self.AppContentLayout.addWidget(self.SettingsFrame)
        self.TimeDysplayFrame = QFrame(self.AppContentFrame)
        self.TimeDysplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.TimeDysplayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.TimeDysplayFrame.setObjectName("TimeDysplayFrame")
        self.TimeFrame = QVBoxLayout(self.TimeDysplayFrame)
        self.TimeFrame.setContentsMargins(10, 0, 10, 0)
        self.TimeFrame.setSpacing(0)
        self.TimeFrame.setObjectName("TimeFrame")
        self.TimeDysplay = QLabel(self.TimeDysplayFrame)
        self.TimeDysplay.setMinimumSize(QSize(0, 265))
        self.TimeDysplay.setMaximumSize(QSize(16777215, 265))
        font = QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(190)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.TimeDysplay.setFont(font)
        self.TimeDysplay.setStyleSheet\
            (
                """
                color: rgb(255, 255, 255);
                background-color: rgba(38, 97, 139, 100);
                """
            )
        self.TimeDysplay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TimeDysplay.setObjectName("TimeDysplay")
        self.TimeFrame.addWidget(self.TimeDysplay)
        self.AppContentLayout.addWidget(self.TimeDysplayFrame)
        self.AppLayout.addWidget(self.AppContentFrame)
        self.CreditBarFrame = QFrame(self.AppFrame)
        self.CreditBarFrame.setMaximumSize(QSize(16777215, 30))
        self.CreditBarFrame.setStyleSheet("background-color: none;")
        self.CreditBarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.CreditBarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.CreditBarFrame.setObjectName("CreditBarFrame")
        self.CreditBarLayout = QHBoxLayout(self.CreditBarFrame)
        self.CreditBarLayout.setContentsMargins(0, 0, 0, 0)
        self.CreditBarLayout.setSpacing(0)
        self.CreditBarLayout.setObjectName("CreditBarLayout")
        self.CreditFrame = QFrame(self.CreditBarFrame)
        self.CreditFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.CreditFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.CreditFrame.setObjectName("CreditFrame")
        self.InternalCreditFrame = QHBoxLayout(self.CreditFrame)
        self.InternalCreditFrame.setObjectName("InternalCreditFrame")
        self.Credit = QLabel(self.CreditFrame)
        font = QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.Credit.setFont(font)
        self.Credit.setStyleSheet("color: rgb(0, 0, 127);")
        self.Credit.setObjectName("Credit")
        self.InternalCreditFrame.addWidget(self.Credit)
        self.CreditBarLayout.addWidget(self.CreditFrame)
        self.Resize = QFrame(self.CreditBarFrame)
        self.Resize.setMaximumSize(QSize(30, 30))
        self.Resize.setFrameShape(QFrame.Shape.StyledPanel)
        self.Resize.setFrameShadow(QFrame.Shadow.Raised)
        self.Resize.setObjectName("Resize")
        self.CreditBarLayout.addWidget(self.Resize)
        self.AppLayout.addWidget(self.CreditBarFrame)
        self.WindowLayout.addWidget(self.AppFrame)
        self.setCentralWidget(self.WindowFrame)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Window", "MainWindow"))
        self.Title.setText(_translate("Window", "StudyFlow"))
        self.MinTimeEntry.setPlaceholderText(_translate("Window", "Min.Time (minutes)"))
        self.MaxTimeEntry.setPlaceholderText(_translate("Window", "Max.Time (minutes)"))
        self.BreakTimeEntry.setPlaceholderText(_translate("Window", "Break Time (minutes)"))
        self.OverTimeEntry.setPlaceholderText(_translate("Window", "Over Time (minutes)"))
        self.SessionsEntry.setPlaceholderText(_translate("Window", "Sessions"))
        self.TimeDysplay.setText(_translate("Window", "00:00"))
        self.Credit.setText(_translate("Window", "by: Patrizio S. Onida"))

    def Maximize(self): # this function maximizes the window
        print('Maximizing window')
        if not self.isMaximized: # check if the window is not maximized
            self.showMaximized() # maximize the window
            self.isMaximized = True # set the window state to maximized
        else: 
            self.showNormal() # unmaximize the window
            self.SetWindowGeometry() # resize the window to original size
            self.isMaximized = False # set the window state to not maximized
    
    def MoveWindow(self, Event): # this function allows you to move the window
        print('Moving window')
        if self.isMaximized: # check if the window is not maximized
            self.Maximize()
        
        if Event.buttons() == Qt.LeftButton:
            self.Window.move(self.Window.pos() + Event.globalPos() - self.Window.dragPos)
            self.Window.dragPos = Event.globalPos()
            Event.accept()

if __name__ == '__main__':
    
    StudyFlow = QApplication([])
    StudyFlow.setAttribute(Qt.AA_ShareOpenGLContexts)
    StudyFlowWindow = App()
    Exit(StudyFlow.exec())
