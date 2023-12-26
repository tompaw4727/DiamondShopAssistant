

################################################################################
## Form generated from reading UI file 'orders_delete_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(339, 178)
        Form.setFixedSize(339, 178)
        Form.setStyleSheet(u"QWidget {	background-color: #caf0f8\n"
"}")
        self.subbmitButton = QPushButton(Form)
        self.subbmitButton.setObjectName(u"subbmitButton")
        self.subbmitButton.setGeometry(QRect(90, 130, 161, 41))
        self.subbmitButton.setStyleSheet(u"QPushButton {\n"
"font-family: \"Times New Roman\", serif;\n"
"   font-size: 14px;\n"
"    color: #000;\n"
"    border: 2px solid #343a40;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"	background: #f8f9fa\n"
"    }\n"
"QPushButton:hover {\n"
"    background: #d3d3d3\n"
"}")
        self.id_lineEdit = QLineEdit(Form)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setGeometry(QRect(100, 70, 141, 31))
        self.id_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 0, 241, 51))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.subbmitButton.setText(QCoreApplication.translate("Form", u"submit", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">Delete an order with ID:</span></p></body></html>", None))
    # retranslateUi

