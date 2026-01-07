import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Algseis - tühjad listid
saajad = []
soovid = []


def kogu_soovid():
    """Kogub kasutajalt soovide tekstid ja lisab need listi."""
    try:
        arv = int(input("Kui palju soove soovid sisestada? "))
        print("\nSisesta soovide tekstid:")
        for i in range(arv):
            soov = input(f"Soov {i + 1}: ")
            soovid.append(soov)
        print(f"\n? Lisatud {len(soovid)} soovi!")
    except ValueError:
        raise ValueError("Viga! Palun sisesta number, mitte tekst.")


def kogu_saajad():
    """Kogub kasutajalt saajate e-posti aadressid."""
    try:
        arv = int(input("Kui palju saajaid soovid sisestada? "))
        print("\nSisesta saajate e-posti aadressid:")
        for i in range(arv):
            while True:
                aadress = input(f"Saaja {i + 1}: ")
                if '@' in aadress:
                    saajad.append(aadress)
                    break
                else:
                    print("Hoiatus: E-posti aadress peab sisaldama '@' sümbolit. Proovi uuesti.")
        print(f"\n? Lisatud {len(saajad)} saajat!")
    except ValueError:
        raise ValueError("Viga! Palun sisesta number, mitte tekst.")


def genereeri_juhuslik_soov(soovide_list):
    """Valib juhuslikult ühe soovi listist."""
    if not soovide_list:
        raise ValueError("Soove pole veel lisatud! Palun alusta programm uuesti.")
    return random.choice(soovide_list)


def koosta_onnitlused(valitud_saajad=None):
    """Koostab õnnitlused valitud saajatele.
    
    Args:
        valitud_saajad: List saajate aadressidest või None (kõik saajad)
    
    Returns:
        List õnnitlustega kujul "saaja@mail.ee: Soov"
    """
    if valitud_saajad is None:
        valitud_saajad = saajad
    
    onnitlused = []
    for saaja in valitud_saajad:
        soov = genereeri_juhuslik_soov(soovid)
        onnitlus = f"{saaja}: {soov}"
        onnitlused.append(onnitlus)
    
    return onnitlused


def saada_kiri(saaja, sisu):
    """Saadab e-kirja saajale.
    
    Args:
        saaja: Saaja e-posti aadress
        sisu: Kirja sisu (õnnitluse tekst)
    
    Returns:
        True eduka saatmise korral, False vea korral
    """
    # Konfigureeri saatja andmed
    saatja_email = "sinu.email@gmail.com"  # Asenda oma e-posti aadressiga
    saatja_parool = "sinu_rakenduse_parool"  # Asenda oma rakenduse parooliga
    
    try:
        # Loo e-kiri
        msg = MIMEMultipart()
        msg['From'] = saatja_email
        msg['To'] = saaja
        msg['Subject'] = "Jõuluõnnitlus! ??"
        
        msg.attach(MIMEText(sisu, 'plain', 'utf-8'))
        
        # Ühendu SMTP serveriga ja saada kiri
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(saatja_email, saatja_parool)
            server.send_message(msg)
        
        print(f"? E-kiri edukalt saadetud aadressile {saaja}")
        return True
        
    except smtplib.SMTPException as e:
        print(f"? SMTP viga kirja saatmisel aadressile {saaja}: {e}")
        return False
    except Exception as e:
        print(f"? Viga kirja saatmisel aadressile {saaja}: {e}")
        return False
