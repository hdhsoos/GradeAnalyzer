# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAINMAIN.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

FOUR_MIN = 3.6
# минимальный средний балл для четвёрки

FIVE_MIN = 4.6
# минимальный средний балл для пятёрки


def average(grades):
    # функция подсчёта среднего балла
    s = sum(grades)
    lenght = len(grades)
    ave = s / lenght
    # ave - средний балл для расчетов
    sa = ave
    # sa - средний балл, который потом вернёт функция

    g = 5
    # g - оценка, которую нам необходимо получать, чтобы поднять балл
    # min - минимальный балл для получения оценки
    # счётчик
    n = 0
    # считаем, сколько пятёрок необходимо до 4
    while ave < FOUR_MIN:
        n += 1
        s += g
        lenght += 1
        ave = s / lenght
    n1 = n

    # считаем, сколько пятёрок необходимо до 5
    g = 4
    s = sum(grades)
    lenght = len(grades)
    ave = s / lenght
    n = 0
    while ave < FOUR_MIN:
        n += 1
        s += g
        lenght += 1
        ave = s / lenght
    n2 = n

    # считаем, сколько пятёрок нужно до 5
    g = 5
    s = sum(grades)
    lenght = len(grades)
    ave = s / lenght
    n = 0
    while ave < FIVE_MIN:
        n += 1
        s += g
        lenght += 1
        ave = s / lenght
    n3 = n

    return (sa, n2, n1, n3)
    # средний балл, 4 до четвёрки, 5 до четвёрки, 5 до пятёрки


class Ui_MainWindow(object):
    # класс, который я импортировала с помощью pyuic5
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 430, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 701, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber_19 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_19.setObjectName("lcdNumber_19")
        self.gridLayout.addWidget(self.lcdNumber_19, 2, 3, 1, 1)
        self.lcdNumber_24 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_24.setObjectName("lcdNumber_24")
        self.gridLayout.addWidget(self.lcdNumber_24, 7, 3, 1, 1)
        self.lcdNumber_40 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_40.setObjectName("lcdNumber_40")
        self.gridLayout.addWidget(self.lcdNumber_40, 1, 4, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lcdNumber_18 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_18.setObjectName("lcdNumber_18")
        self.gridLayout.addWidget(self.lcdNumber_18, 1, 3, 1, 1)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.gridLayout.addWidget(self.lcdNumber_6, 4, 1, 1, 1)
        self.lcdNumber_34 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_34.setObjectName("lcdNumber_34")
        self.gridLayout.addWidget(self.lcdNumber_34, 7, 4, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 1, 1, 1, 1)
        self.lcdNumber_23 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_23.setObjectName("lcdNumber_23")
        self.gridLayout.addWidget(self.lcdNumber_23, 6, 3, 1, 1)
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.gridLayout.addWidget(self.lcdNumber_10, 5, 2, 1, 1)
        self.lcdNumber_12 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.gridLayout.addWidget(self.lcdNumber_12, 3, 2, 1, 1)
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.gridLayout.addWidget(self.lcdNumber_8, 6, 1, 1, 1)
        self.lcdNumber_17 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_17.setObjectName("lcdNumber_17")
        self.gridLayout.addWidget(self.lcdNumber_17, 0, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lcdNumber_14 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_14.setObjectName("lcdNumber_14")
        self.gridLayout.addWidget(self.lcdNumber_14, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 6, 5, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 7, 5, 1, 1)
        self.lcdNumber_37 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_37.setObjectName("lcdNumber_37")
        self.gridLayout.addWidget(self.lcdNumber_37, 4, 4, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 0, 2, 1, 1)
        self.lcdNumber_35 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_35.setObjectName("lcdNumber_35")
        self.gridLayout.addWidget(self.lcdNumber_35, 6, 4, 1, 1)
        self.lcdNumber_15 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_15.setObjectName("lcdNumber_15")
        self.gridLayout.addWidget(self.lcdNumber_15, 7, 1, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 5, 1, 1)
        self.lcdNumber_20 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_20.setObjectName("lcdNumber_20")
        self.gridLayout.addWidget(self.lcdNumber_20, 3, 3, 1, 1)
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.gridLayout.addWidget(self.lcdNumber_9, 6, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.lcdNumber_39 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_39.setObjectName("lcdNumber_39")
        self.gridLayout.addWidget(self.lcdNumber_39, 2, 4, 1, 1)
        self.lcdNumber_16 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_16.setObjectName("lcdNumber_16")
        self.gridLayout.addWidget(self.lcdNumber_16, 7, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 5, 1, 1)
        self.lcdNumber_11 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.gridLayout.addWidget(self.lcdNumber_11, 4, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 5, 5, 1, 1)
        self.lcdNumber_36 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_36.setObjectName("lcdNumber_36")
        self.gridLayout.addWidget(self.lcdNumber_36, 5, 4, 1, 1)
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.gridLayout.addWidget(self.lcdNumber_7, 5, 1, 1, 1)
        self.lcdNumber_22 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_22.setObjectName("lcdNumber_22")
        self.gridLayout.addWidget(self.lcdNumber_22, 5, 3, 1, 1)
        self.lcdNumber_21 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_21.setObjectName("lcdNumber_21")
        self.gridLayout.addWidget(self.lcdNumber_21, 4, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lcdNumber_13 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.gridLayout.addWidget(self.lcdNumber_13, 2, 2, 1, 1)
        self.lcdNumber_38 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_38.setObjectName("lcdNumber_38")
        self.gridLayout.addWidget(self.lcdNumber_38, 3, 4, 1, 1)
        self.lcdNumber_26 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_26.setObjectName("lcdNumber_26")
        self.gridLayout.addWidget(self.lcdNumber_26, 0, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 10, 101, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 10, 81, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 10, 101, 21))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(480, 10, 81, 21))
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_7.setText(_translate("MainWindow", "Ввести данные"))
        self.label_3.setText(_translate("MainWindow", "Предмет 3"))
        self.label_8.setText(_translate("MainWindow", "Предмет 8"))
        self.pushButton_5.setText(_translate("MainWindow", "Ввести данные"))
        self.label_5.setText(_translate("MainWindow", "Предмет 6"))
        self.label.setText(_translate("MainWindow", "Предмет 2"))
        self.label_2.setText(_translate("MainWindow", "Предмет 1"))
        self.pushButton_9.setText(_translate("MainWindow", "Ввести данные"))
        self.pushButton_10.setText(_translate("MainWindow", "Ввести данные"))
        self.pushButton_3.setText(_translate("MainWindow", "Ввести данные"))
        self.pushButton_6.setText(_translate("MainWindow", "Ввести данные"))
        self.label_6.setText(_translate("MainWindow", "Предмет 7"))
        self.pushButton_4.setText(_translate("MainWindow", "Ввести данные"))
        self.pushButton_8.setText(_translate("MainWindow", "Ввести данные"))
        self.label_4.setText(_translate("MainWindow", "Предмет 5"))
        self.label_7.setText(_translate("MainWindow", "Предмет 4"))
        self.label_9.setText(_translate("MainWindow", "4 до четвёрки:"))
        self.label_10.setText(_translate("MainWindow", "5 до четвёрки:"))
        self.label_11.setText(_translate("MainWindow", "Средний балл:"))
        self.label_13.setText(_translate("MainWindow", "5 до пятёрки:"))


class AnalyzerWidget(QMainWindow, Ui_MainWindow):
    # основной класс анализатора
    def __init__(self):
        super().__init__()
        uic.loadUi('MAINMAIN.ui', self)
        # self.colorRow(0, QColor(0, 150, 100))
        # добавляем оценки в строчку
        self.pushButton_3.clicked.connect(self.gradeadd)
        self.pushButton_4.clicked.connect(self.gradeadd)
        self.pushButton_5.clicked.connect(self.gradeadd)
        self.pushButton_6.clicked.connect(self.gradeadd)
        self.pushButton_7.clicked.connect(self.gradeadd)
        self.pushButton_8.clicked.connect(self.gradeadd)
        self.pushButton_9.clicked.connect(self.gradeadd)
        self.pushButton_10.clicked.connect(self.gradeadd)
        # self.replay сбрасывает все поля
        self.pushButton_2.clicked.connect(self.replay)
        # меняем цвет кнопки
        # хотела изменить всё, но не успела
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')

    def gradeadd(self):

        name, okBtnPressed = QInputDialog.getText(self, "Введите название предмета",
                                                  "Как называется предмет?")
        if okBtnPressed:
            # мы определяем отправителя
            # определив, какую строчку выбрал пользователь, мы меняем текст
            if self.sender() == self.pushButton_3:
                self.label_2.setText(name)
            elif self.sender() == self.pushButton_4:
                self.label.setText(name)
            elif self.sender() == self.pushButton_5:
                self.label_3.setText(name)
            elif self.sender() == self.pushButton_6:
                self.label_7.setText(name)
            elif self.sender() == self.pushButton_7:
                self.label_4.setText(name)
            elif self.sender() == self.pushButton_8:
                self.label_5.setText(name)
            elif self.sender() == self.pushButton_9:
                self.label_6.setText(name)
            elif self.sender() == self.pushButton_10:
                self.label_8.setText(name)
            grades, okBtnPressed = QInputDialog.getText(self, "Введите оценки",
                                                        "Вставьте оценки.")
            if grades != '':
                # проверка на пустоту
                if okBtnPressed:
                    grades = list(map(float, grades.split()))
                    information = average(grades)
                    # мы определяем отправителя
                    # определив, какую строчку выбрал пользователь, мы меняем текст
                    if self.sender() == self.pushButton_3:
                        self.lcdNumber.display(information[0])
                        self.lcdNumber_2.display(information[1])
                        self.lcdNumber_17.display(information[2])
                        self.lcdNumber_26.display(information[3])
                    elif self.sender() == self.pushButton_4:
                        self.lcdNumber_3.display(information[0])
                        self.lcdNumber_14.display(information[1])
                        self.lcdNumber_18.display(information[2])
                        self.lcdNumber_40.display(information[3])
                    elif self.sender() == self.pushButton_5:
                        self.lcdNumber_4.display(information[0])
                        self.lcdNumber_13.display(information[1])
                        self.lcdNumber_19.display(information[2])
                        self.lcdNumber_39.display(information[3])
                    elif self.sender() == self.pushButton_6:
                        self.lcdNumber_5.display(information[0])
                        self.lcdNumber_12.display(information[1])
                        self.lcdNumber_20.display(information[2])
                        self.lcdNumber_38.display(information[3])
                    elif self.sender() == self.pushButton_7:
                        self.lcdNumber_6.display(information[0])
                        self.lcdNumber_11.display(information[1])
                        self.lcdNumber_21.display(information[2])
                        self.lcdNumber_37.display(information[3])
                    elif self.sender() == self.pushButton_8:
                        self.lcdNumber_7.display(information[0])
                        self.lcdNumber_10.display(information[1])
                        self.lcdNumber_22.display(information[2])
                        self.lcdNumber_36.display(information[3])
                    elif self.sender() == self.pushButton_9:
                        self.lcdNumber_8.display(information[0])
                        self.lcdNumber_9.display(information[1])
                        self.lcdNumber_23.display(information[2])
                        self.lcdNumber_35.display(information[3])
                    elif self.sender() == self.pushButton_10:
                        self.lcdNumber_15.display(information[0])
                        self.lcdNumber_16.display(information[1])
                        self.lcdNumber_24.display(information[2])
                        self.lcdNumber_34.display(information[3])

    def replay(self):
        # команда заменяет все номера на нули
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        self.lcdNumber_3.display(0)
        self.lcdNumber_4.display(0)
        self.lcdNumber_5.display(0)
        self.lcdNumber_6.display(0)
        self.lcdNumber_7.display(0)
        self.lcdNumber_8.display(0)
        self.lcdNumber_9.display(0)
        self.lcdNumber_10.display(0)
        self.lcdNumber_11.display(0)
        self.lcdNumber_12.display(0)
        self.lcdNumber_13.display(0)
        self.lcdNumber_14.display(0)
        self.lcdNumber_15.display(0)
        self.lcdNumber_16.display(0)
        self.lcdNumber_17.display(0)
        self.lcdNumber_18.display(0)
        self.lcdNumber_19.display(0)
        self.lcdNumber_20.display(0)
        self.lcdNumber_21.display(0)
        self.lcdNumber_22.display(0)
        self.lcdNumber_23.display(0)
        self.lcdNumber_24.display(0)
        self.lcdNumber_26.display(0)
        self.lcdNumber_34.display(0)
        self.lcdNumber_35.display(0)
        self.lcdNumber_36.display(0)
        self.lcdNumber_37.display(0)
        self.lcdNumber_38.display(0)
        self.lcdNumber_39.display(0)
        self.lcdNumber_40.display(0)
        # команда заменяет все названия предметов на стандартные
        self.label.setText('Предмет 2')
        self.label_2.setText('Предмет 1')
        self.label_3.setText('Предмет 3')
        self.label_4.setText('Предмет 5')
        self.label_5.setText('Предмет 6')
        self.label_6.setText('Предмет 7')
        self.label_7.setText('Предмет 4')
        self.label_8.setText('Предмет 8')


app = QApplication(sys.argv)
ex = AnalyzerWidget()
ex.show()
sys.exit(app.exec_())
