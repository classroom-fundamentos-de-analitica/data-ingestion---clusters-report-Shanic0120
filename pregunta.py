"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import re
import pandas as pd
import numpy as np

def ingest_data():
    archivo=pd.read_fwf(
    "clusters_report.txt",
    colspecs="infer",
    widths=[8,10,20,100])
    datos=archivo.drop([0,1],axis=0)
    datos = pd.DataFrame(datos)
    datos.columns=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave']
    newdf=pd.DataFrame(columns=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave'])
    c=0
    for i in range(len(datos)):
        if not isinstance(datos.iloc[i]['cluster'],float): 
            newdf.loc[c]=datos.iloc[i]
            c+=1
        else:      
            newdf.iloc[c-1]['principales_palabras_clave']+=" "+datos.iloc[i]['principales_palabras_clave']

    newdf['cantidad_de_palabras_clave'] = newdf['cantidad_de_palabras_clave'].astype('int')       
    newdf['cantidad_de_palabras_clave'] = newdf['cantidad_de_palabras_clave'].astype('int')
    newdf['porcentaje_de_palabras_clave']=newdf['porcentaje_de_palabras_clave'].apply(lambda i:float(i.split(',')[0])+float('0.'+i.split(',')[1][0]))
    newdf['principales_palabras_clave']=newdf['principales_palabras_clave'].apply(lambda x:x[:-1] if x[-1]=='.' else x)
    newdf['principales_palabras_clave']=newdf['principales_palabras_clave'].apply(lambda x:x.replace(',',', '))
    newdf['principales_palabras_clave']=newdf['principales_palabras_clave'].apply(lambda x:re.sub('\s+',' ',x))

    return newdf