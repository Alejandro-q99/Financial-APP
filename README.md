

# Financial Scraper


Decripción



## Data Extractors

______
**ToDefine**: 

- The current `name_spiders`:

  - `bonos.py`
  - Which other datasource we need to consume?


- In order to run the the scrapper we most to run the current spiders.

  - `scrapy crawl bonos -o app/Data/bonos.json`
  - `scrapy crawl bonos -o app/Data/bonos.csv`
______

... Si este poryecto es en tiempo real precisaremos una arquieterua basada en streaming que consuma en tiempo real y no or lotes. 
... Pregutnar temproalidad.




## Streamlit UI


Para levantar un proyecto de streamlit simplemente nos paramos en la carpeta raiz y podemos correr el programa así: `streamlit run .\app\main.py` .