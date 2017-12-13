# precatorios_trf4
Conjunto de scripts básicos para raspagem de dados do Tribunal Regional Federal da 4a região

# Motivação

Este projeto de final de semana foi utilizado como exercício para uma empresa de webscrapping. O objetivo era, dada uma lista de precatórios (em PDF), a leitura e armazenamento das informações dos mesmos.

## Como utilizar

Existem três scripts neste repositório, que realizam três etapas distintas:

1. main.py (leitura do dump do PDF que foi gerado com a biblioteca pdfminer)
2. scraper.py (o arquivo que é utilizado pelo Selenium para controlar o navegador - o Firefox, no caso - que acessará o site do tribunal e procurará pelo precatório especificado)
3. document_parser.py (script que lê o HTML que é salvo pelo `scraper.py`)

## Captcha

O segundo script (`scraper.py`) utiliza o webdriver porque o site do TRF4 não possui uma API pública acessível, ou se possui, não era conhecida. Há uma limitação nesta abordagem que é a de resolução de um Captcha na página de pesquisa do precatório. Para contornar essa limitação é possível que o webdriver salve uma imagem do captcha e use um serviço externo de resolução de captchas para obter o resultado correto.

O terceiro script (`document_parser.py`) leva em consideração que o captcha foi acertado, e a próxima página já é a do precatório pesquisado. Seria necessário então salvar o HTML da página do precatório e fazer este script ler o arquivo `.html`. O retorno desse script poderia ser facilmente alterado para um JSON.
