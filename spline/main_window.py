from PyQt5.QtWidgets import QMainWindow, QDialog, QLabel,QPushButton,QHBoxLayout

from spline_view import SplineView
from control_panel import ControlPanel

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        close_action = file_menu.addAction('Close')
        close_action.triggered.connect(self.close)
        file_menu = menubar.addMenu('Edit')
        undo_action = file_menu.addAction('Undo')
        redo_action = file_menu.addAction('Redo')
        file_menu = menubar.addMenu('About')
        about_action = file_menu.addAction('About')
        about_action.triggered.connect(self.show_about)

        spline_view = SplineView()
        undo_action.triggered.connect(spline_view.Undo)
        self.setCentralWidget(spline_view)

        control_panel = ControlPanel(spline_view.maximumWidth(), spline_view.maximumHeight())
        self.statusBar().addWidget(control_panel)

        control_panel.state_changed.connect(spline_view.set_current_knot)
        spline_view.current_knot_changed.connect(control_panel.set_state)
    
    def show_about(self):
        self.about_dialog=QDialog()
        self.about_dialog.setWindowTitle('About project')
        self.label=QLabel()
        self.label.setText('1\n\ 2 \n3')
        layout=QHBoxLayout()
        layout.addWidget(self.label)
        self.about_dialog.setLayout(layout)
        self.about_dialog.showNormal()
        