from selenium.webdriver import Chrome,ChromeOptions,Firefox,FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import filecmp


browser = Firefox()
browser.maximize_window()

browser.get("http://gresnik.com/")
browser.save_screenshot("naslovna.png")
naslovna_slika = os.path.abspath("naslovna.png")
postoji = filecmp.cmp(naslovna_slika, "naslovna.png")
assert postoji

naslovi = browser.find_elements(By.TAG_NAME,"h3")
tekst = 'Srbija njavljuje ulazak u "Svemirsku trku"'
# for naslov in naslovi:
#     print(naslov.text)
assert tekst in naslovi[3].text

element = browser.find_element(By.XPATH,'/html/body/section[2]/div/div/div[3]/a')
browser.implicitly_wait(5)
browser.execute_script("arguments[0].click();", element)
time.sleep(3)
browser.save_screenshot("ekipa.png")
browser.back()
time.sleep(1)
ekipa_slika = os.path.abspath("ekipa.png")
postoji = filecmp.cmp(ekipa_slika, "ekipa.png")
assert postoji

linkovi = browser.find_elements(By.TAG_NAME,"a")
tekstovi = None
for link in linkovi:
    if link.text == "Tekstovi":
        tekstovi = link
        break
tekstovi.click()
browser.save_screenshot("tekstovi.png")
tekstovi_slika = os.path.abspath("tekstovi.png")
postoji = filecmp.cmp(tekstovi_slika, "tekstovi.png")
assert postoji

o_blogu = browser.find_element(By.CSS_SELECTOR,"#responsive > div.top-bar-right > ul > li:nth-child(3) > a")
o_blogu.click()
tekst = "Zaključak"
h3 = browser.find_elements(By.TAG_NAME,"h3")
assert tekst in h3[1].text
browser.save_screenshot("blog.png")
blog_slika = os.path.abspath("blog.png")
postoji = filecmp.cmp(blog_slika, "blog.png")
assert postoji

login = browser.find_element(By.XPATH,'//*[@id="responsive"]/div[2]/ul/li[4]/a')
login.click()
#provera - autor
kor_ime = browser.find_element(By.NAME,"user")
kor_ime.send_keys("Autor")
sifra = browser.find_element(By.NAME,"pass")
sifra.send_keys("123")
browser.save_screenshot("login.png")
submit = browser.find_element(By.NAME,"submit")
submit.click()
login_slika = os.path.abspath("login.png")
postoji = filecmp.cmp(login_slika, "login.png")
assert postoji


novi_clanak = browser.find_element(By.LINK_TEXT,'Novi članak')
novi_clanak.click()
browser.save_screenshot("noviclanak.png")
noviclanak_slika = os.path.abspath("noviclanak.png")
postoji = filecmp.cmp(noviclanak_slika, "noviclanak.png")
assert postoji

naslov_area = browser.find_element(By.XPATH,'/html/body/section/div/div/div/div[1]/div/form/fieldset[1]/textarea')
naslov_area.send_keys("TIGAR")
uvod_area = browser.find_element(By.XPATH,'/html/body/section/div/div/div/div[1]/div/form/fieldset[2]/textarea[1]')
uvod_area.send_keys("desi tigre")
text_area = browser.find_element(By.XPATH,'/html/body/section/div/div/div/div[1]/div/form/fieldset[2]/textarea[2]')
text_area.send_keys("Marko Markovic")
obj = browser.find_element(By.NAME,"objavljen")
obj.send_keys("1")

save = browser.find_element(By.NAME,"submit")
save.click()

svi_clanci = browser.find_element(By.XPATH,'//*[@id="responsive"]/div[2]/ul/li[3]/a')
svi_clanci.click()
browser.save_screenshot("sviclanci.png")
sviclanci_slika = os.path.abspath("sviclanci.png")
postoji = filecmp.cmp(sviclanci_slika, "sviclanci.png")
assert postoji

clanci = browser.find_elements(By.TAG_NAME,"h3")
tigar = None
for clanak in clanci:
    if clanak.text == "TIGAR":
        tigar = clanak
        #print("evo ga",tigar.text)
assert tigar in clanci


# delete = browser.find_element(By.XPATH,'/html/body/section/div/div/div/div[1]/div/form/fieldset[4]/input[2]')
# delete.click()

logout = browser.find_element(By.LINK_TEXT, "LogOut")
logout.click()
browser.save_screenshot("logout.png")
logout_slika = os.path.abspath("logout.png")
postoji = filecmp.cmp(logout_slika, "logout.png")
assert postoji

povratak = browser.find_element(By.XPATH,'/html/body/section/div/div/div/div/a')
povratak.click()


login = browser.find_element(By.XPATH,'//*[@id="responsive"]/div[2]/ul/li[4]/a')
login.click()
#provera - gost
kor_ime = browser.find_element(By.NAME,"user")
kor_ime.send_keys("Gost")
sifra = browser.find_element(By.NAME,"pass")
sifra.send_keys("456")
browser.save_screenshot("login2.png")
submit = browser.find_element(By.NAME,"submit")
submit.click()
time.sleep(2)
login2_slika = os.path.abspath("login2.png")
postoji = filecmp.cmp(login2_slika, "login2.png")
assert postoji

logout = browser.find_element(By.LINK_TEXT, "LogOut")
logout.click()
pocetna = browser.find_element(By.LINK_TEXT, 'Početna')
pocetna.click()
login = browser.find_element(By.XPATH,'//*[@id="responsive"]/div[2]/ul/li[4]/a')
login.click()
# #provera - else
kor_ime = browser.find_element(By.NAME,"user")
kor_ime.send_keys("marko")
sifra = browser.find_element(By.NAME,"pass")
sifra.send_keys("markovic")
browser.save_screenshot("login3.png")
submit = browser.find_element(By.NAME,"submit")
submit.click()
login3_slika = os.path.abspath("login3.png")
postoji = filecmp.cmp(login3_slika, "login3.png")
assert postoji
time.sleep(2)
browser.save_screenshot("neuspesno.png")
browser.back()
neuspesno_slika = os.path.abspath("neuspesno.png")
postoji = filecmp.cmp(neuspesno_slika, "neuspesno.png")
assert postoji

pocetna = browser.find_element(By.LINK_TEXT, 'Početna')
pocetna.click()
browser.save_screenshot("naslovnakraj.png")
naslovnakraj_slika = os.path.abspath("naslovnakraj.png")
postoji = filecmp.cmp(naslovnakraj_slika, "naslovnakraj.png")
assert postoji


time.sleep(5)
browser.close()

