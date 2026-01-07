# Jõuluõnnitluste Süsteem

Interaktiivne Pythoni programm jõuluõnnitluste genereerimiseks ja saatmiseks e-posti teel.

##  Kirjeldus

See projekt on loodud õppeeesmärkidel ja demonstreerib Pythoni põhilisi kontseptsioone:
- Moodulite kasutamine
- Funktsioonid ja andmestruktuurid (listid)
- Veakäsitlus (try/except)
- Lõpmatu tsükkel kasutajaliidese jaoks
- E-kirjade saatmine SMTP protokolli abil

Programm võimaldab kasutajal:
- Koguda õnnitluste tekste
- Koguda saajate e-posti aadresse
- Genereerida juhuslikke õnnitlusi
- Saata õnnitlusi e-posti teel

##  Projektikuvaus

```
ChristmasCardGen1.0/
??? joulutervitused.py      # Põhiprogramm (käivita see fail)
??? onnitleja.py             # Moodulfail andmetöötlusega
??? naidisandmed.txt         # Näidisandmed testimiseks
??? ChristmasCardGen1.0.py   # Info fail
??? README.md                # See fail
```

##  Kuidas alustada

### Eeldused

- Python 3.6 või uuem
- Pythoni standardteegid: `smtplib`, `email`, `random`

### Installeerimine

1. Klooni repositoorium:
```bash
git clone https://github.com/karlthecoder105/ChristmasCardGen1.0.git
cd ChristmasCardGen1.0
```

2. Python on juba vajalike teekidega varustatud, täiendavat installimist pole vaja.

### Programmi käivitamine

```bash
python joulutervitused.py
```

##  Kasutamine

### 1. Esmane seadistamine

Programmi käivitamisel küsitakse:
- **Soovide arv** ja nende tekstid (nt "Rahulikke pühi!")
- **Saajate arv** ja nende e-posti aadressid

**Näidisandmed testimiseks:**

Soovid:
- Rahulikke pühi!
- Head uut aastat!
- Säravaid jõule!

Saajad:
- mari@test.ee
- peeter@test.ee
- kalle@test.ee

### 2. Menüü valikud

Pärast andmete sisestamist kuvatakse menüü:

```
1 - Õnnitle kõiki saajaid
2 - Õnnitle ühte konkreetset saajat
3 - Õnnitle mitut saajat (komaga eraldatud)
0 - Välju programmist
```

#### Valik 1: Õnnitle kõiki saajaid
Genereerib juhuslikud õnnitlused kõigile sisestatud saajatele.

#### Valik 2: Õnnitle ühte konkreetset saajat
Küsib konkreetse e-posti aadressi ja genereerib sellele õnnitluse.

#### Valik 3: Õnnitle mitut saajat
Võimaldab sisestada mitu e-posti aadressi komaga eraldatuna (nt `mari@test.ee, peeter@test.ee`).

#### Valik 0: Välju
Lõpetab programmi töö.

### 3. E-kirjade saatmine

Pärast õnnitluste genereerimist küsitakse, kas soovid saata e-kirjad. Selleks tuleb eelnevalt konfigureerida e-posti andmed.

##  E-posti konfiguratsioon

E-kirjade saatmiseks pead muutma `onnitleja.py` failis `saada_kiri()` funktsioonis järgmisi väärtusi:

```python
saatja_email = "sinu.email@gmail.com"  # Sinu e-posti aadress
saatja_parool = "sinu_rakenduse_parool"  # Rakenduse parool
```

### Gmail'i kasutamine

1. Logi sisse oma Gmail kontole
2. Mine [Google Account Security](https://myaccount.google.com/security) lehele
3. Luba 2-sammuline autentimine
4. Genereeri rakenduse parool:
   - Google Account ? Security ? 2-Step Verification ? App passwords
5. Kasuta genereeritud parooli `saatja_parool` väärtusena

**Tähelepanu:** Ära jaga oma parooli teistega ega lisa seda avalikku repositooriumi!

##  Tehnilised detailid

### Moodulfail (onnitleja.py)

- `kogu_soovid()` - Kogub kasutajalt soovide tekstid
- `kogu_saajad()` - Kogub kasutajalt e-posti aadressid (valideerib '@' olemasolu)
- `genereeri_juhuslik_soov(soovide_list)` - Valib juhuslikult soovi listist
- `koosta_onnitlused(valitud_saajad=None)` - Koostab õnnitlused saajatele
- `saada_kiri(saaja, sisu)` - Saadab e-kirja SMTP kaudu

### Põhiprogramm (joulutervitused.py)

- Impordib kõik vajalikud funktsioonid moodulist
- Kogub esmased andmed (soovid ja saajad)
- Käivitab lõpmatu menüütsükli
- Käsitleb kasutaja valikuid
- Haldab veakäsitlust

##  Veakäsitlus

Programm käsitleb järgmisi vigu:

- **ValueError**: Kui kasutaja sisestab arvu asemel teksti
- **SMTPException**: E-kirja saatmise vead (autentimine, ühendus)
- **Tühjade listide kontroll**: Hoiatab, kui soove pole lisatud

##  Õppematerjalid

Projekt põhineb Moodle'i materjali: https://moodle.edu.ee/mod/resource/view.php?id=2568200&redirect=1

### Õpitud teemad:
-  Listid
-  Funktsioonid (def)
-  Moodulid
-  Lõpmatu tsükkel (while True)
-  Veakäsitlus (try/except)
-  SMTP e-kirjade saatmine

##  Panustamine

See on õppeprojekt. Kui soovid panustada:
1. Tee fork repositooriumist
2. Loo uus branch (`git checkout -b feature/UusFunktsioon`)
3. Tee oma muudatused
4. Tee commit (`git commit -m 'Lisa uus funktsioon'`)
5. Push'i branch'i (`git push origin feature/UusFunktsioon`)
6. Ava Pull Request

## Hoiatused

- Ära jaga oma e-posti paroole avalikult
- Kasuta ainult testimiseks mõeldud e-posti aadresse
- Gmail piirab päevas saadetavate e-kirjade arvu (umbes 500)
- Programm on loodud õppeeesmärkidel, mitte tootmiskasutuseks

## Litsents

See projekt on loodud õppeeesmärkidel ja on vabalt kasutatav.

## Autor

Karl-Lauri Puusepp

## Kontakt

Kui sul on küsimusi või ettepanekuid, ava issue või võta ühendust läbi GitHub'i.

---

**Häid pühi!**

