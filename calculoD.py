
#Fuções------------------------------------------------------------------------
def calculate_distance(A, RSSI, n): #implemeta a formula para calcular n
    return 10 ** ((A - RSSI) / (10 * n))

def show_result(d): #mostra a distancia na tela
    print(f"Distancia = {d:.2f} metros")


def show_menu(): #um texto de menu para dar um charme
    print("-"*40,"\n")
    print("-Calculadora de distancia-\n\n")
    print("isira os dados\n")
    print("-"*40,"\n\n")

#---------------------------------------------------------------------------

show_menu()
isWork = True
while isWork == True: #loop de funcionamento, só para quando o usuario deseja
    try: 
        #captura os dados do usuario
        A = float(input("Digite o A: "))
        RSSI = float(input("Digite o RSSI: "))
        n = float(input("Digite o n: "))

        #calcula e mostra a distancia
        d = calculate_distance(A, RSSI, n)
        show_result(d)
        #verifica se o usurio quer manter o loop ou não
        status = input("Deseja inserir mais valores? (Y/N): ")
        if(status == "N" or status == "n"):
            print("\nAte a proxima!\n")
            isWork = False 
    except ValueError: #Tratamento de erros
        print("Valor não aceito!\n\n") # no caso aqui todo erro só mostra a mensagem


        