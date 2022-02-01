# coding=utf-8
from selenium import webdriver
from time import sleep
# twilio
from twilio.rest import Client

url = "https://www.studentbostader.se/sv/sok-bostad/lediga-bostader?pagination=0&paginationantal=300#"

browser = webdriver.Chrome()
browser.get(url)
sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]").click()
sleep(5)
locate = browser.find_elements_by_class_name("sb-widget")[1]

# ONLY USE THIS ONCE
rows = locate.find_elements_by_xpath("div")[1:]

print(rows[0].text)
print(len(rows))

information_class_names = ('ObjektOmrade', 'ObjektAdress', 'ObjektYta', 'ObjektIkon'
                           , 'ObjektTyp', 'ObjektHyra', 'ObjektPoang', 'ObjektInflyt')

address_to_information = {}
for row in rows:
    temp = []
    temp.append(row.find_element_by_class_name(information_class_names[0]).text)
    for info in information_class_names[2:]:
        temp.append(row.find_element_by_class_name(info).text)
    address_to_information[row.find_element_by_class_name(information_class_names[1]).text] = temp

# Your Account SID from twilio.com/console
account_sid = "ACf6fc51ba23fd487225896dc38b49e662"
# Your Auth Token from twilio.com/console
auth_token = "e5f1412b7b3ce35e69d6a23eaa8c3ba8"

def send(hyra, adress):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886', body='Ny hyra: , Område: ', to='whatsapp:+46763107889'
    )
    print(message.sid)


def new_appartment_information(elem):
    # for information in information_class_names:
    #  print(elem.find_element_by_class_name(information).text)
    # print('\n')
    send(elem.find_element_by_class_name("ObjektHyra").text, elem.find_element_by_class_name("ObjektAdress").text, )


def search(old_row):
    row = locate.find_elements_by_xpath("div")[1:]
    new_row = [r for r in row if (r not in old_row)]
    if (new_row):
        for each_new in new_row:
            new_appartment_information(each_new)
    return row


def reset():
    global locate
    browser.refresh()
    locate = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]")

#loop = 1
#for _ in range(loop)
print("Begin Loop")
loop_counter = 0
while True:
    print(loop_counter, end=" ")
    rows = search(rows)
    for _ in range(100):
        sleep(1)
    loop_counter += 1