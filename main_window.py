from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import  QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
import sys

class Window(QMainWindow):
    """ Main Window """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel("I am a central widgets")) # Central widget is must always. It can be Qwidgets
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("Menu")
        self.menu1 = self.menuBar().addMenu("Copy")
        self.menu.addAction("&Exit",self.close)
        self.menu1.addAction("&Exit",self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit',self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage(" I am in the status Bar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())