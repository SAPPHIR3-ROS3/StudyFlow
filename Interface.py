# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(800, 600)
        Window.setMinimumSize(QtCore.QSize(800, 600))
        self.WindowFrame = QtWidgets.QWidget(Window)
        self.WindowFrame.setObjectName("WindowFrame")
        self.WindowLayout = QtWidgets.QVBoxLayout(self.WindowFrame)
        self.WindowLayout.setContentsMargins(0, 0, 0, 0)
        self.WindowLayout.setSpacing(0)
        self.WindowLayout.setObjectName("WindowLayout")
        self.AppFrame = QtWidgets.QFrame(self.WindowFrame)
        self.AppFrame.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 250, 221, 255), stop:1 rgba(50, 122, 178, 255));\n"
"border-radius: 15px")
        self.AppFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.AppFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.AppFrame.setObjectName("AppFrame")
        self.AppLayout = QtWidgets.QVBoxLayout(self.AppFrame)
        self.AppLayout.setContentsMargins(0, 0, 0, 0)
        self.AppLayout.setSpacing(0)
        self.AppLayout.setObjectName("AppLayout")
        self.TitleBar = QtWidgets.QFrame(self.AppFrame)
        self.TitleBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.TitleBar.setStyleSheet("background-color: none;")
        self.TitleBar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.TitleBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TitleBar.setObjectName("TitleBar")
        self.TitleBarLayout = QtWidgets.QHBoxLayout(self.TitleBar)
        self.TitleBarLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBarLayout.setSpacing(0)
        self.TitleBarLayout.setObjectName("TitleBarLayout")
        self.TitleArea = QtWidgets.QFrame(self.TitleBar)
        self.TitleArea.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TitleArea.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TitleArea.setObjectName("TitleArea")
        self.TitleLayout = QtWidgets.QHBoxLayout(self.TitleArea)
        self.TitleLayout.setObjectName("TitleLayout")
        self.Title = QtWidgets.QLabel(self.TitleArea)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color:rgb(108, 89, 255);")
        self.Title.setObjectName("Title")
        self.TitleLayout.addWidget(self.Title)
        self.TitleBarLayout.addWidget(self.TitleArea)
        self.TitleButtons = QtWidgets.QFrame(self.TitleBar)
        self.TitleButtons.setMaximumSize(QtCore.QSize(100, 16777215))
        self.TitleButtons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TitleButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TitleButtons.setObjectName("TitleButtons")
        self.TitleButtonsLayout = QtWidgets.QHBoxLayout(self.TitleButtons)
        self.TitleButtonsLayout.setObjectName("TitleButtonsLayout")
        self.MaximizButton = QtWidgets.QPushButton(self.TitleButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.MaximizButton.sizePolicy().hasHeightForWidth())
        self.MaximizButton.setSizePolicy(sizePolicy)
        self.MaximizButton.setMinimumSize(QtCore.QSize(16, 16))
        self.MaximizButton.setMaximumSize(QtCore.QSize(16, 16))
        self.MaximizButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgba(0, 255, 0, 80);\n"
"}")
        self.MaximizButton.setText("")
        self.MaximizButton.setObjectName("MaximizButton")
        self.TitleButtonsLayout.addWidget(self.MaximizButton)
        self.MinimizieButton = QtWidgets.QPushButton(self.TitleButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.MinimizieButton.sizePolicy().hasHeightForWidth())
        self.MinimizieButton.setSizePolicy(sizePolicy)
        self.MinimizieButton.setMinimumSize(QtCore.QSize(16, 16))
        self.MinimizieButton.setMaximumSize(QtCore.QSize(16, 16))
        self.MinimizieButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(255, 170, 0);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgba(255,170, 0, 80);\n"
"}")
        self.MinimizieButton.setText("")
        self.MinimizieButton.setObjectName("MinimizieButton")
        self.TitleButtonsLayout.addWidget(self.MinimizieButton)
        self.CloseButton = QtWidgets.QPushButton(self.TitleButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMinimumSize(QtCore.QSize(16, 16))
        self.CloseButton.setMaximumSize(QtCore.QSize(16, 16))
        self.CloseButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(255, 0, 0);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgba(255, 0, 0, 80);\n"
"}")
        self.CloseButton.setText("")
        self.CloseButton.setObjectName("CloseButton")
        self.TitleButtonsLayout.addWidget(self.CloseButton)
        self.TitleBarLayout.addWidget(self.TitleButtons)
        self.AppLayout.addWidget(self.TitleBar)
        self.AppContentFrame = QtWidgets.QFrame(self.AppFrame)
        self.AppContentFrame.setStyleSheet("background-color: none;")
        self.AppContentFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.AppContentFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.AppContentFrame.setObjectName("AppContentFrame")
        self.AppContentLayout = QtWidgets.QVBoxLayout(self.AppContentFrame)
        self.AppContentLayout.setContentsMargins(0, 0, 0, 0)
        self.AppContentLayout.setSpacing(10)
        self.AppContentLayout.setObjectName("AppContentLayout")
        self.SettingsFrame = QtWidgets.QFrame(self.AppContentFrame)
        self.SettingsFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.SettingsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.SettingsFrame.setObjectName("SettingsFrame")
        self.SettingFrameLayout = QtWidgets.QVBoxLayout(self.SettingsFrame)
        self.SettingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.SettingFrameLayout.setSpacing(10)
        self.SettingFrameLayout.setObjectName("SettingFrameLayout")
        self.TimeSettingsFrame = QtWidgets.QFrame(self.SettingsFrame)
        self.TimeSettingsFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TimeSettingsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TimeSettingsFrame.setObjectName("TimeSettingsFrame")
        self.TimeSettingFrameLayout = QtWidgets.QVBoxLayout(self.TimeSettingsFrame)
        self.TimeSettingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.TimeSettingFrameLayout.setSpacing(5)
        self.TimeSettingFrameLayout.setObjectName("TimeSettingFrameLayout")
        self.FirstRow = QtWidgets.QFrame(self.TimeSettingsFrame)
        self.FirstRow.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.FirstRow.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.FirstRow.setObjectName("FirstRow")
        self.FirstRowLayout = QtWidgets.QHBoxLayout(self.FirstRow)
        self.FirstRowLayout.setContentsMargins(10, 0, 10, 0)
        self.FirstRowLayout.setSpacing(5)
        self.FirstRowLayout.setObjectName("FirstRowLayout")
        self.MinTimeEntry = QtWidgets.QLineEdit(self.FirstRow)
        self.MinTimeEntry.setMinimumSize(QtCore.QSize(380, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.MinTimeEntry.setFont(font)
        self.MinTimeEntry.setStyleSheet("color:rgb(85, 85, 127);\n"
"background-color: rgba(38, 97, 139, 100);\n"
"border-radius: 8px;")
        self.MinTimeEntry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MinTimeEntry.setObjectName("MinTimeEntry")
        self.FirstRowLayout.addWidget(self.MinTimeEntry)
        self.MaxTimeEntry = QtWidgets.QLineEdit(self.FirstRow)
        self.MaxTimeEntry.setMinimumSize(QtCore.QSize(380, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.MaxTimeEntry.setFont(font)
        self.MaxTimeEntry.setStyleSheet("color:rgb(85, 85, 127);\n"
"background-color: rgba(38, 97, 139, 100);\n"
"border-radius: 8px;")
        self.MaxTimeEntry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MaxTimeEntry.setObjectName("MaxTimeEntry")
        self.FirstRowLayout.addWidget(self.MaxTimeEntry)
        self.TimeSettingFrameLayout.addWidget(self.FirstRow)
        self.MIddleRow = QtWidgets.QFrame(self.TimeSettingsFrame)
        self.MIddleRow.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MIddleRow.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MIddleRow.setObjectName("MIddleRow")
        self.MIddleRowLayout = QtWidgets.QHBoxLayout(self.MIddleRow)
        self.MIddleRowLayout.setContentsMargins(10, 0, 10, 0)
        self.MIddleRowLayout.setSpacing(5)
        self.MIddleRowLayout.setObjectName("MIddleRowLayout")
        self.BreakTimeEntry = QtWidgets.QLineEdit(self.MIddleRow)
        self.BreakTimeEntry.setMinimumSize(QtCore.QSize(380, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.BreakTimeEntry.setFont(font)
        self.BreakTimeEntry.setStyleSheet("color:rgb(85, 85, 127);\n"
"background-color: rgba(38, 97, 139, 100);\n"
"border-radius: 8px;")
        self.BreakTimeEntry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.BreakTimeEntry.setObjectName("BreakTimeEntry")
        self.MIddleRowLayout.addWidget(self.BreakTimeEntry)
        self.OverTimeEntry = QtWidgets.QLineEdit(self.MIddleRow)
        self.OverTimeEntry.setMinimumSize(QtCore.QSize(380, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.OverTimeEntry.setFont(font)
        self.OverTimeEntry.setStyleSheet("color:rgb(85, 85, 127);\n"
"background-color: rgba(38, 97, 139, 100);\n"
"border-radius: 8px;")
        self.OverTimeEntry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.OverTimeEntry.setObjectName("OverTimeEntry")
        self.MIddleRowLayout.addWidget(self.OverTimeEntry)
        self.TimeSettingFrameLayout.addWidget(self.MIddleRow)
        self.LastRow = QtWidgets.QFrame(self.TimeSettingsFrame)
        self.LastRow.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.LastRow.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.LastRow.setObjectName("LastRow")
        self.LastRowLayout = QtWidgets.QHBoxLayout(self.LastRow)
        self.LastRowLayout.setContentsMargins(0, 0, 0, 0)
        self.LastRowLayout.setSpacing(5)
        self.LastRowLayout.setObjectName("LastRowLayout")
        self.SessionsEntry = QtWidgets.QLineEdit(self.LastRow)
        self.SessionsEntry.setMinimumSize(QtCore.QSize(385, 35))
        self.SessionsEntry.setMaximumSize(QtCore.QSize(385, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.SessionsEntry.setFont(font)
        self.SessionsEntry.setStyleSheet("color:rgb(85, 85, 127);\n"
"background-color: rgba(38, 97, 139, 100);\n"
"border-radius: 8px;")
        self.SessionsEntry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SessionsEntry.setObjectName("SessionsEntry")
        self.LastRowLayout.addWidget(self.SessionsEntry)
        self.TimeSettingFrameLayout.addWidget(self.LastRow)
        self.SettingFrameLayout.addWidget(self.TimeSettingsFrame)
        self.ButtonSettings = QtWidgets.QFrame(self.SettingsFrame)
        self.ButtonSettings.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ButtonSettings.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ButtonSettings.setObjectName("ButtonSettings")
        self.ButtonSettingsLayout = QtWidgets.QHBoxLayout(self.ButtonSettings)
        self.ButtonSettingsLayout.setContentsMargins(10, 0, 10, 0)
        self.ButtonSettingsLayout.setSpacing(10)
        self.ButtonSettingsLayout.setObjectName("ButtonSettingsLayout")
        self.StartStopButton = QtWidgets.QPushButton(self.ButtonSettings)
        self.StartStopButton.setMinimumSize(QtCore.QSize(0, 120))
        self.StartStopButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(20, 147, 158);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgba(20, 147, 158, 150)\n"
"}")
        self.StartStopButton.setText("")
        self.StartStopButton.setObjectName("StartStopButton")
        self.ButtonSettingsLayout.addWidget(self.StartStopButton)
        self.PlayPauseButton = QtWidgets.QPushButton(self.ButtonSettings)
        self.PlayPauseButton.setMinimumSize(QtCore.QSize(0, 120))
        self.PlayPauseButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(20, 147, 158);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgba(20, 147, 158, 150)\n"
"}")
        self.PlayPauseButton.setText("")
        self.PlayPauseButton.setObjectName("PlayPauseButton")
        self.ButtonSettingsLayout.addWidget(self.PlayPauseButton)
        self.SkipToBreakButton = QtWidgets.QPushButton(self.ButtonSettings)
        self.SkipToBreakButton.setMinimumSize(QtCore.QSize(0, 120))
        self.SkipToBreakButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(20, 147, 158);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgba(20, 147, 158, 150)\n"
"}")
        self.SkipToBreakButton.setText("")
        self.SkipToBreakButton.setObjectName("SkipToBreakButton")
        self.ButtonSettingsLayout.addWidget(self.SkipToBreakButton)
        self.SettingFrameLayout.addWidget(self.ButtonSettings)
        self.AppContentLayout.addWidget(self.SettingsFrame)
        self.TimeDysplayFrame = QtWidgets.QFrame(self.AppContentFrame)
        self.TimeDysplayFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TimeDysplayFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TimeDysplayFrame.setObjectName("TimeDysplayFrame")
        self.TimeFrame = QtWidgets.QVBoxLayout(self.TimeDysplayFrame)
        self.TimeFrame.setContentsMargins(10, 0, 10, 0)
        self.TimeFrame.setSpacing(0)
        self.TimeFrame.setObjectName("TimeFrame")
        self.TimeDysplay = QtWidgets.QLabel(self.TimeDysplayFrame)
        self.TimeDysplay.setMinimumSize(QtCore.QSize(0, 265))
        self.TimeDysplay.setMaximumSize(QtCore.QSize(16777215, 265))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(190)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.TimeDysplay.setFont(font)
        self.TimeDysplay.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(38, 97, 139, 100);")
        self.TimeDysplay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TimeDysplay.setObjectName("TimeDysplay")
        self.TimeFrame.addWidget(self.TimeDysplay)
        self.AppContentLayout.addWidget(self.TimeDysplayFrame)
        self.AppLayout.addWidget(self.AppContentFrame)
        self.CreditBarFrame = QtWidgets.QFrame(self.AppFrame)
        self.CreditBarFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.CreditBarFrame.setStyleSheet("background-color: none;")
        self.CreditBarFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.CreditBarFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.CreditBarFrame.setObjectName("CreditBarFrame")
        self.CreditBarLayout = QtWidgets.QHBoxLayout(self.CreditBarFrame)
        self.CreditBarLayout.setContentsMargins(0, 0, 0, 0)
        self.CreditBarLayout.setSpacing(0)
        self.CreditBarLayout.setObjectName("CreditBarLayout")
        self.CreditFrame = QtWidgets.QFrame(self.CreditBarFrame)
        self.CreditFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.CreditFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.CreditFrame.setObjectName("CreditFrame")
        self.InternalCreditFrame = QtWidgets.QHBoxLayout(self.CreditFrame)
        self.InternalCreditFrame.setObjectName("InternalCreditFrame")
        self.Credit = QtWidgets.QLabel(self.CreditFrame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.Credit.setFont(font)
        self.Credit.setStyleSheet("color: rgb(0, 0, 127);")
        self.Credit.setObjectName("Credit")
        self.InternalCreditFrame.addWidget(self.Credit)
        self.CreditBarLayout.addWidget(self.CreditFrame)
        self.Resize = QtWidgets.QFrame(self.CreditBarFrame)
        self.Resize.setMaximumSize(QtCore.QSize(30, 30))
        self.Resize.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Resize.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Resize.setObjectName("Resize")
        self.CreditBarLayout.addWidget(self.Resize)
        self.AppLayout.addWidget(self.CreditBarFrame)
        self.WindowLayout.addWidget(self.AppFrame)
        Window.setCentralWidget(self.WindowFrame)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.Title.setText(_translate("Window", "StudyFlow"))
        self.MinTimeEntry.setPlaceholderText(_translate("Window", "Min.Time (minutes)"))
        self.MaxTimeEntry.setPlaceholderText(_translate("Window", "Max.Time (minutes)"))
        self.BreakTimeEntry.setPlaceholderText(_translate("Window", "Break Time (minutes)"))
        self.OverTimeEntry.setPlaceholderText(_translate("Window", "Over Time (minutes)"))
        self.SessionsEntry.setPlaceholderText(_translate("Window", "Sessions"))
        self.TimeDysplay.setText(_translate("Window", "00:00"))
        self.Credit.setText(_translate("Window", "by: Patrizio S. Onida"))
