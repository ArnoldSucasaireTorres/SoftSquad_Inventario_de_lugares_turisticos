from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class Hosttest(LiveServerTestCase):

    def testhomepage(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/brave-browser"
        chrome_driver_binary = "/home/msac/Escritorio/entorno/SoftSquad_Inventario_de_lugares_turisticos/InventarioLugaresTuristicos/chromedriver"
        driver= webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        
        driver.get('http://127.0.0.1:8000/')
        
        time.sleep(5)

        #Seleccionando el label a la pagina de destinos
        destinos_a = driver.find_element_by_link_text('Destinos')
        destinos_a.send_keys(Keys.RETURN)
        
        time.sleep(3)

        #Seleccionando el filtro
        filter_input = driver.find_element_by_id("filter_input")
        filter_input.send_keys(Keys.ARROW_DOWN)

        time.sleep(1)
        
        #Escribiendo una entrada de test
        value_input = driver.find_element_by_id('value_input')
        value_input.send_keys('volcan')

        time.sleep(3)

        #Regresando al inicio
        DesTur_a = driver.find_element_by_link_text("DesTur")
        DesTur_a.send_keys(Keys.RETURN)




