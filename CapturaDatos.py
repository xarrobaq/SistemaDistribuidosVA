import pandas

excel_data_df = pandas.read_excel('base_datos.xlsx', sheet_name='Employees')

filaini = input("Ingrese fila inicio \n")
filafin = input("Ingrese fila final \n")

filaini = int(filaini)
filafin = int(filafin)

df_rango = excel_data_df.loc[(excel_data_df['ID'] >= filaini) & (excel_data_df['ID'] <= filafin)]

df_rango.to_json('file.json')

#print('Excel Sheet to JSON:\n', df)