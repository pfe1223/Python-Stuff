talk_rate = 0.13
text_rate = 0.01
data_rate = 10
taxes = 5.32

talk = float(input('Enter number of minutes: '))
text = float(input('Enter number of text messages: '))
data = float(input('Enter amount of data: '))

talk_amount = talk * talk_rate
text_amount = text * text_rate
data_amount = data * data_rate

total = talk_amount + text_amount + data_amount + taxes

print("Your montly cellphone bill is $" + str(total) + ".")