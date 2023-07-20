import pika
import sys
import pandas

excel_data_df = pandas.read_excel('base_datos.xlsx', sheet_name='Employees')

filaini = input("Ingrese fila inicio \n")
filafin = input("Ingrese fila final \n")

filaini = int(filaini)
filafin = int(filafin)

df_rango = excel_data_df.loc[(excel_data_df['ID'] >= filaini) & (excel_data_df['ID'] <= filafin)]


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
message = str(df_rango)

channel.basic_publish(exchange='logs', routing_key='form', body=message)
print(" [x] Sent %r" % message)
connection.close()
