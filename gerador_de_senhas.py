'''
Gerador de senhas em Python, este projeto reflete a evolução do meu aprendizado
em busca de me aperfeiçoar cada vez mais na linguagem de programação

'''
import secrets
import sys
import string
import time #importei o time para dar o tempo de espera nos momentos que retornar para o menu

#usaremos para guardar as senhas
senhas = []




def gerar_senhas():
    print("\nVamos gerar a sua senha!")
    while True:
        try:
            tamanho = int(input("\nDeseja que sua senha tenha quantos caracteres? "))
            if tamanho < 8:
                print("\nSua senha deve ter no minimo 8 caracteres\n")
                continue
            elif tamanho > 128:
                print("\nSua senha excede o limite maximo de caracteres!")
                continue
            else:
                break
        except ValueError:
            print("\nDigite um numero para o tamanho da senha!")
            continue

        
    while True:
        maiuscula = input("\nDeseja adicionar letra maiuscula? s/n: ").strip().lower()
        if maiuscula in ("s","sim"):
            maiuscula = True
            break
        elif maiuscula in ("n","não","nao"):
            maiuscula = False
            break
        else:
            print("\nOpção invalida!")
            continue
    while True:
        numeros = input("\nDeseja adicionar numeros? s/n: ").strip().lower()
        if numeros in ("s","sim"):
            numeros = True
            break
        elif numeros in ("n","nao","não"):
            numeros = False
            break
        else:
            print("\nOpção invalida!")
            continue

    while True:
            simbolos = input("\nDeseja adicionar simbolos? s/n: ").strip().lower()
            if simbolos in ("s","sim"):
                simbolos = True
                break
            elif simbolos in ("n","nao","não"):
                simbolos = False
                break
            else:
                print("\nOpção invalida!")
                continue


    todos_os_caracteres = ""

    # minusculas seram obrigatorias, pois se o usuario escolhe não para todas,
    # não tem senha, e esse não é o objetivo agora
    todos_os_caracteres += string.ascii_lowercase
    if numeros:
        todos_os_caracteres += string.digits
    if maiuscula:
        todos_os_caracteres += string.ascii_uppercase
    if simbolos:
        todos_os_caracteres += string.punctuation

    senha_gerada = "".join(secrets.choice(todos_os_caracteres) for _ in range(tamanho))
    senhas.append(senha_gerada)

    print(f"\nAqui está sua nova senha: {senha_gerada}")
    escolha = input("\nDeseja gerar outra senha? s/n: ").strip().lower()
    if escolha in ("sim","s"):
        return gerar_senhas()
    elif escolha in ("n","nao","não"):
        print("\nVoltando para o menu em 5 segundos.......")
        # um tempo para ler a senha , ler a mensagem e voltar para o menu
        time.sleep(5)
        return menu()
    else:
        print("\nVocê digitou uma opção invalida, voltando para o menu em 5 segundos...")
        time.sleep(5)
        return menu()

    
    
def ver_senhas_salvas():
    #usaremos esta lista escolhas na hora de exibir as senhas salvas
    opcoes = []
    if not senhas:
        print("\nVocê não tem senhas salvas!")
        time.sleep(3)
        return menu()
    else:
        print(f"\n Suas senhas salvas({len(senhas)}):")
        #procuramos todas as senhas salvas!
        for numero , senha in enumerate(senhas, start=1):
            print(f"{numero} - {senha}")
            #adicionamos o numero do qual essa senha representa
            opcoes.append(numero)


        while True:
            escolha = input("Deseja alterar excluir alguma senha? s/n: ").strip().lower()
            if escolha in ("s","sim"):
                while True:
                    try:
                        excluir_senha = int(input("\nDigite o numero da senha que deseja excluir: "))

                    except ValueError:
                        print("\nOpção invalida, vamos tentar novamente!")
                        continue


                    if excluir_senha in opcoes:
                        del senhas[excluir_senha - 1]
                        print("\nSenha excluida")

                        while True:
                            print("1 - Ver as senhas salvas")
                            voltar = input("\n2 - Voltar para o menu: ").strip().lower()

                            if voltar in ("1","ver as senhas salvas"):
                                return ver_senhas_salvas()
                            
                            elif voltar in ("2","voltar para o menu"):
                                return menu()
                            
                            else:
                                print("\nOpção invalida!")
                                continue

                    else:
                        print("\nVocê selecionou uma opção invalida!")
                        continue

            elif escolha in ("n","não","nao"):
                print("\nVoltando para o menu...")
                time.sleep(3)
                return menu()
            else: 
                print("\nOpção invalida")
                continue
            
def menu():
    while True:
        print("\n===Gerador de senha===\n\n")
        print("Escolha uma opção:\n")
        print("1 - gerar nova senha")
        print("2 - ver senhas salvas")
        escolha = input("3 - sair: ").strip().lower()
        if escolha in ("1","gerar nova senha"):
            return gerar_senhas()
        elif escolha in ("2","ver senhas salvas"):
            return ver_senhas_salvas()
        elif escolha in ("3","sair"):
            print("\nEncerrando o programa...")
            time.sleep(3)
            sys.exit()


    pass



if __name__ == "__main__":
    menu()