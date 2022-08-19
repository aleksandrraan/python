from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
app = QApplication([])
label = QLabel('Hello World!')
label.setStyleSheet("QLabel{font-size: 18pt;}")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.show()
app.exec()