

################################################################################
## Form generated from reading UI file 'customer_add_window.ui'
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
        Form.resize(600, 252)
        Form.setFixedSize(600, 252)
        Form.setStyleSheet(u"QWidget {	background-color: #caf0f8\n"
"}")
        self.subbmitButton = QPushButton(Form)
        self.subbmitButton.setObjectName(u"subbmitButton")
        self.subbmitButton.setGeometry(QRect(230, 180, 161, 41))
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
        self.phone_lineEdit = QLineEdit(Form)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setGeometry(QRect(80, 40, 113, 21))
        self.phone_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.purpose_comboBox = QComboBox(Form)
        self.purpose_comboBox.addItem("")
        self.purpose_comboBox.addItem("")
        self.purpose_comboBox.addItem("")
        self.purpose_comboBox.addItem("")
        self.purpose_comboBox.addItem("")
        self.purpose_comboBox.addItem("")
        self.purpose_comboBox.setObjectName(u"purpose_comboBox")
        self.purpose_comboBox.setGeometry(QRect(80, 120, 111, 22))
        self.purpose_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 51, 21))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 40, 41, 20))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 40, 41, 20))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.mail_lineEdit = QLineEdit(Form)
        self.mail_lineEdit.setObjectName(u"mail_lineEdit")
        self.mail_lineEdit.setGeometry(QRect(270, 40, 113, 21))
        self.mail_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.age_lineEdit = QLineEdit(Form)
        self.age_lineEdit.setObjectName(u"age_lineEdit")
        self.age_lineEdit.setGeometry(QRect(460, 40, 121, 21))
        self.age_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.sex_comboBox = QComboBox(Form)
        self.sex_comboBox.addItem("")
        self.sex_comboBox.addItem("")
        self.sex_comboBox.setObjectName(u"sex_comboBox")
        self.sex_comboBox.setGeometry(QRect(270, 120, 111, 22))
        self.sex_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.item_comboBox = QComboBox(Form)
        self.item_comboBox.addItem("")
        self.item_comboBox.addItem("")
        self.item_comboBox.addItem("")
        self.item_comboBox.addItem("")
        self.item_comboBox.addItem("")
        self.item_comboBox.addItem("")
        self.item_comboBox.addItem("")
        self.item_comboBox.setObjectName(u"item_comboBox")
        self.item_comboBox.setGeometry(QRect(470, 120, 111, 22))
        self.item_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 120, 61, 21))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 120, 31, 21))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 120, 31, 21))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.subbmitButton.setText(QCoreApplication.translate("Form", u"submit", None))
        self.purpose_comboBox.setItemText(0, QCoreApplication.translate("Form", u"investment", None))
        self.purpose_comboBox.setItemText(1, QCoreApplication.translate("Form", u"gift", None))
        self.purpose_comboBox.setItemText(2, QCoreApplication.translate("Form", u"personal purchase", None))
        self.purpose_comboBox.setItemText(3, QCoreApplication.translate("Form", u"collector's purchase", None))
        self.purpose_comboBox.setItemText(4, QCoreApplication.translate("Form", u"occasional purchase", None))
        self.purpose_comboBox.setItemText(5, QCoreApplication.translate("Form", u"other", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">phone:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">mail:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">age:</span></p></body></html>", None))
        self.age_lineEdit.setText("")
        self.sex_comboBox.setItemText(0, QCoreApplication.translate("Form", u"M", None))
        self.sex_comboBox.setItemText(1, QCoreApplication.translate("Form", u"F", None))

        self.item_comboBox.setItemText(0, QCoreApplication.translate("Form", u"rings", None))
        self.item_comboBox.setItemText(1, QCoreApplication.translate("Form", u"necklaces", None))
        self.item_comboBox.setItemText(2, QCoreApplication.translate("Form", u"bracelets", None))
        self.item_comboBox.setItemText(3, QCoreApplication.translate("Form", u"earrings", None))
        self.item_comboBox.setItemText(4, QCoreApplication.translate("Form", u"watches", None))
        self.item_comboBox.setItemText(5, QCoreApplication.translate("Form", u"collector's item", None))
        self.item_comboBox.setItemText(6, QCoreApplication.translate("Form", u"decorations", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">purpose:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">sex:</span></p><p><br/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">item:</span></p></body></html>", None))
    # retranslateUi

