"""


UNDER COSNTRUCTION

"""

import pandas as pd
import matplotlib.pyplot as plt



def calcular_tipo_cambio_implícito(precios, plazos):
    """
    Calcula el tipo de cambio implícito para un conjunto de instrumentos financieros.

    :param precios: DataFrame con precios de los instrumentos en diferentes monedas y plazos.
    :param plazos: Lista de los plazos a considerar (CI, 24h, 48h).
    :return: DataFrame con los tipos de cambio implícitos calculados.
    """
    resultados = pd.DataFrame()

    for plazo in plazos:
        for i in range(len(precios)):
            for j in range(len(precios)):
                if i != j:
                    tipo_cambio = precios.iloc[i][plazo] / precios.iloc[j][plazo]
                    resultados = resultados.append({
                        'Instrumento1': precios.index[i],
                        'Instrumento2': precios.index[j],
                        'Plazo': plazo,
                        'TipoCambioImplícito': tipo_cambio
                    }, ignore_index=True)

    return resultados

def combinaciones_tipo_cambio_implícito(precios, plazos):
    """
    Calcula todas las combinaciones posibles de tipos de cambio implícito.

    :param precios: DataFrame con precios de los instrumentos en diferentes monedas y plazos.
    :param plazos: Lista de los plazos a considerar (CI, 24h, 48h).
    :return: DataFrame con todas las combinaciones de tipos de cambio implícitos.
    """
    # Esta función se puede expandir para calcular combinaciones más complejas
    return calcular_tipo_cambio_implícito(precios, plazos)

def mejores_opciones_tipo_cambio(resultados, top_n=5):
    """
    Selecciona y muestra las mejores opciones de tipo de cambio implícito.

    :param resultados: DataFrame con los tipos de cambio implícitos calculados.
    :param top_n: Número de mejores opciones para mostrar.
    :return: DataFrame con las top_n mejores opciones.
    """
    mejores = resultados.sort_values(by='TipoCambioImplícito', ascending=False).head(top_n)

    # Visualización de los resultados
    plt.figure(figsize=(10, 6))
    plt.barh(mejores['Instrumento1'] + '/' + mejores['Instrumento2'], mejores['TipoCambioImplícito'])
    plt.xlabel('Tipo de Cambio Implícito')
    plt.title(f'Top {top_n} Mejores Opciones de Tipo de Cambio Implícito')
    plt.show()

    return mejores

# Ejemplo de uso (se necesitarán datos reales para funcionar correctamente)
precios_ejemplo = pd.DataFrame({
    'CI': [25.5, 30.75, 40, 50], 
    '24h': [26, 31, 41, 51], 
    '48h': [27, 32, 42, 52]
}, index=['GD30', 'GD30D', 'Instrumento3', 'Instrumento4'])
plazos_ejemplo = ['CI', '24h', '48h']

# Calcular tipos de cambio implícito
resultados_tc = calcular_tipo_cambio_implícito(precios_ejemplo, plazos_ejemplo)

# Calcular combinaciones de tipos de cambio implícito
resultados_combinaciones = combinaciones_tipo_cambio_implícito(precios_ejemplo, plazos_ejemplo)

# Obtener y mostrar las 5 mejores opciones
mejores_opciones = mejores_opciones_tipo_cambio(resultados_tc, top_n=5)