import os
import Crud


class Menu:

    def __init__(self):
        self.opcao = -1

    @staticmethod
    def pegarvo():
        print('Por favor informe o caminho do arquivo ou pasta')
        atal = input()
        print(f'Caminho atual: {os.getcwd()}')
        atal = atal.replace(Crud.Crud().caminho_inicial,"")
        Crud.Crud().inseriatal(atal)

    # def jamegarfile(jameg=atal):
        # print('Informe o nome do Jamego que deseja consultar: ')
        # jameg = input()
        # jameg.open(atal)

    @staticmethod
    def menu():
        return int(input('\nEscolha umas das alternativas abaixo: \n\n' +
                         '1. Cadastrar Jamegão\n'                             +
                         '2. Consultar Jamegões\n'                            +
                         '3. Consultar Atalhos\n'                               +
                         '4. Editar Jamegão\n'                                   +
                         '5. Desativar Jamegão\n'                             +
                         '6. Escolher outro arquivo\n'                       +
                         '0. Sair\n'))

    def executar(self):
        loop = 0
        self.opcao = Menu().menu()
        while self.opcao != 0:
            if not loop == 0:
                self.opcao = Menu().menu()
            loop = loop + 1
            print(self.opcao)
            if self.opcao == 1:
                cadastro_sucedido = False
                while not cadastro_sucedido:
                    print('Informe o nome do novo Jamego: ')
                    jameg = input()
                    if not Crud.Crud().consultarCadastro(jameg):
                        cadastro_sucedido = True
                        Crud.Crud().inserijame(jameg)
                    else:
                        print("Não é possível haver dois arquivos com o mesmo nome. Por favor, escolha outro nome para seu jamego!")
            elif self.opcao == 2:
                Crud.Crud().consutodo()

            elif self.opcao == 3:
                print('Qual atalho deseja abrir?')
                Crud.Crud().consultarAtalhos()
                print('Informe a pasta e Subpasta: ')
                atal = input()
                Crud.Crud().joinfiles(atal)

            elif self.opcao == 4:
                print('Escolha uma Jamegão para editar')
                Crud.Crud().consutodo()
                jameg = input()
                print('Informe o novo nome do Jamegão')
                novjame = input()
                Crud.Crud().atualijame(novjame, jameg)

            elif self.opcao == 5:
                Crud.Crud().consutodo()
                print('Escolha um Jamegão para desativar:')
                jameg = input()
                Crud.Crud().excluirjame(jameg)

            elif self.opcao == 6:
                Crud.Crud().abrirpasta()
                Menu.pegarvo()
                print('Informe o nome do novo Jamego: ')
                jameg = input()
                Crud.Crud().inserijame(jameg)
