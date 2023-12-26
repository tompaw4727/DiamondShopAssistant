
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 618)
        MainWindow.setFixedSize(708, 618)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #caf0f8\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color: #caf0f8\n"
"}")
        self.orders_pushButton = QPushButton(self.centralwidget)
        self.orders_pushButton.setObjectName(u"orders_pushButton")
        self.orders_pushButton.setGeometry(QRect(490, 530, 171, 51))
        self.orders_pushButton.setStyleSheet(u"QPushButton {\n"
"font-family: \"Times New Roman\", serif;\n"
"    font-size: 14px;\n"
"    color: #000;\n"
"    border: 2px solid #343a40;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"	background: #f8f9fa\n"
"    }\n"
"QPushButton:hover {\n"
"    background: #d3d3d3\n"
"}")
        self.customer_pushButton = QPushButton(self.centralwidget)
        self.customer_pushButton.setObjectName(u"customer_pushButton")
        self.customer_pushButton.setGeometry(QRect(490, 460, 171, 51))
        self.customer_pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.predict_pushButton = QPushButton(self.centralwidget)
        self.predict_pushButton.setObjectName(u"predict_pushButton")
        self.predict_pushButton.setGeometry(QRect(470, 380, 211, 61))
        self.predict_pushButton.setStyleSheet(u"QPushButton {\n"
"	font-family: \"Times New Roman\", serif;\n"
"    color: #000;\n"
"	font-size: 25px;\n"
"    border: 2px solid #343a40;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: #f8f9fa\n"
"    }\n"
"QPushButton:hover {\n"
"    background: #d3d3d3;\n"
"}\n"
"\n"
"        \n"
"")
        self.customers_t_pushButton = QPushButton(self.centralwidget)
        self.customers_t_pushButton.setObjectName(u"customers_t_pushButton")
        self.customers_t_pushButton.setGeometry(QRect(30, 530, 171, 51))
        self.customers_t_pushButton.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Times New Roman\", serif;\n"
"    color: #000;\n"
"   font-size: 14px;\n"
"    border: 2px solid #343a40;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"	background: #f8f9fa\n"
"    }\n"
"QPushButton:hover {\n"
"    background: #d3d3d3\n"
"}")
        self.item_andtype_t_pushButton = QPushButton(self.centralwidget)
        self.item_andtype_t_pushButton.setObjectName(u"item_andtype_t_pushButton")
        self.item_andtype_t_pushButton.setGeometry(QRect(260, 530, 171, 51))
        self.item_andtype_t_pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.purpose_and_type_t_pushButton = QPushButton(self.centralwidget)
        self.purpose_and_type_t_pushButton.setObjectName(u"purpose_and_type_t_pushButton")
        self.purpose_and_type_t_pushButton.setGeometry(QRect(260, 460, 171, 51))
        self.purpose_and_type_t_pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.annual_t_pushButton = QPushButton(self.centralwidget)
        self.annual_t_pushButton.setObjectName(u"annual_t_pushButton")
        self.annual_t_pushButton.setGeometry(QRect(30, 460, 171, 51))
        self.annual_t_pushButton.setStyleSheet(u"QPushButton {\n"
"font-family: \"Times New Roman\", serif;\n"
"    color: #000;\n"
"    font-size: 14px;\n"
"    border: 2px solid #343a40;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"	background: #f8f9fa\n"
"    }\n"
"QPushButton:hover {\n"
"    background: #d3d3d3\n"
"}")
        self.carat_lineEdit = QLineEdit(self.centralwidget)
        self.carat_lineEdit.setObjectName(u"carat_lineEdit")
        self.carat_lineEdit.setGeometry(QRect(110, 150, 113, 21))
        self.carat_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 150, 41, 21))
        self.label.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 150, 41, 20))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 150, 49, 21))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.length_lineEdit = QLineEdit(self.centralwidget)
        self.length_lineEdit.setObjectName(u"length_lineEdit")
        self.length_lineEdit.setGeometry(QRect(110, 240, 113, 21))
        self.length_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	background-color: #f8f9fa;\n"
"	border: 1px solid #343a40;\n"
"}")
        self.width_lineEdit = QLineEdit(self.centralwidget)
        self.width_lineEdit.setObjectName(u"width_lineEdit")
        self.width_lineEdit.setGeometry(QRect(330, 240, 113, 21))
        self.width_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.depth_lineEdit = QLineEdit(self.centralwidget)
        self.depth_lineEdit.setObjectName(u"depth_lineEdit")
        self.depth_lineEdit.setGeometry(QRect(550, 240, 113, 21))
        self.depth_lineEdit.setStyleSheet(u"QLineEdit {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 240, 51, 21))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, 240, 51, 20))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 240, 49, 21))
        self.label_8.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 320, 121, 20))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	font-family: \"Times New Roman\", serif;\n"
"}")
        self.color_comboBox = QComboBox(self.centralwidget)
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.setObjectName(u"color_comboBox")
        self.color_comboBox.setGeometry(QRect(550, 150, 111, 22))
        self.color_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.clarity_comboBox = QComboBox(self.centralwidget)
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.addItem("")
        self.clarity_comboBox.setObjectName(u"clarity_comboBox")
        self.clarity_comboBox.setGeometry(QRect(330, 150, 111, 22))
        self.clarity_comboBox.setStyleSheet(u"QComboBox {\n"
"font-family: \"Times New Roman\", serif;\n"
"	border: 1px solid #343a40;\n"
"	background-color: #f8f9fa\n"
"}")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 141, 111))
        self.label_10.setStyleSheet(u"image: url(:/nowyPrzedrostek/diamond.svg)")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(150, 40, 481, 51))
        self.label_11.setStyleSheet(u"QLabel {\n"
"	background-color: #caf0f8;\n"
"	font-family: \"Times New Roman\", serif;\n"
"\n"
"}")
        self.price_textBrowser = QTextBrowser(self.centralwidget)
        self.price_textBrowser.setObjectName(u"price_textBrowser")
        self.price_textBrowser.setGeometry(QRect(230, 310, 231, 41))
        self.price_textBrowser.setStyleSheet(u"QTextBrowser{font-family: \"Times New Roman\", serif;\n"
"	background-color: #f8f9fa;\n"
"	border: 1px solid #343a40;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/nowyPrzedrostek/diamond-jewel-svgrepo-com.svg\" /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.orders_pushButton.setText(QCoreApplication.translate("MainWindow", u"Orders Data Base", None))
        self.customer_pushButton.setText(QCoreApplication.translate("MainWindow", u"Customers Data Base ", None))
        self.predict_pushButton.setText(QCoreApplication.translate("MainWindow", u"Predict Price", None))
        self.customers_t_pushButton.setText(QCoreApplication.translate("MainWindow", u"Custommers Trends", None))
        self.item_andtype_t_pushButton.setText(QCoreApplication.translate("MainWindow", u"Item and Type Trends", None))
        self.purpose_and_type_t_pushButton.setText(QCoreApplication.translate("MainWindow", u"Purpose and Type Trends", None))
        self.annual_t_pushButton.setText(QCoreApplication.translate("MainWindow", u"Annual Trends", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Carat:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Color:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Clarity :</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Length:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Width:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Depth:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Predicted Price:</span></p></body></html>", None))
        self.color_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"J", None))
        self.color_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"I", None))
        self.color_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"D", None))
        self.color_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"H", None))
        self.color_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.color_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"E", None))
        self.color_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))

        self.clarity_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"I1", None))
        self.clarity_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"SI2", None))
        self.clarity_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"SI1", None))
        self.clarity_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"VS2", None))
        self.clarity_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"VS1", None))
        self.clarity_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"VVS2", None))
        self.clarity_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"VVS1", None))
        self.clarity_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"IF", None))

#if QT_CONFIG(whatsthis)
        self.label_10.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/nowyPrzedrostek/diamond-jewel-svgrepo-com.svg\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">DiamondShopAssistant</span></p><p align=\"center\"><span style=\" font-size:36pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:36pt;\"><br/></span></p></body></html>", None))
        self.price_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Times New Roman','serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">$</span></p></body></html>", None))
    # retranslateUi

