

# Financial Scraper


This tool is a data scraper designed to collect economic data from a specified source. It extracts details such as the ticker (stock symbol), the associated index (like Badlar), and various financial attributes of each instrument. These attributes include the current price, the percentage change in price, the Internal Rate of Return (IRR), the maturity of the instrument (MD), the volume of transactions, the parity, the theoretical value (VT), the theoretical IRR (TTIR), the IRR until the next adjustment (UPTIR), days until the next amortization (DQ), the amortization percentage (PQ), and the price quality (QP).


Poner aqui lo de la bolsa

The tool aims to be designed for analyzing and presenting market data in real-time or at a regular frequency, which would be useful for investors, financial analysts, and other professionals interested in tracking specific financial instruments. The ability to extract and present these data in a structured and coherent manner would be key to its effectiveness.

P



## Usage

- The current `name_spiders`:

  - `bonos.py`


- In order to run the the scrapper we most to run the current spiders.

  - `scrapy crawl bonos -o bonos.json`
  - `scrapy crawl bonos -o bonos.csv`

