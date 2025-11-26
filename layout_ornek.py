import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class LayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGRIDLAYOUT ORNEK")
        self.setGeometry(200, 250, 500, 300)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        self.label = QLabel("Kullanıcı Adı :", self)
        self.line_edit = QLineEdit(self)
        horizontal_layout.addWidget(self.label)
        horizontal_layout.addWidget(self.line_edit)

        main_layout.addLayout(horizontal_layout)

        self.button = QPushButton("kaydet", self)
        main_layout.addWidget(self.button)

        button_layout = QHBoxLayout()
        self.button1 = QPushButton("BUTON 1")
        self.button2 = QPushButton("BUTON 2")

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)

        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)


app = QApplication(sys.argv)
window = LayoutExample()
window.show()
sys.exit(app.exec_())