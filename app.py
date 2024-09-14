from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json
import csv

app=Flask(__name__)

#Tarjetas
# Función para cargar los datos desde un archivo CSV
def leer_datos_csv(archivo):
    cards = []
    with open(archivo, newline='', encoding='utf-8') as archivocsv:
        reader = csv.DictReader(archivocsv)
        for row in reader:
            cards.append({
                'nombre_pais': row['nombre_pais'],  # Nombre de las columnas en tu CSV
                'nombre': row['nombre'],
                'item1': row['item1'],
                'valor1': row['valor1'],
                'item2': row['item2'],
                'valor2': row['valor2']
            })
    return cards

#Graficos
# Función para cargar datos desde dos archivos CSV
def cargar_datos():
    df_boyaca = pd.read_csv('consolidado_boyaca.csv')  # Archivo CSV para la sección de boyaca
    df_cundinamarca = pd.read_csv('consolidado_cundinamarca.csv')  # Archivo CSV para la sección de cundinamarca
    return df_boyaca, df_cundinamarca

# Función para generar gráficos a partir de los DataFrames
def generar_graficos(df_boyaca, df_cundinamarca):
    # Sección Boyaca
    torta1_fig_boyaca = px.pie(df_boyaca, values='Porcentaje_Obs', names='Tipo_Organización', title='Observaciones Aportados por Tipo de Organizaciones')
    torta2_fig_boyaca = px.pie(df_boyaca, values='Porcentaje_Esp', names='Tipo_Organización', title='Especies exploradas por Tipo de Organizaciones')
    barras_fig_boyaca = px.bar(df_boyaca, x='Tipo_Organización', y='Observaciones', title='Observaciones por Tipo de Organización', color='Tipo_Organización')
    lineas_fig_boyaca = px.line(df_boyaca, x='Tipo_Organización', y='Especies', title='Especies por Tipo de Organización')

    # Sección Cundinmarca
    torta1_fig_cundinamarca = px.pie(df_cundinamarca, values='Porcentaje_Obs', names='Tipo_Organización', title='Observaciones Aportados por Tipo de Organizaciones')
    torta2_fig_cundinamarca = px.pie(df_cundinamarca, values='Porcentaje_Esp', names='Tipo_Organización', title='Especies exploradas por Tipo de Organizaciones')
    barras_fig_cundinamarca = px.bar(df_cundinamarca, x='Tipo_Organización', y='Observaciones', title='Observaciones por Tipo de Organización', color='Tipo_Organización')
    lineas_fig_cundinamarca = px.line(df_cundinamarca, x='Tipo_Organización', y='Especies', title='Especies por Tipo de Organización')

    # Convertir gráficos a JSON para ser utilizados en JavaScript
    return {
        'Graf_Boyaca': [
            json.loads(pio.to_json(torta1_fig_boyaca)),
            json.loads(pio.to_json(torta2_fig_boyaca)),
            json.loads(pio.to_json(barras_fig_boyaca)),
            json.loads(pio.to_json(lineas_fig_boyaca))
        ],
        'Graf_Cundinamarca': [
            json.loads(pio.to_json(torta1_fig_cundinamarca)),
            json.loads(pio.to_json(torta2_fig_cundinamarca)),
            json.loads(pio.to_json(barras_fig_cundinamarca)),
            json.loads(pio.to_json(lineas_fig_cundinamarca))
        ]
    }

#Rutas
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def index_2():
    return render_template('index.html')
@app.route('/mapas.html')
def mapas():
    return render_template('mapas.html')
@app.route('/boyaca.html')
def boyaca():
    return render_template('boyaca.html')
@app.route('/cundinamarca.html')
def cundinamarca():
    return render_template('cundinamarca.html')
@app.route('/dashboard.html')
def dashboard():
    #Tarjetas
    # Cargar los datos de dos conjuntos de tarjetas
    cards_1 = leer_datos_csv('filtroextraidos.csv')  #primer archivo
    cards_2 = leer_datos_csv('filtro_cundinamarca.csv') #segundo archivo
    
    #Graficos
    # Cargar los datos desde los dos archivos CSV
    df_boyaca, df_cundinamarca = cargar_datos()
    # Generar gráficos
    graficos = generar_graficos(df_boyaca, df_cundinamarca)
    
    return render_template('dashboard.html', cards_1=cards_1, cards_2=cards_2, graficos=graficos)
@app.route('/contactenos.html')
def contactenos():
    return render_template('contactenos.html')
@app.route('/suscribirse.html')
def suscribirse():
    return render_template('suscribirse.html')
@app.route('/pqrs.html')
def pqrs():
    return render_template('pqrs.html')

if __name__=='__main__':
    app.run(debug=True)