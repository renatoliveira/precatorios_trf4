from selenium import webdriver

trf4_url = 'https://www2.trf4.jus.br/trf4/controlador.php?acao=consulta_processual_pesquisa'

# TODO: Substituir o caminho pelo caminho no PATH do sistema.
driver = webdriver.Firefox(executable_path="C:/Users/Renato/Desktop/prec/drivers/geckodriver.exe")
driver.get(trf4_url)

document_number = driver.find_element_by_id('txtValor')
document_number.send_keys('50152649020174049388')

send_button = driver.find_element_by_id('botaoEnviar')
send_button.click()

driver.save_screenshot('ss.png')
# Aqui podemos pegar a posição do captcha, recortar a imagem, e enviar para um serviço
# de "captcha solver" como o Antigate, anti-captcha, etc.

# e depois fechamos o browser ou iniciamos outra consulta, repetindo o processo
driver.close()
