# coding=utf-8
# RefreshSiteBot for continuously waiting for a appartment

from selenium import webdriver
from twilio.rest import Client
from time import sleep
# Linköping bostad
url = "https://www.studentbostader.se/sv/sok-bostad/lediga-bostader?actionId=&omraden=&egenskaper=SNABB&oboTyper="

# Load up Chrome and pull up the website
browser = webdriver.Chrome()
browser.get(url)
sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]").click()

# <--------------------------------Settings-------------------------------->

# Your Account SID
account_sid = "ACf6fc51ba23fd487225896dc38b49e662"
# Your Auth Token
auth_token  = "e5f1412b7b3ce35e69d6a23eaa8c3ba8"

load_up_time = 2
sleep_time =10
information_class_names = ('ObjektAdress', 'ObjektYta', 'ObjektHyra')


# Let The Website laod Up First
sleep(load_up_time)


# <--------------------------------Functions-------------------------------->

def reset():
    browser.refresh()
    sleep(load_up_time)
    rows = browser.find_elements_by_class_name("objektListaMarknad")[1:]
    return rows

def info(rows):
    ret = {}
    for row in rows:
        address = row.find_element_by_class_name(information_class_names[0]).text
        if (address in already_up):
            continue
        temp = []
        for information in information_class_names[1:]:
            temp.append(row.find_element_by_class_name(information).text)
        ret[address] = temp
    return ret
def send(mes):
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='whatsapp:+14155238886', body='Det finns en Bostad Direkt just nu. {}'.format(mes), to='whatsapp:+46763107889')
    print(message.sid)

print("Begin Loop")
already_up = {}

while True:
    rows = reset()
    new = info(rows)
    if (new):
        for k, v in new.items():
            send(f"{k} {' '.join(v)}")
        already_up = new.copy()
        new = {}
    for _ in range(sleep_time):
        sleep(1)
