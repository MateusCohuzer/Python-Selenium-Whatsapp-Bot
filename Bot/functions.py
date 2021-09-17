from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib
import urllib.request


def messageBuilder(tuner, message):
    retorno = "Error"
    if tuner == "0":
        retorno = str(input(message))
    return retorno


def readList(message):
    lista = []
    c = 0
    while (True):
        escopo = str(input("\n" + message + ": "))
        lista.append(escopo)
        c += 1
        escopo_boll = str(input("Digite 0 se já inseriu todos os contatos desejados: "))
        if escopo_boll == "0":
            break
    return lista


def readZeroOne(message):
    retorno = str
    while (True):
        retorno = str(input(message))
        if retorno in "01":
            break
    return retorno


def webdriverLauncher(driver):
    try:
        urllib.request.urlopen('https://web.whatsapp.com/')
    except urllib.error.URLError:
        print('\033[31mWHATSAPP INDISPONIVEL\033[m')
    else:
        driver.get('https://web.whatsapp.com/')
        time.sleep(10)


def contactFinder(contact, driver):
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
        #Ambos os Xpath's servem para encontrar as caixas de busca e mensagem do whatsapp
        time.sleep(1.5)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contact)
        campo_pesquisa.send_keys(Keys.ENTER)


def stickerFinder(driver):
    campo_emoji = driver.find_element_by_xpath('//div[contains(@class, "_1uqmP _3agz_")]')
    campo_emoji.click()
    time.sleep(0.1)
    campo_sticker = driver.find_element_by_xpath('//button[contains(@class, "_23sAs _3V3JJ _1Eec4 _1owZM")]')
    campo_sticker.click()
    time.sleep(0.1)


def messageSender(message, driver):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    #campo_mensagem[0] == Buscar contatos; campo_mensagem[1] == escrever a mensagem
    campo_mensagem[1].click()
    time.sleep(0.5)
    campo_mensagem[1].send_keys(message)
    campo_mensagem[1].send_keys(Keys.ENTER)


def stickerSender(driver):
    campo_stickers = driver.find_elements_by_xpath('//div[contains(@class, "_2elZc")]')
    campo_stickers[0].click()
    time.sleep(0.2)

