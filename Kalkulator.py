import logging
logging.basicConfig(level=logging.DEBUG)

def kalkulator():
    operation=input("Podaj dzialanie, poslugujac sie odpowiednia cyfra: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie: ")
    argument_1=input("Podaj skladnik 1: ")
    argument_2=input("Podaj skladnik 2: ")
    operation=float(operation)
    argument_1=float(argument_1)
    argument_2=float(argument_2)
    if operation==1:
        result=argument_1+argument_2
        logging.info(f'Dodaje {argument_1} i {argument_2}')
        print("Wynik dodawania: ", result)
    elif operation==2:
        result=argument_1-argument_2
        logging.info(f'Odejmuje {argument_2} od {argument_1}')
        print("Wynik odejmowania: ", result)
    elif operation==3:
        result=argument_1*argument_2
        logging.info(f'Mnoze {argument_1} i {argument_2}')
        print("Wynik mnozenia: ", result)
    elif operation==4:
        result=argument_1/argument_2
        logging.info(f'Dziele {argument_1} przez {argument_2}')
        print("Wynik dzielenia: ", result)
kalkulator()