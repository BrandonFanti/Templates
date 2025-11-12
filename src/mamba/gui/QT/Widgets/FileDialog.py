from PySide6.QtWidgets import (
    QFileDialog,
)

class FileDialog(QFileDialog):
    def __init__(self, *args, select_type=QFileDialog.AnyFile, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFileMode(select_type)
        self.setViewMode(QFileDialog.Detail)