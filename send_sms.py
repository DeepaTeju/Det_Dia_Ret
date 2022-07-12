from twilio.rest import Client
#--------------------------------------------------------
# change values of account_sid, auth_token, to and from - all from twilio account
#-------------------------------------------------------
def send(value, classes):
    #Your Account SID from twilio.com/console
    account_sid = "AC78e6f905ba8c648fdf343e4a38f4ffc5"
    #Your Auth Token from twilio.com/console
    auth_token  = "919cc7065a505dad343e8064828d17c4"

    client = Client("AC9c868899f0f00d91080afc0b7c4", "22543adb52ea46fb64f8a939a75da0")
    message = client.messages.create(
    to="+918861123978",
    from_="+917899911604",
    body=f"Blindness detection system report! severity level is : {value} and class is {classes}")
    #
    print('Message sent Succesfully !')
    print(message.sid)