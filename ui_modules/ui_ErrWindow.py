from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialog
from ui_modules.sampleWindow import SampleDialog
from ui_modules.ui.err import UiErrWindow


class ErrWindow(SampleDialog, UiErrWindow):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.titleWindowLoad()
        self.nameButton = None

        self.player = QMediaPlayer()
        self.sound = QMediaContent(QtCore.QUrl.fromLocalFile('resources/sound/err.wav'))
        self.player.setMedia(self.sound)

        self.buttonBox.clicked.connect(self.__buttonPress)
        self.pushButton_close.clicked.connect(self.__closeButtonAction)

    def __closeButtonAction(self):
        self.nameButton = 'close'

    def __showWind(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.resize(self.minimumSizeHint())
        self.player.play()
        self.exec_()

    def setData(self, title: str = 'Не указано', text: str = 'Не указано', button: list = [], titleWind: str = 'Ошибка'):
        self.label.setText(title)
        self.label_2.setText(text)
        self.label_title.setText(titleWind)

        spacing = 0 if len(button) == 0 else 11
        self.verticalLayout_3.setSpacing(spacing)
        self.buttonBox.clear()

        for i in button:
            try:
                self.buttonBox.addButton(i)
            except:
                pass

        self.__showWind()

    def __buttonPress(self, name):
        self.nameButton = name.text()
        self.close()

    def getButtonName(self):
        return self.nameButton

    def paintEvent(self, event):
        self.update()
        self.adjustSize()
        self.frame.setFixedWidth(321)