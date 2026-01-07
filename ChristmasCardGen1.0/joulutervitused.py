from onnitleja import (
    kogu_soovid,
    kogu_saajad,
    koosta_onnitlused,
    saada_kiri
)

def naita_menu():
    """Kuvab kasutajale menüü valikud."""
    print("\n" + "=" * 50)
    print("?? JÕULUÕNNITLUSTE SÜSTEEM ??")
    print("=" * 50)
    print("1 - Õnnitle kõiki saajaid")
    print("2 - Õnnitle ühte konkreetset saajat")
    print("3 - Õnnitle mitut saajat (komaga eraldatud)")
    print("0 - Välju programmist")
    print("=" * 50)


def main():
    """Põhiprogramm, mis juhib menüüd."""
    print("=" * 50)
    print("?? Tere tulemast jõuluõnnitluste süsteemi! ??")
    print("=" * 50)
    
    # Esmane andmete kogumine
    try:
        print("\n?? Alustame andmete kogumisega...\n")
        kogu_soovid()
        print()
        kogu_saajad()
    except ValueError as e:
        print(f"\n? Viga andmete kogumisel: {e}")
        print("Programm lõpetab töö.")
        return
    except Exception as e:
        print(f"\n? Ootamatu viga: {e}")
        print("Programm lõpetab töö.")
        return
    
    # Lõpmatu menüütsükkel
    while True:
        try:
            naita_menu()
            valik = input("\nSinu valik: ").strip()
            
            if valik == "1":
                # Õnnitle kõiki saajaid
                print("\n?? Koostan õnnitlused kõigile saajatele...")
                onnitlused = koosta_onnitlused()
                print("\n? Koostatud õnnitlused:")
                print("-" * 50)
                for onnitlus in onnitlused:
                    print(onnitlus)
                print("-" * 50)
                
                # Valikuline: küsi kas saata e-kirjad
                saada = input("\nKas soovid saata e-kirjad? (jah/ei): ").strip().lower()
                if saada == "jah":
                    for onnitlus in onnitlused:
                        saaja, sisu = onnitlus.split(": ", 1)
                        saada_kiri(saaja, sisu)
            
            elif valik == "2":
                # Õnnitle ühte konkreetset saajat
                aadress = input("\nSisesta saaja e-posti aadress: ").strip()
                print(f"\n?? Koostan õnnitluse aadressile {aadress}...")
                onnitlused = koosta_onnitlused([aadress])
                print("\n? Koostatud õnnitlus:")
                print("-" * 50)
                for onnitlus in onnitlused:
                    print(onnitlus)
                print("-" * 50)
                
                # Valikuline: küsi kas saata e-kiri
                saada = input("\nKas soovid saata e-kirja? (jah/ei): ").strip().lower()
                if saada == "jah":
                    saaja, sisu = onnitlused[0].split(": ", 1)
                    saada_kiri(saaja, sisu)
            
            elif valik == "3":
                # Õnnitle mitut saajat
                aadressid_str = input("\nSisesta saajate aadressid (komaga eraldatud): ").strip()
                aadressid_list = [a.strip() for a in aadressid_str.split(',')]
                print(f"\n?? Koostan õnnitlused {len(aadressid_list)} saajale...")
                onnitlused = koosta_onnitlused(aadressid_list)
                print("\n? Koostatud õnnitlused:")
                print("-" * 50)
                for onnitlus in onnitlused:
                    print(onnitlus)
                print("-" * 50)
                
                # Valikuline: küsi kas saata e-kirjad
                saada = input("\nKas soovid saata e-kirjad? (jah/ei): ").strip().lower()
                if saada == "jah":
                    for onnitlus in onnitlused:
                        saaja, sisu = onnitlus.split(": ", 1)
                        saada_kiri(saaja, sisu)
            
            elif valik == "0":
                # Välju programmist
                print("\n?? Aitäh kasutamast! Head jõule! ??")
                break
            
            else:
                print("\n? Vale valik! Palun vali 0-3.")
        
        except ValueError as e:
            if "Soove pole veel lisatud" in str(e):
                print(f"\n? Viga: {e}")
            else:
                print(f"\n? Sisendi viga: {e}")
        except Exception as e:
            print(f"\n? Ootamatu viga menüü käsitlemisel: {e}")
            print("Palun proovi uuesti.")


if __name__ == "__main__":
    main()
