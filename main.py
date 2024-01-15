# Lai ieietu ortusā
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# Fails ar lietotajvārdu un paroli gan ortusam, gan gmail
from settings import *
# Lai nosūtītu e-pastu
import smtplib
# Lai sagatavotu e-pastu nosūtīšanai
import email
from email.message import EmailMessage
# Lai apskatītu e-pastus
import imaplib
#Lai varētu viegli nomainit laiku zonu
import pytz
# Lai uzstādītu laiku
import time
from datetime import datetime

if ortus_username == "" or ortus_password == "" or gmail_password == "" or gmail_username == "":
    print("Nav pabeigta uzstādīšana! Lūdzu pabeigt uzstādīšanu settings.py failā.")
    quit()


chrome_options = Options()
chrome_options.add_argument("--headless")

imap_url = "imap.gmail.com"
smtp_server = "smtp.gmail.com"
gmail_port = 587
now = str(time.strftime("%d-%b-%Y"))
GMTTime = datetime.now(pytz.timezone('GMT'))
nowTime = str(GMTTime.strftime("%H:%M"))
z = 0

while True:
    print("Started")
    my_mail = imaplib.IMAP4_SSL(imap_url)
    my_mail.login(gmail_username, gmail_password)

    my_mail.select("INBOX")
    key = 'FROM'
    value = test_email
    aaa, data = my_mail.search(None, 'OR', '(' + key, value, 'SINCE', now + ')', '(' + key, "noreply-estudijas@rtu.lv",'SINCE', now + ')')
    list = data[0].split()
    # print(list)
    for i in list:
        aaa, data = my_mail.fetch(i, '(RFC822)')
        mail = data[0][1]
        msg = email.message_from_bytes(mail)
        str_msg = str(msg)
        # print(msg.get('Date')[17:22])
        # print(nowTime.replace("-",":"))
        try:
            if msg.get('Date')[17:22] >= nowTime.replace("-",":"):
                str_msg = str_msg[str_msg.find("uzdevuma iesniegumam<"):]
                str_msg = str_msg[str_msg.find("estudijas"):]
                str_msg = str_msg[:str_msg.find(">.")]
                link = "https://" + str_msg.replace("3D", "")
                # print(link)
                if link != "https://":
                    if z == 0:
                        driver = webdriver.Chrome(options=chrome_options)
                        driver.get("https://estudijas.rtu.lv/")
                        time.sleep(1.5)
                        driver.find_element(By.ID, "submit").click()
                        time.sleep(1.5)
                        driver.find_element(By.ID, "IDToken1").send_keys(ortus_username)
                        driver.find_element(By.ID, "IDToken2").send_keys(ortus_password)
                        driver.find_element(By.NAME, "Login.Submit").click()
                        time.sleep(2)
                        # Start connection
                        my_server = smtplib.SMTP(smtp_server, gmail_port)
                        my_server.ehlo()
                        my_server.starttls()

                        # Login with email and password
                        my_server.login(gmail_username, gmail_password)
                        z=1

                    driver.get(link)
                    time.sleep(2)

                    page = driver.find_element(By.ID, "region-main")
                    prieksmetaNosaukums = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/section/h2").get_attribute("innerHTML")
                    prieksmetaNosaukums = prieksmetaNosaukums[:prieksmetaNosaukums.find("<small>")]
                    text = page.text
                    text = text[text.find("Vērtējums"):]
                    atbilde = text[:text.find("\n")]
                    print(atbilde)


                    msg = EmailMessage()
                    msg.set_content(atbilde)

                    msg['Subject'] = "Jauna atzīme " + prieksmetaNosaukums.lower()
                    msg['From'] = gmail_username
                    msg['To'] = gmail_username

                    my_server.send_message(msg)
                    print("Email sent")
        except:
            pass

    if z==1:
        my_server.quit()
        driver.close()
        my_mail.close()
        my_mail.logout()
        z = 0
    now = str(time.strftime("%d-%b-%Y"))
    GMTTime = datetime.now(pytz.timezone('GMT'))
    nowTime = str(GMTTime.strftime("%H:%M"))
    print("ENDED")
    time.sleep(60*minutes)
