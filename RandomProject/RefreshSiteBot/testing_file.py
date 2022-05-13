from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "ACf6fc51ba23fd487225896dc38b49e662"
# Your Auth Token from twilio.com/console
auth_token = "e5f1412b7b3ce35e69d6a23eaa8c3ba8"

def send():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="Funkar",
        to='whatsapp:+46763107889'
    )

    print(message.sid)

send()
