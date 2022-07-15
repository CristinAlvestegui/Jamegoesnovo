import Dao
import os
import Menu


class Crud:

    def __init__(self):
        self.caminho_inicial = r'C:\Users\calve\Documents'
        self.db_connect = Dao.connection()
        self.con = self.db_connect.cursor()

    def inserijame(self, nome):
        try:
            sql = "insert into Jamegoes(jameg) values('{}')".format(nome)
            self.con.execute(sql)
            self.db_connect.commit()
            print("{} Inserido".format(self.con.rowcount))
        except Exception as erro:
            print(erro)

    def consultarCadastro(self, nome):
        try:
            sql = "SELECT * FROM jamegoes"
            self.con.execute(sql)
            for cod, jameg in self.con:
                if jameg == nome:
                    self.con.close()
                    return True
                else:
                    return False
        except Exception as error:
            print(error)
        finally:
            self.con.close()

    def inseriatal(self, nome):
        try:
            sql = "insert into Atalho(atal) values('{}')".format(nome)
            self.con.execute(sql)
            self.db_connect.commit()
            print("{} Inserido".format(self.con.rowcount))
        except Exception as erro:
            print(erro)

    def consultarAtalhos(self):
        try:
            sql = "SELECT * FROM atalho"
            self.con.execute(sql)
            for (atal) in self.con:
                print("Atalhos: {}".format(atal))
        except Exception as erro:
            print(erro)

    def consutodo(self):
        try:
            sql = 'select * from Jamegoes'
            self.con.execute(sql)
            for(cod, jameg) in self.con:
                print("Jameg: {}".format(jameg))
        except Exception as erro:
            print(erro)

    def consujame(self, nome):
        try:
            sql = "select * from Jamegoes where jameg = '{}'".format(nome)
            self.con.execute(sql)
            for(jameg) in self.con:
                print("jameg: {}".format(jameg))
        except Exception as erro:
            print(erro)

    def consuatal(self, nome):
        try:
            sql = "select * from Atalho where atal = '{}'".format(nome)
            self.execute(sql)
            for(atal) in self.con:
                print("jameg: {}".format(atal))
        except Exception as erro:
            print(erro)

    def atualijame(self, nome, novo_nome):
        try:
            sql = "update Jamegoes set jameg = '{}' where jameg = '{}'".format(nome, novo_nome)
            self.con.execute(sql)
            self.db_connect.commit()
            print('{} Atualizado!'.format(self.con.rowcount))
        except Exception as erro:
            print(erro)

    def excluirjame(self, nome):
        try:
            sql = "delete from Jamegoes where jameg = '{}'".format(nome)
            self.con.execute(sql)
            self.db_connect.commit()
            print('{} Excluido!'.format(self.con.rowcount))
        except Exception as erro:
            print(erro)

    def abrirpasta(self):
        arvo = self.caminho_inicial
        print('\nBem-vindo ao seu diretorio!\n')
        for arvo, dirs, files in os.walk(arvo):
            if not dirs:
                print('A pasta: ', arvo, 'não possui subpastas')
            else:
                print('A pasta: ', arvo, 'possui as subpastas:')
                for sub in dirs:
                    print('\t\t', sub)
            if not files:
                print('\t não possui arquivos')
                print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
            else:
                print('\t e os arquivos: ')
                for file in files:
                    print('\t\t', file)

    @staticmethod
    def pegarvo():
        print('Por favor informe a subpasta e o nome do arquivo:')
        atal = input()
        Crud().inseriatal(atal)
        Menu.Menu().executar()

    @staticmethod
    def joinfiles(self, atal):
        cami = os.path.join(self.caminho_inicial, atal)
        os.system(cami)