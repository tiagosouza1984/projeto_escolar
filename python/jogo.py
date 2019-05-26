
import forca
print("estou no jogo")


def menu():
    print('     Menu\n')
    print('Escolha o jogo:\n')
    print('Digite 1 para jogo da forca')
    print('Digite 2 para jogo da velha')
    print('Digite 3 para sair\n')    


flag = False
while not flag:
    close = False
    menu()
    opcao = input('Sua opção: ')
    if opcao == '1':      
        print('Jogo da Forca')
        forca.main()
        flag = False
    elif opcao == '2':
        print('Jogo da Velha')   
        flag = True   
    elif opcao == '3':
        while not close:
            resp = input('Tem certeza que deseja sair?\nDigite "Sim" para sair ou "Não" para continuar: ')
            resp = resp.upper()              
            if resp == 'SIM':
                print('Até a próxima!')
                flag = True
                close = True
            elif resp == 'NÃO':
                close = True
                print('\n')
            else:
                print('Opção não identificada!\n')
    else:
        print('Opção não identificada!\n')


