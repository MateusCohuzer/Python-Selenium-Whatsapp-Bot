import functions
from time import perf_counter

print('='*60)
print(' '*20, 'WHATSAPP BOT 2')
print('='*60)
print('\n ~> By: Mateus "CohuzEr"')

# Input
tuner = functions.readZeroOne("\nDigite para:\n0-Mensagem de Texto\n1-Figurinha\n>> ") # 1-Send the sticker in first place in the recently sent ones
message = functions.messageBuilder(tuner, "\nInsira a mensagem desejada: ")
contacts = functions.readList("Insira o nome exato do contato ou grupo desejado")
message_amount = int(input("\nInsira quantas mensagens serão enviadas: "))

#Processing
driver = functions.webdriver.Chrome(functions.ChromeDriverManager().install())
functions.webdriverLauncher(driver)

if tuner == "0":
    for contact in contacts:
        functions.contactFinder(contact, driver)
        start = perf_counter()
        for i in range(message_amount):
            functions.messageSender(message, driver)
        finish = perf_counter()
        functions.contactFinder(contact, driver)
        print(f"Foram enviadas {message_amount} mensagens em {round((finish - start), 2)} segundos", driver)#time test
else:
    for contact in contacts:
        functions.contactFinder(contact, driver)
        functions.stickerFinder(driver)
        for i in range(message_amount):
            functions.stickerSender(driver)
