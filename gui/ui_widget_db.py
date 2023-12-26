

################################################################################
## Form generated from reading UI file 'widget_db.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(680, 413)
        Form.setFixedSize(680, 413)
        Form.setStyleSheet(u"QWidget {	background-color: #caf0f8\n"
"}")
        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(150, 350, 161, 41))
        self.addButton.setStyleSheet(u"QPushButton {\n"
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
        self.deleteButton = QPushButton(Form)
        self.deleteButton.setObjectName(u"edditButton")
        self.deleteButton.setGeometry(QRect(380, 350, 151, 41))
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
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
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 20, 641, 311))
        self.textBrowser.setStyleSheet(u"QTextBrowser{ \n"
"font-family: \"Times New Roman\", serif; \n"
"background-color: #f8f9fa; \n"
"border: 1px solid #343a40; }")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"add", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"delete", None))


