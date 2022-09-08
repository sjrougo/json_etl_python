import json
import requests

import matplotlib.pyplot as plt

def fetch():
    resultados = []
    dataset = []
    dicc = {}
    # Ejercicio de consumo de datos por API
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    data = response.json()
    for dato in data['results']:
        resultados.append(dato)
        #print(dato, '\n')
    #resultados = response['results']
    #dataset = [resultados[x] for x in range(0, len(resultados)) if resultados[x]["currency_id"] == 'ARS' ]
    #{"price": 1250, "condition": "used"}
    for x in range(0, len(resultados)):
        if resultados[x]["currency_id"] == 'ARS':
            dicc = {'price': resultados[x]['price'], 'condition': resultados[x]['condition']}
            dataset.append(dicc)
    #print(dataset)
    return dataset

def transform(dataset, min, max):
    min_count = None
    min_max_count = None
    max_count = None
    
    lista_min = [dataset[x] for x in range(0, len(dataset)) if dataset[x]['price'] < min]
    lista_med = [dataset[x] for x in range(0, len(dataset)) if dataset[x]['price'] > min and dataset[x]['price'] < max]
    lista_max = [dataset[x] for x in range(0, len(dataset)) if dataset[x]['price'] > max]
    
    min_count = len(lista_min)
    min_max_count = len(lista_med)
    max_count = len(lista_max)
    
    return [min_count, min_max_count, max_count]

def report (lista):
    
    fig = plt.figure()
    fig.suptitle('Alquileres MELI - Mendoza', fontsize=16)
    fig.set_facecolor('whitesmoke')
    ax = fig.add_subplot()
    etiquetas = ['< a 20000', 'Entre 20000 y 200000', '> a 200000']

    ax.pie(lista, labels = etiquetas)
    ax.set_facecolor('lightgreen')

    ax.legend()
    ax.grid()
    plt.show()



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    fetch()
    print(transform(fetch(), 20000, 200000))
    report(transform(fetch(), 20000, 200000))
    print("terminamos")
