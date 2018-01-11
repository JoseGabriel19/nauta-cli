import sys
import subprocess
import os
from main_window import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Main_Widget(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.proc = None
        self.pushButton.clicked.connect(self.execute)

    def execute(self):
        command = self.textEdit.toPlainText()
        command = command.split()
        print(command)
        self.textEdit.clear()
        self.proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Main_Widget()
    widget.show()
    sys.exit(app.exec_())