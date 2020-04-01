from PyQt5 import QtWidgets
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *

# Only needed for access to command line arguments
from PyQt5 import QtGui
import sys
import random


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_window()


    def init_window(self):

        # # Create widgets
        # Save Button
        self.button_save = QtWidgets.QPushButton(self)
        self.button_save.setToolTip('Ctrl+C')
        self.button_save.setIcon(QtGui.QIcon("icon.png"))
        self.button_save.setStyleSheet("background-color:rgb(50, 63, 214)")
        self.button_save.resize(55, 50)
        self.button_save.move(350, 70)

        # Create Password - button
        self.create_pass = QtWidgets.QPushButton("Generate Password", self)
        self.create_pass.setToolTip('Create Password!')
        self.create_pass.setFont(QtGui.QFont("Helvetica", 12, QtGui.QFont.Bold))
        self.create_pass.setStyleSheet("background-color:rgb(50, 63, 214)")
        self.create_pass.clicked.connect(self.generete_password)
        self.create_pass.resize(380, 50)
        self.create_pass.move(25, 360)

        # Title title
        self.title = QtWidgets.QLabel(self)
        self.title.setText("Password Generador")
        self.title.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
        self.title.setStyleSheet("color: rgb(255,255,255)")
        self.title.resize(400, 40)
        self.title.move(45, 5)
        # self.setCentralWidget(self.title)

        # Line Edit
        self.line=QtWidgets.QLineEdit(self)
        self.line.setStyleSheet("background-color:rgb(2, 9, 62)")
        self.line.resize(380, 60)
        self.line.move(30, 65)

        # Label's --> 5
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Password length")
        self.label1.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label1.setStyleSheet("color: rgb(255,255,255)")
        self.label1.resize(250, 40)
        self.label1.move(25, 145)


        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Include uppercase letters")
        self.label2.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label2.setStyleSheet("color: rgb(255,255,255)")
        self.label2.resize(250, 40)
        self.label2.move(25, 185)


        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Include lowercase letters")
        self.label3.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label3.setStyleSheet("color: rgb(255,255,255)")
        self.label3.resize(250, 40)
        self.label3.move(25, 225)


        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("Include numbers")
        self.label4.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label4.setStyleSheet("color: rgb(255,255,255)")  # white
        self.label4.resize(250, 40)
        self.label4.move(25, 265)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("Include symbols")
        self.label4.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label4.setStyleSheet("color: rgb(255,255,255)")  # white
        self.label4.resize(250, 40)
        self.label4.move(25, 305)

        # radio
        self.checkbox1 = QtWidgets.QCheckBox(self)
        self.checkbox1.move(395, 190)

        self.checkbox2 = QtWidgets.QCheckBox(self)
        self.checkbox2.move(395, 230)

        self.checkbox3 = QtWidgets.QCheckBox(self)
        self.checkbox3.move(395, 270)

        self.checkbox4 = QtWidgets.QCheckBox(self)
        self.checkbox4.move(395, 310)


        # Spin Box
        self.sp = QtWidgets.QSpinBox(self)
        #self.sp.valueChanged.connect(self.valuechange)
        self.sp.setValue(15)

        self.sp.resize(80, 30)
        self.sp.move(330, 145)

        # MainWindow proprieties
        #               left, top, width, height
        self.setGeometry(300, 300, 435, 430)
        self.setWindowTitle('   ')
        self.setStyleSheet("QMainWindow {background-color:rgb(37,33,95)}")   # "background-color:rgb(70,70,225)"

        self.show()



    def valuechange(self):
        # self.l1.setText("current value:" + str(self.sp.value()))
        print("Current Value Is : " + str(self.sp.value()))

    def generete_password(self):
        length = self.sp.value()
        random_string = ""
        letras = "ABCDEFGHIJKLNMOPQRSTUVXWZ"
        if self.checkbox1.isChecked():
            random_string += letras
        if self.checkbox2.isChecked():
            random_string += letras.lower()
        if self.checkbox3.isChecked():
            random_string += "0123456789"
        if self.checkbox4.isChecked():
            random_string += "@£§€{[]}|!$%&/()=?»«*+`´ºª^~;,.:-_><"


        random_seq = ''.join([random.choice(random_string) for i in range(int(length))])
        print(random_seq)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # window.show()

    app.exec_()

