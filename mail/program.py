"""
 +-+-+-+-+-+ +-+-+-+-+-+-+-+
 |P|a|w|e|ł| |P|u|ź|n|i|a|k|
 +-+-+-+-+-+ +-+-+-+-+-+-+-+

PROGRAM DO WYSYŁANIA I ODBIERANIA MAILI
UNIWERSYTET PEDAGOGICZNY IM. KEN W KRAKOWIE
PROJEKT ZALICZENIOWY JĘZYKI SKRYPTOWE

"""
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import easyimap


# Aby zainstalować "easyimap":
# 1. Wejdź w ustawienia - Crtl + Alt + S (PyCharm)
# 3. Następnie wybrać Project -> Project Interpreter -> kliknąć '+'
# 4. Wyszukać: easyimap-python i zainstalować

# FUNKCJA ZAKOŃCZENIA PROGRAMU
def koniecProgramu():
    print("Kliknij enter aby zakończyć działanie programu.")
    poczekanie = input()
    sys.exit()


# FUNKCJA PAUZOWANIA PROGRAMU
def pauzaProgramu():
    print("\n---------- (kliknij enter aby kontynuować) ----------")
    poczekanie = input()


# FUNKCJA WYBORU, WYBIERA JEDNĄ Z KILKU FUNKCJI
def wyborFunkcji(programStatus):
    if programStatus == 1:
        print("\n\tDostępne funkcje:\n\t1) Wyślij mail\n\t"
              "2) Odbierz mail\n\t3) Konfiguracja\n\t"
              "0) Zakończ program")

        funkcja = int(input())
        if funkcja == 1:
            print("Wybrałeś opcje wysyłki maila, "
                  "postępuj zgodnie z poleceniami:\n")
            wyslijWiadomosc()
            pauzaProgramu()
            print("\nWybierz co robimy dalej:")
            wyborFunkcji(1)
        elif funkcja == 2:
            print("Wybrałeś opcje odbioru maila, poniżej "
                  "zobaczysz listę wiadomości w skrzynce: " + login + "\n")
            odbierzMail()
            pauzaProgramu()
            print("\nWybierz co robimy dalej:")
            wyborFunkcji(1)
        elif funkcja == 3:
            print("Wybrałeś opcje zmiany konfigarcji, "
                  "uzupełnij wymagane dane:\n")
            zmienKonfiguracje()
            pauzaProgramu()
            print("\nWybierz co robimy dalej:")
            wyborFunkcji(1)
        elif funkcja == 0:
            print("Wybrałeś opcję zakończenia programu!")
            koniecProgramu()
        else:
            print("Zły numer, wybierz ponownie bądź kliknij "
                  "0 aby wyjść z programu.")
            wyborFunkcji(1)

    else:
        koniecProgramu()


# FUNKCJA WYSYŁKI MAILA
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


# FUNKCJA ODBIERANIA MAILA
def odbierzMail():
    ileMaili = input("Podaj ilość maili jaką "
                     "chcesz przeczytać: ")
    skrzynka = "inbox"
    imapper = easyimap.connect(serwer, login, haslo, skrzynka,
                               ssl=False, port=143)
    for mail_id in imapper.listids(limit=int(ileMaili)):
        mail = imapper.mail(mail_id)
        print("----------\nWiadomośc email:\n----------")
        print("Od: " + mail.from_addr)
        print("Do: " + mail.to)
        print("Temat: " + mail.title)
        print("Treść:\n" + mail.body)
    imapper.quit()


# ZMIANA KONFIGURACJI SERWERA I KONTA
def zmienKonfiguracje():
    global login, haslo, serwer, port
    print("Czy chcesz zmienić konfigurację, czy "
          "skorzystać z przykładowego konta?"
          "(1 - moje konto, 2 - przykładowe)")
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
    print("\n--- Program nie jest skonfigurowany! "
          "Wypełnij wymagane dane! ---\n")
    zmienKonfiguracje()
    print("\nWitaj w programie do wysyłania i odbierania maili!\n"
          "Aby przejść dalej wybierz odpowiednią opcję:")
    wyborFunkcji(programStatus)


if __name__ == "__main__":
    main()
