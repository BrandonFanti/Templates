
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QScrollArea,
    QGridLayout,
    QVBoxLayout,
)
from PyQt6.QtCore import QSize,Qt

from .QChartScrolled import QChartXY
import pyqtgraph as pg

class QVBoxScrolled(QWidget):
    __version__ = "0.0.1"
    __author__ = "Your Name"

    row = 0

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self)

        self.setMinimumSize(QSize(kwargs.get('wmin_size', 300), kwargs.get('hmin_size', 200)),) 

        self.layout = QGridLayout()
        self.scroll_widget = QWidget()
        self.scroll_area = QScrollArea()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.main_vbox_layout = QVBoxLayout()

        self.scroll_widget.setLayout(self.main_vbox_layout)
        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)


    def add_widget(self, widget):
        self.main_vbox_layout.addWidget(widget)
        self.row += 1

    def __repr__(self):
        d = {}
        for key,value in self.__dict__.items():
            if not key.startswith("_"): # Exclude private attributes
                d[key] = value
        if d.keys():
            return f"{__class__.__name__}({d})"
        else:
            return f"{__class__.__name__}()"


    def get_version_info() -> str:
        return (
            f"This is {__class__.__name__} class!\n"
            f"From the package: {__package__}\n"
            f"Authored by: {__class__.__author__}\n"
            f"Version: {__class__.__version__}\n"
        )

    def main():
        print(__class__.get_version_info())
        print(f"You can initialize it like this: ")
        print(repr(__class__()))
