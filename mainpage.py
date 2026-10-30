# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpage.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Sudoku(object):
    def setupUi(self, Sudoku):
        if not Sudoku.objectName():
            Sudoku.setObjectName(u"Sudoku")
        Sudoku.resize(701, 436)
        Sudoku.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(Sudoku)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table_number = QTableWidget(self.centralwidget)
        self.table_number.setObjectName(u"table_number")
        self.table_number.setGeometry(QRect(10, 20, 391, 391))
        self.table_number.setStyleSheet(u"border: 2px solid black;")
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(420, 20, 81, 81))
        self.btn1.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(510, 20, 81, 81))
        self.btn2.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(600, 20, 81, 81))
        self.btn3.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setGeometry(QRect(420, 110, 81, 81))
        self.btn4.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setGeometry(QRect(510, 110, 81, 81))
        self.btn5.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setGeometry(QRect(600, 110, 81, 81))
        self.btn6.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setGeometry(QRect(510, 200, 81, 81))
        self.btn8.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setGeometry(QRect(420, 200, 81, 81))
        self.btn7.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setGeometry(QRect(600, 200, 81, 81))
        self.btn9.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        self.btn_new = QPushButton(self.centralwidget)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setGeometry(QRect(420, 290, 201, 51))
        self.btn_new.setStyleSheet(u"border-radius: 5px;\n"
"font-size: 20px;\n"
"color: white;\n"
"background-color: #6d82c7;\n"
"font-weight: 600;")
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(630, 290, 51, 51))
        self.btn_delete.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"font-size: 20px;")
        icon = QIcon()
        icon.addFile(u"iconics/eraser.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon)
        self.btn_delete.setIconSize(QSize(28, 32))
        Sudoku.setCentralWidget(self.centralwidget)

        self.retranslateUi(Sudoku)

        QMetaObject.connectSlotsByName(Sudoku)
    # setupUi

    def retranslateUi(self, Sudoku):
        Sudoku.setWindowTitle(QCoreApplication.translate("Sudoku", u"MainWindow", None))
        self.btn1.setText(QCoreApplication.translate("Sudoku", u"1", None))
        self.btn2.setText(QCoreApplication.translate("Sudoku", u"2", None))
        self.btn3.setText(QCoreApplication.translate("Sudoku", u"3", None))
        self.btn4.setText(QCoreApplication.translate("Sudoku", u"4", None))
        self.btn5.setText(QCoreApplication.translate("Sudoku", u"5", None))
        self.btn6.setText(QCoreApplication.translate("Sudoku", u"6", None))
        self.btn8.setText(QCoreApplication.translate("Sudoku", u"8", None))
        self.btn7.setText(QCoreApplication.translate("Sudoku", u"7", None))
        self.btn9.setText(QCoreApplication.translate("Sudoku", u"9", None))
        self.btn_new.setText(QCoreApplication.translate("Sudoku", u"\u041d\u043e\u0432\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.btn_delete.setText("")
    # retranslateUi

