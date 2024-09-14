from bs4 import BeautifulSoup
import requests
import pandas as pd

#Extraer la información de Boyaca
html_text = requests.get('https://cifras.biodiversidad.co/boyaca').text
soup = BeautifulSoup(html_text, 'lxml')

#Extraer la información conjunto de las tarjetas (cards) de Boyaca
data_container = soup.find_all('div', class_ = 'bg-white flex flex-col justify-between text-black-2 py-3 px-4 w-auto gap-y-2 shadow-default hover:shadow-select')
#print(data_container)

dato_pais = []
dato_name = []
data_rows1 = []
data_rows2 = []
data_valors1 = []
data_valors2 = []

# Iterar sobre los elementos y extraer la información de Boyaca
for data in data_container:
    pais = data.find('p', class_ = 'text-sm italic')
    nombre = data.find('a')
    
    data_pais = pais.text.strip()
    data_nombre = nombre.text.strip()
    # Buscar las tablas dentro de cada contenedor
    data_tables = data('table') # Esto devuelve una lista de tablas
    
    for table in data_tables:
        #print(table.prettify()) # Imprimir cada tabla con formato legible
        rows = table.find_all('th') # Buscar todas las filas de la tabla
        if len(rows) > 1:
            data_row1 = rows[0].text.strip()
            data_row2 = rows[1].text.strip()
            data_row3 = rows[2].text.strip()
            data_row4 = rows[3].text.strip()
            #print(data_row3)
            data_rows1.append(data_row1) 
            data_valors1.append(data_row2)  
            data_rows2.append(data_row3)
            data_valors2.append(data_row4)
    
    dato_pais.append(data_pais)   
    dato_name.append(data_nombre)
   
df=pd.DataFrame({
    'nombre_pais':dato_pais,
    'nombre':dato_name,
    'item1':data_rows1,
    'valor1':data_valors1,
    'item2':data_rows2,
    'valor2':data_valors2,
})

#Filtración de los datos de CO de Boyaca
filtro_df = df[(df['nombre_pais'] == 'País de publicación: CO') & (df['valor1'] >= '100')] 
filtro_df.loc[filtro_df['nombre_pais'] == 'País de publicación: CO', 'nombre_pais'] = 'Colombia' #Reemplazar el dato de CO por Colombia
#print(filtro_df)

#Pasar los datos del dataframe y el filtro de Boyaca a un csv
df.to_csv('datosextraidos.csv', index=False)
filtro_df.to_csv('filtroextraidos.csv', index=False)

#----------------------------------------------------------------------------------------------------------
#Extraer la información de Cundinamarca
html_text_cund = requests.get('https://cifras.biodiversidad.co/cundinamarca').text
soup_cund = BeautifulSoup(html_text_cund, 'lxml')

#Extraer la información conjunto de las tarjetas (cards) de Cundinamarca
data_container_cund = soup_cund.find_all('div', class_ = 'bg-white flex flex-col justify-between text-black-2 py-3 px-4 w-auto gap-y-2 shadow-default hover:shadow-select')
#print(data_container_cund)

dato_pais = []
dato_name = []
data_rows1 = []
data_rows2 = []
data_valors1 = []
data_valors2 = []

# Iterar sobre los elementos y extraer la información de Cundinamarca
for data in data_container_cund:
    pais = data.find('p', class_ = 'text-sm italic')
    nombre = data.find('a')
    
    data_pais = pais.text.strip()
    data_nombre = nombre.text.strip()
    # Buscar las tablas dentro de cada contenedor
    data_tables = data('table') # Esto devuelve una lista de tablas
    
    for table in data_tables:
        #print(table.prettify()) # Imprimir cada tabla con formato legible
        rows = table.find_all('th') # Buscar todas las filas de la tabla
        if len(rows) > 1:
            data_row1 = rows[0].text.strip()
            data_row2 = rows[1].text.strip()
            data_row3 = rows[2].text.strip()
            data_row4 = rows[3].text.strip()
            #print(data_row3)
            data_rows1.append(data_row1) 
            data_valors1.append(data_row2)  
            data_rows2.append(data_row3)
            data_valors2.append(data_row4)
    
    dato_pais.append(data_pais)   
    dato_name.append(data_nombre)
   
df_cundinamarca=pd.DataFrame({
    'nombre_pais':dato_pais,
    'nombre':dato_name,
    'item1':data_rows1,
    'valor1':data_valors1,
    'item2':data_rows2,
    'valor2':data_valors2,
})

#print(df_cundinamarca)

#convertir la variable en numerico
#df['valor1'] = pd.to_numeric(df['valor1'], errors='coerce')

#Filtración de los datos de CO de Boyaca
filtro_Cundinamarca = df_cundinamarca[(df_cundinamarca['nombre_pais'] == 'País de publicación: CO')] 
filtro_Cundinamarca.loc[filtro_Cundinamarca['nombre_pais'] == 'País de publicación: CO', 'nombre_pais'] = 'Colombia' #Reemplazar el dato de CO por Colombia
#print(filtro_Cundinamarca)

#Reemplazar el dato de nombre_pais por cada uno de los paises
#df_cundinamarca.loc[df_cundinamarca['nombre_pais'] == 'País de publicación: CO', 'nombre_pais'] = 'Colombia' 
#print(df_cundinamarca)

#Pasar los datos del dataframe y el filtro de Cundinamarca a un csv
df_cundinamarca.to_csv('datos_cundinamarca.csv', index=False)
filtro_Cundinamarca.to_csv('filtro_cundinamarca.csv', index=False)
print(filtro_Cundinamarca)