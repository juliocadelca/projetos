from time import sleep
import pyautogui as pg

# Abrir Chrome
pg.PAUSE = 1
pg.press('win')
pg.write('Chrome')
sleep(1)
pg.press('enter')
# Digitar www.instagram.com e dar enter
pg.write('www.instagram.com')
sleep(1)
pg.press('enter')
sleep(3)
# Clicar em pesquisar e buscar por insta desejado
pg.click(84,271, duration=2)
pg.click(196,198, duration=2)
pg.write('uberlandia_noticias')
sleep(5)
pg.click(213,262, duration=1)
# Clicar no instal e clicar em seguidores
# Começar a seguir todo mundo de tempo em tempo