import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PYQT ORNEGI")
        self.button = QPushButton("TIKLA")
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("Butona tıklandı")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

