

################################################################################
## Form generated from reading UI file 'orders_add_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(613, 372)
        Form.setFixedSize(613, 372)
        Form.setStyleSheet(u"QWidget {	background-color: #caf0f8\n"
"}")
        self.subbmitButton = QPushButton(Form)
        self.subbmitButton.setObjectName(u"subbmitButton")
        self.subbmitButton.setGeometry(QRect(220, 320, 161, 41))
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
        self.carat_lineEdit = QLineEdit(Form)
        self.carat_lineEdit.setObjectName(u"carat_lineEdit")
        self.carat_lineEdit.setGeometry(QRect(80, 40, 113, 21))
        self.carat_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.cut_comboBox = QComboBox(Form)
        self.cut_comboBox.addItem("")
        self.cut_comboBox.addItem("")
        self.cut_comboBox.addItem("")
        self.cut_comboBox.addItem("")
        self.cut_comboBox.addItem("")
        self.cut_comboBox.setObjectName(u"cut_comboBox")
        self.cut_comboBox.setGeometry(QRect(270, 40, 111, 22))
        self.cut_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.color_comboBox = QComboBox(Form)
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.setObjectName(u"color_comboBox")
        self.color_comboBox.setGeometry(QRect(480, 40, 111, 22))
        self.color_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.clarity_comboBox = QComboBox(Form)
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.setObjectName(u"clarity_comboBox")
        self.clarity_comboBox.setGeometry(QRect(80, 120, 111, 22))
        self.clarity_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.table_lineEdit = QLineEdit(Form)
        self.table_lineEdit.setObjectName(u"table_lineEdit")
        self.table_lineEdit.setGeometry(QRect(480, 120, 113, 21))
        self.table_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.length_lineEdit = QLineEdit(Form)
        self.length_lineEdit.setObjectName(u"length_lineEdit")
        self.length_lineEdit.setGeometry(QRect(80, 200, 113, 21))
        self.length_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	background-color: #f8f9fa;\n"
"	border: 1px solid #343a40;\n"
"}")
        self.width_lineEdit = QLineEdit(Form)
        self.width_lineEdit.setObjectName(u"width_lineEdit")
        self.width_lineEdit.setGeometry(QRect(270, 200, 113, 21))
        self.width_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.depth_lineEdit = QLineEdit(Form)
        self.depth_lineEdit.setObjectName(u"depth_lineEdit")
        self.depth_lineEdit.setGeometry(QRect(480, 200, 113, 21))
        self.depth_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.price_lineEdit = QLineEdit(Form)
        self.price_lineEdit.setObjectName(u"price_lineEdit")
        self.price_lineEdit.setGeometry(QRect(130, 260, 113, 21))
        self.price_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 41, 21))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 40, 31, 20))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 40, 41, 20))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 120, 49, 21))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(420, 120, 41, 21))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 260, 61, 20))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(420, 200, 49, 21))
        self.label_8.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 200, 51, 20))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 200, 51, 21))
        self.label_10.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.client_id_lineEdit = QLineEdit(Form)
        self.client_id_lineEdit.setObjectName(u"client_id_lineEdit")
        self.client_id_lineEdit.setGeometry(QRect(400, 260, 113, 21))
        self.client_id_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(320, 260, 61, 20))
        self.label_11.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.year_lineEdit = QLineEdit(Form)
        self.year_lineEdit.setObjectName(u"year_lineEdit")
        self.year_lineEdit.setGeometry(QRect(270, 120, 113, 21))
        self.year_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(220, 120, 41, 21))
        self.label_12.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.subbmitButton.setText(QCoreApplication.translate("Form", u"submit", None))
        self.cut_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Fair", None))
        self.cut_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Good", None))
        self.cut_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Very Good", None))
        self.cut_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Premium", None))
        self.cut_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Ideal", None))

        self.color_comboBox.setItemText(0, QCoreApplication.translate("Form", u"J", None))
        self.color_comboBox.setItemText(1, QCoreApplication.translate("Form", u"I", None))
        self.color_comboBox.setItemText(2, QCoreApplication.translate("Form", u"D", None))
        self.color_comboBox.setItemText(3, QCoreApplication.translate("Form", u"H", None))
        self.color_comboBox.setItemText(4, QCoreApplication.translate("Form", u"F", None))
        self.color_comboBox.setItemText(5, QCoreApplication.translate("Form", u"E", None))
        self.color_comboBox.setItemText(6, QCoreApplication.translate("Form", u"G", None))

        self.clarity_comboBox.setItemText(0, QCoreApplication.translate("Form", u"I1", None))
        self.clarity_comboBox.setItemText(1, QCoreApplication.translate("Form", u"SI2", None))
        self.clarity_comboBox.setItemText(2, QCoreApplication.translate("Form", u"SI1", None))
        self.clarity_comboBox.setItemText(3, QCoreApplication.translate("Form", u"VS2", None))
        self.clarity_comboBox.setItemText(4, QCoreApplication.translate("Form", u"VS1", None))
        self.clarity_comboBox.setItemText(5, QCoreApplication.translate("Form", u"VVS2", None))
        self.clarity_comboBox.setItemText(6, QCoreApplication.translate("Form", u"VVS1", None))
        self.clarity_comboBox.setItemText(7, QCoreApplication.translate("Form", u"IF", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">carat:</span></p><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">cut:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">color:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">clarity :</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">table:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">price ($):</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">depth:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">width:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">length:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">client ID:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">year:</span></p></body></html>", None))
    # retranslateUi

