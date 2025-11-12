from PySide6.QtWidgets import (
    QApplication,
)
from PySide6.QtUiTools import (
    QUiLoader,
)
import pyqtgraph as pg

from mamba.gui.QT.Widgets import (
    QVBoxScrolled,
    FileDialog,
)

def open():
    dialog=FileDialog()
    dialog.getOpenFileName()

if __name__ == '__main__':
    app = QApplication([])
    window = QUiLoader().load('window.ui')
    sb = QVBoxScrolled()
    window.menu_layout_1.addWidget(sb)
    window.actionOpen.triggered.connect(open)
    window.show()
    pg.exec()