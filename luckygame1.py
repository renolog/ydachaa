from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 724)
        MainWindow.setStyleSheet("background-color: rgb(254, 228, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 740, 301))
        self.label.setStyleSheet("background-color: rgb(216, 198, 222);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(310, 450, 191, 81))
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setStyleSheet("font: 75 20pt \"Rockwell\";\n"
                                     "background-color: rgb(216, 198, 222);")
        self.start_btn.setObjectName("start_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)  # score
        self.label_2.setGeometry(QtCore.QRect(317, 568, 181, 91))
        self.label_2.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_2.setObjectName("label_2")
        self.h1 = QtWidgets.QLabel(self.centralwidget)
        self.h1.setGeometry(QtCore.QRect(80, 170, 170, 170))
        self.h1.setText("")
        self.h1.setPixmap(QtGui.QPixmap("heart.jpg"))
        self.h1.setScaledContents(True)
        self.h1.setObjectName("h1")
        self.h2 = QtWidgets.QLabel(self.centralwidget)
        self.h2.setGeometry(QtCore.QRect(310, 170, 170, 170))
        self.h2.setText("")
        self.h2.setPixmap(QtGui.QPixmap("heart.jpg"))
        self.h2.setScaledContents(True)
        self.h2.setObjectName("h2")
        self.h3 = QtWidgets.QLabel(self.centralwidget)
        self.h3.setGeometry(QtCore.QRect(540, 170, 170, 170))
        self.h3.setText("")
        self.h3.setPixmap(QtGui.QPixmap("heart.jpg"))
        self.h3.setScaledContents(True)
        self.h3.setObjectName("h3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 30, 191, 51))
        self.label_6.setStyleSheet("font: 75 24pt \"Rockwell\";")
        self.label_6.setObjectName("label_6")
        self.f1 = QtWidgets.QLabel(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(80, 170, 170, 170))
        self.f1.setText("")
        self.f1.setPixmap(QtGui.QPixmap("flower.jpg"))
        self.f1.setScaledContents(True)
        self.f1.setObjectName("f1")
        self.f2 = QtWidgets.QLabel(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(310, 170, 170, 170))
        self.f2.setText("")
        self.f2.setPixmap(QtGui.QPixmap("flower.jpg"))
        self.f2.setScaledContents(True)
        self.f2.setObjectName("f2")
        self.f3 = QtWidgets.QLabel(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(540, 170, 170, 170))
        self.f3.setText("")
        self.f3.setPixmap(QtGui.QPixmap("flower.jpg"))
        self.f3.setScaledContents(True)
        self.f3.setObjectName("f3")
        self.c1 = QtWidgets.QLabel(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(80, 170, 170, 170))
        self.c1.setText("")
        self.c1.setPixmap(QtGui.QPixmap("cloud.jpg"))
        self.c1.setScaledContents(True)
        self.c1.setObjectName("c1")
        self.c2 = QtWidgets.QLabel(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(310, 170, 170, 170))
        self.c2.setText("")
        self.c2.setPixmap(QtGui.QPixmap("cloud.jpg"))
        self.c2.setScaledContents(True)
        self.c2.setObjectName("c2")
        self.c3 = QtWidgets.QLabel(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(540, 170, 170, 170))
        self.c3.setText("")
        self.c3.setPixmap(QtGui.QPixmap("cloud.jpg"))
        self.c3.setScaledContents(True)
        self.c3.setObjectName("c3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.c1.hide()
        self.c2.hide()
        self.c3.hide()
        self.f1.hide()
        self.f2.hide()
        self.f3.hide()
        self.h1.hide()
        self.h2.hide()
        self.h3.hide()
        self.c1.hidden = True
        self.c2.hidden = True
        self.c3.hidden = True
        self.f1.hidden = True
        self.f2.hidden = True
        self.f3.hidden = True
        self.h1.hidden = True
        self.h2.hidden = True
        self.h3.hidden = True

        self.start_btn.clicked.connect(self.spin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "LuckyGame"))

    def spin(self, label_2):
        s = random.randint(1, 3)
        n = random.randint(1, 3)
        m = random.randint(1, 3)

        # score
        if s == n and n == m:
            cont = self.label_2.text()
            cont = int(cont) + 3
            cont = str(cont)
            self.label_2.setText(cont)

        if self.c1.hidden and self.c2.hidden and self.c3.hidden and self.f1.hidden and self.f2.hidden \
                and self.f3.hidden and self.h1.hidden and self.h2.hidden and self.h3.hidden:

            if s == 1:
                self.c1.show()
                self.c1.hidden = False
            elif s == 2:
                self.f1.show()
                self.f1.hidden = False
            elif s == 3:
                self.h1.show()
                self.h1.hidden = False

            if n == 1:
                self.c2.show()
                self.c2.hidden = False
            elif n == 2:
                self.f2.show()
                self.f2.hidden = False
            elif n == 3:
                self.h2.show()
                self.h2.hidden = False

            if m == 1:
                self.c3.show()
                self.c3.hidden = False
            elif m == 2:
                self.f3.show()
                self.f3.hidden = False
            elif m == 3:
                self.h3.show()
                self.h3.hidden = False
        else:
            self.c1.hide()
            self.c2.hide()
            self.c3.hide()
            self.f1.hide()
            self.f2.hide()
            self.f3.hide()
            self.h1.hide()
            self.h2.hide()
            self.h3.hide()
            self.c1.hidden = True
            self.c2.hidden = True
            self.c3.hidden = True
            self.f1.hidden = True
            self.f2.hidden = True
            self.f3.hidden = True
            self.h1.hidden = True
            self.h2.hidden = True
            self.h3.hidden = True

            if s == 1:
                self.c1.show()
                self.c1.hidden = False
            elif s == 2:
                self.f1.show()
                self.f1.hidden = False
            elif s == 3:
                self.h1.show()
                self.h1.hidden = False

            if n == 1:
                self.c2.show()
                self.c2.hidden = False
            elif n == 2:
                self.f2.show()
                self.f2.hidden = False
            elif n == 3:
                self.h2.show()
                self.h2.hidden = False

            if m == 1:
                self.c3.show()
                self.c3.hidden = False
            elif m == 2:
                self.f3.show()
                self.f3.hidden = False
            elif m == 3:
                self.h3.show()
                self.h3.hidden = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
