import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton

class HorizontalLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBOX ORNEK")
        self.setGeometry(200, 250, 500, 300)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        button1 = QPushButton("BUTON 1",self)
        button2 = QPushButton("BUTON 2", self)
        button3 = QPushButton("BUTON 3",self)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        central_widget.setLayout(layout)




app = QApplication(sys.argv)
window = HorizontalLayoutExample()
window.show()
sys.exit(app.exec_())