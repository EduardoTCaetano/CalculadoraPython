import os

class Calculadora:
    def __init__(self):
        pass

    def exibir_cabecalho(self):   
        print("""
        ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
        ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
        ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
        ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
        ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
        ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝


            """)

    def operacao_invalida(self):
        print("\n Opção inválida! Por favor, escolha uma opção válida.")        
        input("\n\n Digite algo para continuar") 

    def exibir_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.exibir_cabecalho()
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("9 - Finalizar/Sair \n")

    def obter_opcao_menu(self):
        try:
            opc = int(input("Informe a opção desejada! "))
            if opc in [1, 2, 3, 4]:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                self.realizar_operacao(opc, num1, num2)
            elif opc == 9:
                return 9
            else:
                self.operacao_invalida()
        except ValueError:
            self.operacao_invalida()

    def realizar_operacao(self, opc, num1, num2):
        if opc == 1:
            resultado = num1 + num2
            print("\n Resultado da soma:", resultado)
        elif opc == 2:
            resultado = num1 - num2
            print("\n Resultado da subtração:", resultado)
        elif opc == 3:
            resultado = num1 * num2
            print("\n Resultado da multiplicação:", resultado)
        elif opc == 4:
            if num2 != 0:
                resultado = num1 / num2
                print("\n Resultado da divisão:", resultado)
            else:
                print("Erro: Divisão por zero!")
        input("\n\n Digite algo para continuar")

    def executar_calculadora(self):
        opcao = 0
        while opcao != 9:
            self.exibir_menu()
            opcao = self.obter_opcao_menu()

if __name__ == "__main__":
    calc = Calculadora()
    calc.executar_calculadora()
