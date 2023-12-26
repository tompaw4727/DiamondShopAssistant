import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
import pickle
from PySide6.QtWidgets import QMessageBox
import matplotlib

matplotlib.use('TkAgg')

def connect_to_database(database_info):
    conn = mysql.connector.connect(
            host = database_info[0],  #name of host of your local mysql database
            user = database_info[1],  #name of root of yout local database
            password = database_info[2],  #name of password of your root
            database = database_info[3]  #name of your mysql local database
        )

    return conn

def table_into_df(table_name, columns, conn):

    cursor = conn.cursor()
    show = 'select * from ' + table_name
    cursor.execute(show)
    results = cursor.fetchall()

    df = pd.DataFrame(columns=columns, data=results)

    cursor.close()
    conn.close()

    return df

def add_customer_to_database(phone, mail, age, purpose, sex, item, conn):
    try:
        cursor = conn.cursor()

        add = f"insert into customers values('{phone}', '{mail}', {age}, '{purpose}', '{sex}', null, '{item}', null );"

        cursor.execute(add)
        conn.commit()

    except mysql.connector.Error as e:
        return 0
    else:
        return 1
    finally:
        cursor.close()
        conn.close()

def add_order_to_database(carat, cut, color, clarity, table, x, y, z, price, client_id, year, conn):
    try:
        cursor = conn.cursor()

        add = f"insert into orders values({carat}, '{cut}', '{color}', '{clarity}', {table}, {x}, {y}, {z}, null, {price}, {client_id}, {year}, null );"

        cursor.execute(add)
        conn.commit()

    except mysql.connector.Error as e:
        return 0
    else:
        return 1
    finally:
        cursor.close()
        conn.close()

def delete_from_database(id, database_name, conn):
    try:
        cursor = conn.cursor()

        check_existence = f"select * from {database_name} where id={id};"
        cursor.execute(check_existence)
        reult_of_existing = cursor.fetchone()

        if reult_of_existing:
            delete = "delete from " + database_name + f" where id={id};"

            cursor.execute(delete)
            conn.commit()
            return 1
        else:
            return 0
    except mysql.connector.Error as e:
        return 0
    finally:
        cursor.close()
        conn.close()

def creating_connected_df(df_1, df_2, columns_from_df_1, columns_from_df_2):
    tp_df_1 = df_1[columns_from_df_1]
    tp_df_2 = df_2[columns_from_df_2]
    final_df = pd.concat([tp_df_1, tp_df_2], axis=1)

    return final_df

def create_pie_chart(df, types_feature, by_feature):
    list_of_by_feature = df[by_feature].unique().tolist()

    types_labels = df[types_feature].unique().tolist()
    types_data = df.groupby(by_feature)[types_feature].value_counts().to_list()

    types_data_nested = [types_data[i:i + len(types_labels)] for i in range(0, len(types_data), 5)]

    plt.figure(figsize=(15, 6))

    for i in range(len(list_of_by_feature)):
        plt.subplot(1, len(list_of_by_feature), i + 1)
        plt.pie(types_data_nested[i], colors=sns.color_palette('bright'), autopct='%.0f%%')
        plt.title(f"{list_of_by_feature[i]}")
    plt.suptitle(f"Distribution of Diamond Orders by {types_feature.capitalize()} for a Given {by_feature.capitalize()}.")
    plt.legend(types_labels, title=f"{types_feature.capitalize()}", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

def create_count_plot(df, types_feature, by_feature):
    plt.figure(figsize=(15, 5))

    sns.countplot(data=df, x=by_feature, hue=types_feature)

    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', )
    plt.xlabel(f"{by_feature.capitalize()}'s Type")
    plt.ylabel('Count ')
    if by_feature == "purpose":
        plt.title(f'Quantity Distribution of Purchase Purposes for Diamonds by {types_feature.capitalize()}', fontsize=16)
    elif by_feature == "item":
        plt.title(f'Item-specific Diamond Purchases by {types_feature.capitalize()} Distribution', fontsize=16)
    else:
        plt.title(f'', fontsize=16)

def create_bar_plot_with_price(df, x):
    price_data = df.groupby(x)["price"].mean().reset_index()
    price_data["price"] = price_data["price"].round(2)

    plt.figure(figsize=(9, 5))
    sns.barplot(x=x, y="price", data=price_data, palette="bright", hue="price", dodge=False)

    plt.legend(title="Price", bbox_to_anchor=(1.0, 1), loc='upper left')
    plt.title(f'Average Diamonds Price for {x.capitalize()}')
    plt.xlabel(x.capitalize())
    plt.ylabel('Price')

    plt.tight_layout()

def create_error_window(message):
    error_window = QMessageBox()
    error_window.setIcon(QMessageBox.Critical)
    error_window.setWindowTitle("Error")
    error_window.setText(message)
    error_window.addButton(QMessageBox.Ok)
    button = error_window.exec_()

def create_success_window(message):
    success_window = QMessageBox()
    success_window.setIcon(QMessageBox.Information)
    success_window.setWindowTitle("Success")
    success_window.setText(message)
    success_window.addButton(QMessageBox.Ok)
    button = success_window.exec_()

def set_cat_feature(df, x, columns):
    if x in columns:
        df.at[0, x] = 1
        columns.remove(x)
        for column in columns:
            df.at[0, column] = 0

    return df

def make_prediction(model_path, data):
    loaded_model = pickle.load(open(model_path, 'rb'))
    result = loaded_model.predict(data)

    return result[0]

def prepare_prediction_data(data):
    column_1 = ['color_D', 'color_E', 'color_F', 'color_G', 'color_H', 'color_I', 'color_J']
    column_2 = ['clarity_I1', 'clarity_IF', 'clarity_SI1', 'clarity_SI2', 'clarity_VS1', 'clarity_VS2', 'clarity_VVS1',
                'clarity_VVS2']

    all_columns = ['carat', 'x', 'y', 'z', 'color_D', 'color_E', 'color_F', 'color_G', 'color_H', 'color_I', 'color_J',
                   'clarity_I1', 'clarity_IF', 'clarity_SI1', 'clarity_SI2', 'clarity_VS1', 'clarity_VS2',
                   'clarity_VVS1',
                   'clarity_VVS2']

    tp_df = pd.DataFrame(columns=all_columns)

    tp_df = set_cat_feature(tp_df, data[2], column_1)
    tp_df = set_cat_feature(tp_df, data[1], column_2)
    tp_df = tp_df.apply(pd.to_numeric)
    tp_df.loc[0, 'carat'] = data[0]
    tp_df.loc[0, 'x'] = data[3]
    tp_df.loc[0, 'y'] = data[4]
    tp_df.loc[0, 'z'] = data[5]

    return tp_df