import matplotlib.pyplot as plt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import  QMainWindow

import ui_widget_db
import ui_orders_add_window
import ui_customers_add_window
import ui_orders_delete_window
import ui_customers_delete_window
from ui_main_window import Ui_MainWindow

from functions import (connect_to_database, table_into_df, delete_from_database, add_order_to_database, create_pie_chart, create_bar_plot_with_price,
                       create_count_plot, creating_connected_df, add_customer_to_database, create_error_window, create_success_window,
                       make_prediction, prepare_prediction_data)

class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowTitle('DiamondShopAssistant')

        self.customer_window = None

        self.customers_data = ""
        self.orders_data = ""

        self.customer_pushButton.clicked.connect(self.customers_db_button_logic)
        self.orders_pushButton.clicked.connect(self.orders_db_button_logic)
        self.annual_t_pushButton.clicked.connect(self.annual_trends_button_logic)
        self.customers_t_pushButton.clicked.connect(self.customers_trends_button_logic)
        self.purpose_and_type_t_pushButton.clicked.connect(self.purpose_and_type_trends_button_logic)
        self.item_andtype_t_pushButton.clicked.connect(self.item_and_type_trends_button_logic)
        self.predict_pushButton.clicked.connect(self.predict_button_logic)

    def customers_db_button_logic(self):
        self.customer_db_window = QMainWindow()
        self.ui = ui_widget_db.Ui_Form()
        self.ui.setupUi(self.customer_db_window)
        self.customer_db_window.setWindowTitle("Customers Database")

        self.ui.addButton.clicked.connect(self.customers_add_button_logic)
        self.ui.deleteButton.clicked.connect(self.customers_delete_button_logic)

        self.customer_db_window.show()

        columns_customers = ["phone_number", 'mail', 'age', 'purpose', 'sex', 'age_group', 'item', 'id']
        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        df = table_into_df('customers', columns_customers, conn)

        self.customers_data = df.to_html(index=False, classes='table-auto')
        self.ui.textBrowser.setHtml(self.customers_data)

    def orders_db_button_logic(self):
        self.customer_db_window = QMainWindow()
        self.ui = ui_widget_db.Ui_Form()
        self.ui.setupUi(self.customer_db_window)
        self.customer_db_window.setWindowTitle("Orders Database")

        self.ui.deleteButton.clicked.connect(self.orders_delete_button_logic)
        self.ui.addButton.clicked.connect(self.orders_add_button_logic)

        self.customer_db_window.show()

        columns_orders = ['carat','cut','color', 'clarity', 'table', 'x', 'y', 'z',  'depth', 'price', 'client_id', 'year', 'id',]
        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        df = table_into_df("orders", columns_orders, conn)

        self.orders_date = df.to_html(index=False, classes='table-auto')
        self.ui.textBrowser.setHtml(self.orders_date)

    def customers_add_button_logic(self):
        self.add_window = QMainWindow()
        self.ui = ui_customers_add_window.Ui_Form()
        self.ui.setupUi(self.add_window)

        self.ui.subbmitButton.clicked.connect(self.customers_add_submitt_button_logic)

        self.add_window.show()

    def customers_delete_button_logic(self):
        self.delete_window = QMainWindow()
        self.ui = ui_customers_delete_window.Ui_Form()
        self.ui.setupUi(self.delete_window)

        self.ui.subbmitButton.clicked.connect(self.customers_delete_submitt_button_logic)

        self.delete_window.show()

    def orders_add_button_logic(self):
        self.add_window = QMainWindow()
        self.ui = ui_orders_add_window.Ui_Form()
        self.ui.setupUi(self.add_window)

        self.ui.subbmitButton.clicked.connect(self.orders_add_submitt_button_logic)

        self.add_window.show()

    def orders_delete_button_logic(self):
        self.delete_window = QMainWindow()
        self.ui = ui_orders_delete_window.Ui_Form()
        self.ui.setupUi(self.delete_window)

        self.ui.subbmitButton.clicked.connect(self.orders_delete_submitt_button_logic)

        self.delete_window.show()

    def orders_add_submitt_button_logic(self):
        carat = self.ui.carat_lineEdit.text()
        cut = self.ui.cut_comboBox.currentText()
        color = self.ui.color_comboBox.currentText()
        clarity = self.ui.clarity_comboBox.currentText()
        table = self.ui.table_lineEdit.text()
        x = self.ui.length_lineEdit.text()
        y = self.ui.width_lineEdit.text()
        z = self.ui.depth_lineEdit.text()
        price = self.ui.price_lineEdit.text()
        client_id = self.ui.client_id_lineEdit.text()
        year = self.ui.year_lineEdit.text()

        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        x = add_order_to_database(carat, cut, color, clarity, table, x, y, z, price, client_id, year, conn)
        if x == 0:
            create_error_window("Oops! Something went wrong. It looks like the data you provided is not the correct type. Please review and try again.")
        else:
            create_success_window("Orders successfully added to the database.")
            self.add_window.close()

    def orders_delete_submitt_button_logic(self,):
        order_id = self.ui.id_lineEdit.text()

        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"])
        x = delete_from_database(order_id, 'orders', conn)
        if x == 0:
            create_error_window("An error occurred. You enterned incorrect order ID")
        else:
            create_success_window(f"Order with ID {order_id} successfully deleted from database.")
            self.delete_window.close()

    def customers_add_submitt_button_logic(self):
        phone = self.ui.phone_lineEdit.text()
        mail = self.ui.mail_lineEdit.text()
        age = self.ui.age_lineEdit.text()
        purpose = self.ui.purpose_comboBox.currentText()
        sex = self.ui.sex_comboBox.currentText()
        item = self.ui.item_comboBox.currentText()

        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        x = add_customer_to_database(phone, mail, age, purpose, sex, item,conn)
        if x == 0:
            create_error_window("Oops! Something went wrong. It looks like the data you provided is not the correct type. Please review and try again.")
        else:
            create_success_window("Customer successfully added to the database.")
            self.add_window.close()

    def customers_delete_submitt_button_logic(self):
        customer_id = self.ui.id_lineEdit.text()

        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        x = delete_from_database(customer_id, 'customers', conn)
        if x == 0:
            create_error_window("Oops! Something went wrong. It looks like the Order ID you provided is not the correct type. Please review and try again.")
        else:
            create_success_window(f"Customer with ID {customer_id} successfully deleted from database.")
            self.delete_window.close()

    def annual_trends_button_logic(self):
        columns = ['carat','cut','color', 'clarity', 'table_', 'x', 'y', 'z',  'depth', 'price', 'client_id', 'year_', 'id',]
        conn = connect_to_database(["localhost", "root", "lizus123", "diamondshop"]) # local database info
        df = table_into_df("orders", columns, conn)

        create_pie_chart(df, "cut", "year_")
        create_pie_chart(df, "color", "year_")
        create_pie_chart(df, "clarity", "year_")
        create_bar_plot_with_price(df, 'year_')

        plt.show()

    def customers_trends_button_logic(self):
        columns = ["phone_number", 'mail', 'age', 'purpose', 'sex', 'age_group', 'item', 'id']
        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        df = table_into_df('customers', columns, conn)

        create_pie_chart(df, "purpose", "age_group")
        create_pie_chart(df, "purpose", "sex")
        create_pie_chart(df, "item", "age_group")
        create_pie_chart(df, "item", "sex")

        plt.show()

    def purpose_and_type_trends_button_logic(self):
        columns_1 = ['carat','cut','color', 'clarity', 'table_', 'x', 'y', 'z',  'depth', 'price', 'client_id', 'year_', 'id',]
        columns_2 = ["phone_number", 'mail', 'age', 'purpose', 'sex', 'age_group', 'item', 'id']
        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        df_1 = table_into_df("orders", columns_1, conn)
        df_2 = table_into_df("customers", columns_2, conn)
        final_df = creating_connected_df(df_1, df_2, ["color", "cut", "clarity", "price"], ["item", "purpose"])

        create_count_plot(final_df, "color", "purpose")
        create_count_plot(final_df, "cut", "purpose")
        create_count_plot(final_df, "clarity", "purpose")
        create_bar_plot_with_price(final_df, 'purpose')

        plt.show()

    def item_and_type_trends_button_logic(self):
        columns_1 = ['carat', 'cut', 'color', 'clarity', 'table_', 'x', 'y', 'z', 'depth', 'price', 'client_id','year_', 'id', ]
        columns_2 = ["phone_number", 'mail', 'age', 'purpose', 'sex', 'age_group', 'item', 'id']
        conn = connect_to_database(["localhost", "root", "lizus123", "diamondsshop"]) # local database info
        df_1 = table_into_df("orders", columns_1, conn)
        df_2 = table_into_df("customers", columns_2, conn)
        final_df = creating_connected_df(df_1, df_2, ["color", "cut", "clarity", "price"], ["item", "purpose"])

        create_count_plot(final_df, "color", "item")
        create_count_plot(final_df, "cut", "item")
        create_count_plot(final_df, "clarity", "item")
        create_bar_plot_with_price(final_df, 'item')

        plt.show()

    def predict_button_logic(self):
        clarity = self.clarity_comboBox.currentText()
        color = self.color_comboBox.currentText()
        try:
            carat = float(self.carat_lineEdit.text())
            x = float(self.length_lineEdit.text())
            y = float(self.width_lineEdit.text())
            z = float(self.depth_lineEdit.text())
        except:
            create_error_window("Oops! An error occurred. It seems like you entered data of an incorrect type. Please double-check and try again.")
        else:
            data = [carat, f"clarity_{clarity}", f"color_{color}", x, y, z]
            model_path = r"C:\Users\lilto\Desktop\DS\Projects\DiamondShopAssistant\model\finalized_model.sav"

            prepared_data = prepare_prediction_data(data)
            predictions = make_prediction(model_path, prepared_data)

            font = QFont("Times New Roman", 20)
            self.price_textBrowser.setFont(font)

            self.price_textBrowser.setText("         " + str(round(predictions, 2)) + " $")