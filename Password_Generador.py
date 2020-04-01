from PyQt5.QtWidgets import QMainWindow, QApplication, QSpinBox, \
    QLineEdit, QPushButton, QLabel, QCheckBox
from PyQt5 import QtGui
import sys
from random import choice


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_window()

    def init_window(self):

        ## Create widgets
        # Line Edit
        self.line = QLineEdit(self)
        self.line.setStyleSheet('border: 1px solid rgb(2, 9, 62);'
                                'background-color:rgb(2, 9, 62);'
                                'color: rgb(255, 255, 255);'
                                'font: bold 15pt "Arial";')
        self.line.setEnabled(False)
        self.line.resize(380, 60)
        self.line.move(30, 65)

        # Save Button
        self.button_save = QPushButton("Copy",self)
        self.button_save.setToolTip('Ctrl+C')
        self.button_save.setStyleSheet("background-color:rgb(50, 63, 214)")
        self.button_save.clicked.connect(self.copy)
        self.button_save.resize(55, 50)
        self.button_save.move(350, 70)

        # Create Password - button
        self.create_pass = QPushButton("Generate Password", self)
        self.create_pass.setToolTip('Create Password!')
        self.create_pass.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Bold,))
        self.create_pass.setStyleSheet("background-color:rgb(50, 63, 214);color: white")
        self.create_pass.clicked.connect(self.generete_password)
        self.create_pass.resize(380, 50)
        self.create_pass.move(25, 360)

        # Title title
        self.title = QLabel(self)
        self.title.setText("Password Generador")
        self.title.setFont(QtGui.QFont("Arial", 21, QtGui.QFont.Bold))
        self.title.setStyleSheet("color: rgb(255,255,255)")
        self.title.resize(400, 40)
        self.title.move(40, 15)

        # Label's --> 5
        self.label1 = QLabel(self)
        self.label1.setText("Password length")
        self.label1.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label1.setStyleSheet("color: rgb(255,255,255)")  # white
        self.label1.resize(300, 40)
        self.label1.move(25, 145)

        self.label2 = QLabel(self)
        self.label2.setText("Include uppercase letters ")
        self.label2.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label2.setStyleSheet("color: rgb(255,255,255)")
        self.label2.resize(355, 40)
        self.label2.move(25, 185)

        self.label3 = QLabel(self)
        self.label3.setText("Include lowercase letters ")
        self.label3.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label3.setStyleSheet("color: rgb(255,255,255)")
        self.label3.resize(355, 40)
        self.label3.move(25, 225)

        self.label4 = QLabel(self)
        self.label4.setText("Include numbers ")
        self.label4.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label4.setStyleSheet("color: rgb(255,255,255)")
        self.label4.resize(355, 40)
        self.label4.move(25, 265)

        self.label4 = QLabel(self)
        self.label4.setText("Include symbols  ")
        self.label4.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label4.setStyleSheet("color: rgb(255,255,255)")
        self.label4.resize(355, 40)
        self.label4.move(25, 305)

        # CheckBox's  --> 4
        self.checkbox1 = QCheckBox(self)
        self.checkbox1.setChecked(True)
        self.checkbox1.move(395, 190)

        self.checkbox2 = QCheckBox(self)
        self.checkbox2.setChecked(True)
        self.checkbox2.move(395, 230)

        self.checkbox3 = QCheckBox(self)
        self.checkbox3.setChecked(True)
        self.checkbox3.move(395, 270)

        self.checkbox4 = QCheckBox(self)
        self.checkbox4.setChecked(True)
        self.checkbox4.move(395, 310)

        # Spin Box
        self.sp = QSpinBox(self)
        self.sp.setValue(15)
        self.sp.resize(80, 30)
        self.sp.move(330, 145)

        # MainWindow proprieties
        self.setGeometry(300, 300, 435, 430)
        self.setWindowTitle(" ")
        self.setStyleSheet("QMainWindow {background-color:rgb(37,33,95)}")

        self.show()

    def generete_password(self):
        length = self.sp.value()
        random_string = ""
        letras = "ABCDEFGHIJKLNMOPQRSTUVXWZ"
        numbers = "0123456789"
        special_characters = "@£§€{[]}|!$%&/()=?»«*+`´ºª^~;,.:-_><"

        if self.checkbox1.isChecked():
            random_string += letras
        if self.checkbox2.isChecked():
            random_string += letras.lower()
        if self.checkbox3.isChecked():
            random_string += numbers
        if self.checkbox4.isChecked():
            random_string += special_characters

        if not self.checkbox1.isChecked() and not self.checkbox2.isChecked() \
            and not self.checkbox3.isChecked() and not self.checkbox4.isChecked():
            random_string = letras.lower()

        random_seq = ''.join([choice(random_string) for _ in range(int(length))])
        self.line.setText(random_seq)

    def copy(self):
        QApplication.clipboard().setText(self.line.text())  # Copiar text in line box
        # Colar : text = QtWidgets.QApplication.clipboard().text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

