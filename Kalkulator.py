import logging
import sys
logging.basicConfig(level=logging.DEBUG)

def kalkulator():
    x=input("Podaj dzialanie, poslugujac sie odpowiednia cyfra: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie: ")
    y=input("Podaj skladnik 1: ")
    z=input("Podaj skladnik 2: ")
    x=float(x)
    y=float(y)
    sys.argv.append(y)
    z=float(z)
    sys.argv.append(z)
    if x==1:
        r=y+z
        t=str("Dodaje")
        sys.argv.append(t)
        sys.argv.append(r)
    elif x==2:
        r=y-z
        t=str("Odejmuje")
        sys.argv.append(t)
        sys.argv.append(r)
    elif x==3:
        r=y*z
        t=str("Mnoze")
        sys.argv.append(t)
        sys.argv.append(r)
    elif x==4:
        r=y/z
        t=str("Dziele")
        sys.argv.append(t)
        sys.argv.append(r)

kalkulator()       
if __name__=="__main__":
    logging.info("%s %.2f i %.2f"%(sys.argv[3], sys.argv[1], sys.argv[2]))
    print("Wynik to: %.2f"%sys.argv[4])