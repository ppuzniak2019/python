"""
PROGRAM DO WYSYŁANIA I ODBIERANIA MAILI
PAWEŁ PUŹNIAK 2019
UNIWERSYTET PEDAGOGICZNY IM. KEN W KRAKOWIE
PROJEKT ZALICZENIOWY JĘZYKI SKRYPTOWE

"""
import smtplib
import sys
import email
import imaplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#FUNKCJA ZAKOŃCZENIA PROGRAMU
def koniecProgramu():
    print("Kliknij enter aby zakończyć działanie programu.")
    koniec = input()
    if koniec == True:
        sys.exit()

#FUNKCJA WYBORU, WYBIERA JEDNĄ Z KILKU FUNKCJI
def wyborFunkcji(programStatus):
    if programStatus == 1:
        print("\n\tDostępne funkcje:\n\t1) Wyślij mail\n\t2) Odbierz mail\n\t3) Konfiguracja\n\t"
              "0) Zakończ program")

        funkcja = int(input())
        if funkcja == 1:
            print("Wybrałeś opcje wysyłki maila, postępuj zgodnie z poleceniami:\n")
            wyslijWiadomosc()
            print("\n\nWybierz co robimy dalej:")
            wyborFunkcji(1)
        elif funkcja == 2:
            print("Wybrałeś opcje odbioru maila, poniżej lista wiadomości na koncie: " + login + "\n")
            odbierzMail()
            print("\n\nWybierz co robimy dalej:")
            wyborFunkcji(1)
        elif funkcja == 3:
            print("Wybrałeś opcje zmiany konfigarcji, uzupełnij wymagane dane:\n")
            zmienKonfiguracje()
            print("\n\nWybierz co robimy dalej:")
            wyborFunkcji(1)
        elif funkcja == 0:
            print("Wybrałeś opcję zakończenia programu!")
            koniecProgramu()
        else:
            print("Zły numer, wybierz ponownie bądź kliknij 0 aby wyjść z programu.")
            wyborFunkcji(1)

    else:
        koniecProgramu()

#FUNKCJA WYSYŁKI MAILA
def wyslijWiadomosc():
    nadawca = login
    temat = input("Podaj temat wiadomości: ")
    odbiorca = input("Podaj adres email odbiorcy: ")
    wiadomosc = input("Wpisz krótką treść wiadomości: ")

    msg = MIMEMultipart()
    msg['Subject'] = temat
    msg['From'] = nadawca
    msg['To'] = odbiorca
    TEXT = wiadomosc
    msg.attach(MIMEText(TEXT))
    s = smtplib.SMTP(serwer, port)
    s.ehlo()
    s.login(login, haslo)
    s.sendmail(nadawca, odbiorca, msg.as_string())
    s.quit()

    print("Wiadomość wysłana poprawnie!")

#FUNKCJA ODBIERANIA MAILA
def odbierzMail():
    mail = imaplib.IMAP4_SSL(serwer)
    mail.login(login, haslo)
    mail.select('inbox')

    status, data = mail.search(None, 'ALL')
    mail_ids = []
    for block in data:
        mail_ids += block.split()
    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                print('\tOd: ' + mail_from)
                print('\tTemat: ' + mail_subject)
                print('\tTreść: ' + mail_content + '\n')


#ZMIANA KONFIGURACJI SERWERA I KONTA
def zmienKonfiguracje():
    global login, haslo, serwer, port
    print("Czy chcesz zmienić konfigurację, czy skorzystać z przykładowego konta? (1 - moje konto, 2 - przykładowe)")
    konf = input("Wpisz 1 lub 2: ")
    if konf == str(1):
        login = input("Podaj swój login: ")
        haslo = input("Podaj hasło do konta: ")
        serwer = input("Podaj adres serwera SMTP: ")
        port = input("Podaj port serwera (bez SSL): ")
    elif konf == str(2):
        login = "test@puzniak.pl"
        haslo = "Informatyka1!"
        serwer = "mail.puzniak.pl"
        port = 587
    else:
        print("Zły wybór!")
        koniecProgramu()
    print("Konfiguracja zakończona!")

def main():
    programStatus = 1
    print("Program nie jest skonfigurowany! Wypełnij wymagane dane:\n")
    zmienKonfiguracje()
    print("\nWitaj w programie do wysyłania i odbierania maili!\nAby przejść dalej wybierz odpowiednią opcję:")
    wyborFunkcji(programStatus)

if __name__== "__main__":
    main()


