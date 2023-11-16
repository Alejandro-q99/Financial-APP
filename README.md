

# Financial Scraper


This tool is a data scraper designed to collect economic data from a specified source. It extracts details such as the ticker (stock symbol), the associated index (like Badlar), and various financial attributes of each instrument. These attributes include the current price, the percentage change in price, the Internal Rate of Return (IRR), the maturity of the instrument (MD), the volume of transactions, the parity, the theoretical value (VT), the theoretical IRR (TTIR), the IRR until the next adjustment (UPTIR), days until the next amortization (DQ), the amortization percentage (PQ), and the price quality (QP).


Poner aqui lo de la bolsa

The tool aims to be designed for analyzing and presenting market data in real-time or at a regular frequency, which would be useful for investors, financial analysts, and other professionals interested in tracking specific financial instruments. The ability to extract and present these data in a structured and coherent manner would be key to its effectiveness.

P



## Usage

- The current `name_spiders`:

  - `bonos.py`


- In order to run the the scrapper we most to run the current spiders.

  - `scrapy crawl bonos -o app/Data/bonos.json`
  - `scrapy crawl bonos -o app/Data/bonos.csv`

-------------------
## ANALISIS REQUISITOS


ANÁLISIS REQUISITOS


Introducción:
“””
El mercado argentino es muy chico y tiene muchísimas oportunidades. Para esclarecer lo descripto abajo se realizará una breve introducción. Los bonos argentinos tienen 3 cotizaciones diferentes:
 En pesos EJ: GD30
 En dólares: EJ GD30D
 En dólares cable (son dólares liquidados en EEUU) EJ: GD30C
 Además, los bonos se pueden comprar “poniendo” el dinero en 3 momentos:
 Contado inmediato (es el mismo día)
 24 hs hábiles
 48 hs hábiles
 
Que se conecte vía API con MAV (mercado abierto de valores) o BYMADATA, que tengo entendido de que se puede, para extraer datos en tiempo real de CEDEARS, BONOS y LETRAS. Por otro lado, en caso de avanzar, conseguiría la base de datos de todas las operaciones pasadas. (pero en un primer momento no se va a necesitar para nada)
“”” 

 




________




 
Alance del Bot 1:
“Detención oportunidades de Tipo de cambio implícito”

 1. Saber calcular el precio en tiempo real de los tipos de cambio implícito.
EJ:
-        Ver cotización de GD30 y hacer la división de GD30D.
o   A la fecha cotiza 25.500 / 30,75 = TC 829.
-        Esto mismo realizarlo con todos los instrumentos de mercado (más de 400) y calcular su cotización en Plazo Contado Inmediato, 24 horas y 48hs. (1200 cálculos a la vez ya que es 400*3 aprox)

1.  Calcular los diferentes tipos de cambio implícito con sus diferentes combinaciones.
EJ:
-        Comprar GD30 en CI y venderlo contra GD30D en 48 hs. Eso realizarlo implica realizar muchísimos cálculos más. (ya no es calcular[R3]  el bono con el mismo plazo de liquidación)
 
1.      Mostrar las 5 mejores opciones de Tipo de Cambio implícito 



ANALISIS:

- Digamos que tienes datos en tiempo real de CEDEARS, BONOS y LETRAS. Por otro lado, en caso de avanzar, conseguiría la base de datos de todas las operaciones pasadas. (pero en un primer momento no se va a necesitar para nada) que proviene de un scraper.

- Si tenemos una necesidad de consumo de datos en tiempo de real, también debemos considerar los históricos y el almacenamiento que vamos a tener.

- Solución Dashboard.
Qué significa ser el Top 5? Cuales son los requisitos para ser top 5
________





Alance del Bot 2: Detección de oportunidades arbitrajes en dólares (MEP y Cable)

1.     Detectar en momento real disparidades muy grandes de los precios de los bonos de la misma moneda en tiempo real.

2.-     Extracción del mercado de valor de un bono comparándolo contra el mismo bono comparando el valor del bono en MEP o Cable. MEP es dólares local y Cable es dólar en EEUU.

EJ: A la fecha el Bono GD30D cotiza 30,75 dólares en Contado Inmediato. Uno puede comprar ese Bono en el momento y actualmente la venta contra cable está cotizando 34 dólares. Eso representa una brecha del 10,56% en dólares.


3. Detectar en momento real disparidades muy grandes de los precios de los bonos de la misma moneda en tiempo real CON DIFERENTES PLAZOS DE LIQUIDACIÓN. Extracción del mercado de valor de un bono comparándolo contra el mismo bono comparando el valor del bono en CI, 24 hs y 48hs. Tanto para los bonos en MEP y en CABLE (EJ: GD30, GD30D y GD30C)

EJ: Bono GD30D en CI cotiza 30,75 mientras que en 48hs cotiza 30,8. Esto representa una brecha del 0,1%. Si bien no es mucha la brecha use el mismo ejemplo que antes para seguir la línea, pero entre los 400 activos que hay las brechas suelen llegar al 10% en dólares como el caso mencionado en el punto A.





________




Alcance del Bot 3: Detección oportunidades de Inversiones






1. Realice el calculo del rendimiento de todos los bonos en tiempo real. Para eso tiene que extraer el precio de los bonos, tanto en pesos como en dólares y sus diferentes plazos de liquidación. Ese precio que extrae lo debería insertar en una calculadora (un Excel), armar el flujo de fondos y mostrárselo al cliente/trader.

2. Mostrar las 5 mejores opciones /mayor rendimiento








Alcance del Bot 4:
Que opere directamente contra mercado, que estos arbitrajes no los recomiende, sino que los opere directamente el BOT


Alcance 5: Predicción de comportamiento de carteras de inversión
Alcance 6: Predicción del Tipo de Cambio


 
 


________


## Modelos


- https://huggingface.co/FinGPT/fingpt-mt_llama2-7b_lora
- https://huggingface.co/spaces/FinGPT/FinGPT-Forecaster


Notebook for Fine Tunning

https://github.com/AI4Finance-Foundation/FinGPT/blob/master/fingpt/FinGPT_v3/training_8bit/train_Llama2_13B.ipynb




________


## DATA SOURCES


- La fuente de fatos de bolsistas parace incompleta en la sección de Bonos.
- Revisar si es CEDARS o CER, son dos cosas diferentes

Esta fuente de datos tiene los tickets mas actualizados.

https://open.bymadata.com.ar/#/dashboard


________
