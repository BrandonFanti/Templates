#Source: https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
)

from PyQt6.QtGui import QMouseEvent

class ActionButton(QPushButton):
    name = None

    def __init__(self,*args, name="", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

        self.clicked.connect(self.on_click)

    def on_click(self, **kwargs):
        print(f"I, {self.__class__.__name__}, AKA: {self.name}, HAVE BEEN CLICKED!")

class ExplosionButton(ActionButton):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_click(self, *args, **kwargs):
        raise Exception("Oh no!")


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.layout = QVBoxLayout()

        self.layout.addWidget(ActionButton("Press Me!", name="useless_button"))
        self.layout.addWidget(ExplosionButton("Do NOT Press Me!", name="explosion_button"))

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        # Set the central widget of the Window.
        self.setCentralWidget(self.widget)

def main(logger=None):
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__': main()