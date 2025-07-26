#--------------MADE BOT WHICH REPLIES EMAILS 4 ME!!!!!!!----------------------------------


import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import google.generativeai as genai
import time
import pyperclip



web = uc.Chrome()
web.get("https://mail.google.com/mail/u/0/#sent")

genai.configure(api_key="Your Api Key")
model = genai.GenerativeModel('gemini-2.0-flash')

#SIGN IN PART
usern = web.find_element('xpath', '//*[@id="identifierId"]')
usern.send_keys('your gmail address')
usern.send_keys(Keys.ENTER)

passw= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
passw.send_keys('your gmail password')
passw.send_keys(Keys.ENTER)

#REPLYING PART
actions = ActionChains(web)

time.sleep(4)
actions.send_keys(Keys.ENTER).perform()

time.sleep(2)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

time.sleep(2)
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

time.sleep(2)
actions.key_down(Keys.SHIFT).send_keys('a').key_up(Keys.SHIFT).perform()

og_email = pyperclip.paste()

prompt = f"""
Generate email replying to what the sender wrote here {og_email}. Make it long enuf, and make it's style suits that of what the sender wrote.
Also, end it by saying Sincerly(or whatever way 2 end based on tone of sender), Illuseum
P.S: JUST GIVE ME THE TEXT, NOTHING ELSE!!!!!!!!!!!!!!!!
"""

answer = model.generate_content([prompt], stream=False)
response = answer.text.strip()

time.sleep(1)
actions.send_keys(f'{response}').perform()

time.sleep(1)
actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()

time.sleep(20)