import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton

class FormLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFORMLAYOUT ORNEK")
        self.setGeometry(200, 250, 500, 300)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QFormLayout()
        self.name_label = QLabel("İsim : ",self)
        self.name_input = QLineEdit(self)
        self.email_label = QLabel("Email :", self)
        self.email_input = QLineEdit(self)
        layout.addRow(self.name_label, self.name_input)
        layout.addRow(self.email_label, self.email_input)
        save_button = QPushButton("KAYDET",self)
        layout.addRow(save_button)
        central_widget.setLayout(layout)

app = QApplication(sys.argv)
window = FormLayoutExample()
window.show()
sys.exit(app.exec_())