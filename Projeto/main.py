import pymongo
myclient = pymongo.MongoClient("mongodb+srv://Atlas:grupo2@cluster0.bwsik.mongodb.net/Plataforma_departamental?retryWrites=true&w=majority")

def menuU():
    opcao=0
    while opcao != 6:

        print('''     [1]Listar todos os dados
        [2] Inserir dados
        [3] Editar dados
        [4] Eliminar dados
        [5] Filtrar
        [6] Voltar a tras
        ''')
        opcao= int(input("Qual a opção que deseja realizar"))
        if opcao == 1:
            print('Todos os dados')
            for x in myclient.Plataforma_departamental.Utilizador.find():
                print(x)
        elif opcao == 2:
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Utilizador"]
            passw= int(input("Qual a password que deseja adicionar"))
            tip= input("Qual o tipo de utilizador que deseja adicionar")
            emaill = input("Qual o email que deseja adicionar")
            mydict = { "password": passw, "tipo": tip, "email": emaill }
            x = mycol.insert_one(mydict)
            print("Adicionado com sucesso")
        elif opcao == 3 :
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Utilizador"]
            passw= int(input("Qual a password que deseja alterar"))
            myquery = { "password": passw }
            npassw= int(input("Qual a nova palavra pass que deseja inserir"))
            newvalues = { "$set": { "password": npassw } }
            mycol.update_one(myquery, newvalues)
            print("Alterado com sucesso")
        elif opcao == 4:
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Utilizador"]
            remover = input("insira o email do utilizador que deseja remover")
            myquery = { "email": remover }
            mycol.delete_one(myquery)
            print("Removido com sucesso")
        elif opcao == 5:
            print('Procura documentos com condições AND e OR')
            for x in myclient.Plataforma_departamental.Utilizador.find({"$or":[{"id": {"$gt": 5}}, {"$and":[{"id": {"$gt": 10}}]}]}):
                print(x)
        elif opcao == 6:
            main()
        else:
            print("insira uma opção valida")

def menuDir():
    opcao=0
    while opcao != 6:

        print('''     [1]Listar todos os dados
        [2] Inserir dados
        [3] Editar dados
        [4] Eliminar dados
        [5] Filtrar
        [6] Voltar atras 
        ''')
        opcao= int(input("Qual a opção que deseja realizar"))
        if opcao == 1:
            print('Todos os dados')
            for x in myclient.Plataforma_departamental.Diretor.find():
                print(x)
        elif opcao == 2:
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Diretor"]
            id_escola= int(input("Qual o id_escola que deseja adicionar"))
            id_docente = int(input("Qual o id_docente que deseja adicionar"))
            data_inicio= input("Qual a data_inicio que deseja adicionar")
            mydict = { "id_escola": id_escola, "id_docente": id_docente, "data_inicio": data_inicio }
            x = mycol.insert_one(mydict)
            print("Adicionado com sucesso")
        elif opcao == 3 :
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Diretor"]
            id_docente= int(input("Qual o id_docente que deseja alterar"))
            myquery = { "id_docente": id_docente }
            nid_docente= int(input("Qual o id_docente que deseja inserir"))
            newvalues = { "$set": { "id_docente": nid_docente } }
            mycol.update_one(myquery, newvalues)
            print("Alterado com sucesso")
        elif opcao == 4:
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Diretor"]
            remover = input("insira o id_docente que deseja remover")
            myquery = { "id_docente": remover }
            mycol.delete_one(myquery)
            print("Removido com sucesso")
        elif opção == 5:
            print('Procura documentos com condições AND e OR')
            for x in myclient.Plataforma_departamental.Diretor.find({"$or":[{"id_escola": {"$gt": 1}}, {"$and":[{"id_escola": {"$gt": 3}}]}]}):
                print(x)
        elif opcao == 6:
            main()
        else:
            print("insira uma opção valida")

def menuEsc():
    opcao = 0
    while opcao != 6:

        print(
            '''______________________________________________________________________________________________________''')
        print('''        [0] listar
                [1] Criar
                [2] Editar
                [3] Apagar
                [4] Filtrar
                [5] Voltar Atrás''')
        opcao = int(input('Qual é a sua opção? '))
        if opcao == 0:
            print("Todos dados")
        for x in myclient.Plataforma_departamental.Escola.find():
            print(x)
        if opcao == 1:
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Escola"]
            nom = str(input("Qual o nome que deseja adicionar"))
            sig = input("Qual a sigla que deseja adicionar")
            idd = input("Qual o id da instituição que deseja adicionar")
            mydict = {"nome": nom, "sigla": sig, "id_instituição": idd}
            x = mycol.insert_one(mydict)
        if opcao == 2:
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Escola"]
            nom = str(input("Qual o nome que deseja alterar"))
            myquery = {"nome": nom}
            nom = str(input("Qual o novo nome que deseja inserir"))
            newvalues = {"$set": {"nome": nom}}
            mycol.update_one(myquery, newvalues)
            print("Alterado com sucesso")
        if opcao == 3:
            mydb = myclient["Plataforma_departamental"]
            remover = input("insira o nome da escola que deseja remover")
            myquery = {"nome": remover}
            mycol.delete_one(myquery)
            print("foi eliminado")
        if opcao == 4:
            print('Procura documentos com condições AND e OR')
            for x in myclient.Plataforma_departamental.Escola.find(
                    {"$or": [{"id": {"$gt": 5}}, {"$and": [{"id_instituição": {"$gt": 0}}]}]}):
                print(x)
        if opcao == 5:
            main()
        else:
            print('Opção inválida!')
            print('=-=' * 10)
        print('O programa acabou !')

def menuProj():
    opcao = 0
    while opcao != 6:

        print('''______________________________________________________________________________________________________''')
        print('''        [0] listar
            [1] Criar
            [2] Editar
            [3] Apagar
            [4] Filtrar
            [5] Voltar Atrás''')
        opcao = int(input('Qual é a sua opção? '))
        if opcao == 0:
            print("Todos dados")
        for x in myclient.Plataforma_departamental.Publicacao.find():
            print(x)
        if opcao == 1:
            #inserir dados
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Projeto"]
            titl= input("Qual o titulo que deseja adicionar")
            datainicio= input("Qual a data inicial que deseja adicionar")
            datafim = input("Qual a data final que deseja adicionar")
            localrealização = input("Qual o local de realização que deseja adicionar")
            valorfinaciado= int(input("Qual o valor finaciado que deseja adicionar"))
            mydict = {"Titulo": titl, "data_inicio": datainicio, "data_fim": datafim,"local_realização":localrealização, "valor_finaciado":valorfinaciado }
            x = mycol.insert_one(mydict)

        if opcao == 2:
            #Editar dados
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Projeto"]
            titulo= input("Qual o titulo que deseja alterar")
            myquery = { "titulo": titulo }
            ntitulo= input("Qual o novo titulo que deseja inserir")
            newvalues = { "$set": { "titulo": ntitulo } }
            mycol.update_one(myquery, newvalues)
            print("Alterado com sucesso")

        if opcao == 3:
            #Eliminar dados
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Projeto"]
            remover = input("insira o titulo do projeto que deseja remover:")
            myquery = {"titulo": remover }
            mycol.delete_one(myquery)
            print("Removido com sucesso")

        if opcao == 4:
            print('Procura documentos com condições AND e OR')
            for x in myclient.Plataforma_departamental.Projeto.find({"$or":[{"id": {"$gt": 37}}, {"$and":[{"id": {"$gt": 40}}]}]}):
             print(x)

        if opcao == 5:
             main()




def menuPub():
    opcao = 0
    while opcao != 6:

        print('''______________________________________________________________________________________________________''')
        print('''        [0] listar
            [1] Criar
            [2] Editar
            [3] Apagar
            [4] Filtrar
            [5] Voltar Atrás''')
        opcao = int(input('Qual é a sua opção? '))
        if opcao == 0:
            print("Todos dados")
        for x in myclient.Plataforma_departamental.Publicacao.find():
            print(x)
        if opcao == 1:

            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Publicacao"]
            id= input("Qual o id da Publicação?")
            titulo= input("Qual o titulo da Publicação?")
            data_finalizacao= input("Quando a Publicação foi finalizada?")
            local_realizacao= input("Onde a Publicação foi finalizada?")
            tipo= input("Qual o tipo da Publicação?")
            mydict = { "id": id, "titulo": titulo, "data_finalizacao": data_finalizacao,"local_realizacao": local_realizacao,"tipo" : tipo}
            print("foi adicionado")
        if opcao == 2:
            #Editar dados
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Publicacao"]
            titulo = input("Qual o titulo da Publicação deseja alterar")
            myquery = { "id": titulo }
            Ntitulo = input("Insira o novo titulo:")
            Ndata_finalizacao = input("Atualize a data de finalização:")
            Nlocal_realizacao = input("Atualize a local de finalização")
            newvalues = { "$set": { "titulo": Ntitulo, "data_finalizacao": Ndata_finalizacao,"local_realizacao": Nlocal_realizacao } }
            mycol.update_one(myquery, newvalues)
            #print "customers" after the update:
            for x in mycol.find():
                print("foi editado")
                print(x)
        if opcao == 3:
            #Eliminar dados
            mydb = myclient["Plataforma_departamental"]
            mycol = mydb["Publicacao"]
            remover = input("Insira o Titulo da Publicação que deseja remover")
            myquery = { "titulo": remover }
            mycol.delete_one(myquery)
            for x in mycol.find():
                print("foi eliminado")
                print(x)
        if opcao == 4:
            print('Procura documentos com condições AND e OR')
            for x in myclient.Plataforma_departamental.Publicacao.find({"$or":[{"id": {"$gt": 37}}, {"$and":[{"id": {"$gt": 40}}]}]}):
                print(x)
        if opcao == 5:
            main()
        else:
            print('Opção inválida!')
            print('=-='*10)
        print('O programa acabou !')

def main ():
    print('''    [1]Utilizador
    [2] Escola
    [3] Diretor
    [4] Projeto
    [5] Publicacao 
    ''')
    opcao= int(input("Qual a opção que deseja realizar"))
    if opcao == 1:
        mydb = myclient["Plataforma_departamental"]
        mycol = mydb["Utilizador"]

        mylist = [
            { "password": "6958", "tipo": "docente", "email": "testetstetstet"},
            { "password": "3255", "tipo": "admin", "email": "testetstetstet"},
            { "password": "87846", "tipo": "docente", "email": "testetstetstet"},
            { "password": "21235", "tipo": "docente", "email": "testetstetstet"},
            { "password": "2144", "tipo": "docente", "email": "testetstetstet"},
            { "password": "54221", "tipo": "docente", "email": "testetstetstet"},
            { "password": "45452", "tipo": "docente", "email": "testetstetstet"},
            { "password": "42410", "tipo": "docente", "email": "testetstetstet"},
            { "password": "2442421", "tipo": "docente", "email": "testetstetstet"}
        ]
        x = mycol.insert_many(mylist)
        menuU()

    if opcao == 2:
        mydb = myclient["Plataforma_departamental"]
        mycol = mydb["Escola"]
        mylist = [{"nome": "EscolaABC", "sigla": "ABC", "id_instituição": "1"},
                  {"nome": "EscolaDEF", "sigla": "DEF", "id_instituição": "1"},
                  {"nome": "EscolaGHI", "sigla": "GHI", "id_instituição": "1"},
                  {"nome": "EscolaJKL", "sigla": "JKL", "id_instituição": "1"},
                  {"nome": "EscolaMNO", "sigla": "MNO", "id_instituição": "1"},
                  {"nome": "EscolaPQR", "sigla": "PQR", "id_instituição": "1"},
                  {"nome": "EscolaSTU", "sigla": "STU", "id_instituição": "1"},
                  {"nome": "EscolaVXY", "sigla": "VXY", "id_instituição": "1"},
                  {"nome": "EscolaZ", "sigla": "Z", "id_instituição": "1"}]
        x = mycol.insert_many(mylist)
        menuEsc()

    if opcao == 3:
        mydb = myclient["Plataforma_departamental"]
        mycol = mydb["Diretor"]
        mylist = [
            { "id_docente": "2", "id_escola": "4", "data_inicio": "2015-10-10T00:00:00"},
            { "id_docente": "8", "id_escola": "6", "data_inicio": "2018-02-10T00:00:00"},
            { "id_docente": "8", "id_escola": "9", "data_inicio": "2018-01-12T00:00:00"},
            { "id_docente": "5", "id_escola": "1", "data_inicio": "2019-02-10T00:00:00"},
            { "id_docente": "2", "id_escola": "6", "data_inicio": "2008-02-10T00:00:00"},
            { "id_docente": "3", "id_escola": "6", "data_inicio": "2018-08-10T00:00:00"},
            { "id_docente": "3", "id_escola": "5", "data_inicio": "2011-02-10T00:00:00"},
            { "id_docente": "8", "id_escola": "9", "data_inicio": "2016-02-10T00:00:00"},
            { "id_docente": "7", "id_escola": "1", "data_inicio": "2018-12-10T00:00:00"},
        ]
        x = mycol.insert_many(mylist)
        menuDir()

    if opcao == 4 :
        mydb = myclient["Plataforma_departamental"]
        mycol = mydb["Projeto"]

        mylist = [
        {"titulo": "Projeto1", "data_inicio":"2009-08-28T10:58:00","data_fim":"2015-08-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"200"},
        {"titulo": "Projeto 2 ", "data_inicio":"2013-08-28T10:58:00","data_fim":"2015-07-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"300"},
        {"titulo": "Projeto 3", "data_inicio":"2013-08-28T10:58:00","data_fim":"2015-06-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"400"},
        {"titulo": "Projeto 4", "data_inicio":"2013-08-28T10:58:00","data_fim":"2015-05-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"500"},
        {"titulo": "Projeto 5", "data_inicio":"2013-08-28T10:58:00","data_fim":"2015-04-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"600"},
        {"titulo": "Projeto 6", "data_inicio":"2013-08-28T10:58:00","data_fim":"2015-03-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"700"},
        {"titulo": "Projeto 7", "data_inicio":"2013-08-28T10:58:00","data_fim":"2015-02-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"450"},
        {"titulo": "Projeto 8", "data_inicio":"2013-08-28T10:58:00","data_fim":"2015-01-01T10:08:00", "local_realizacao": "IPB","valor_financiado":"220"}
        ]
        x = mycol.insert_many(mylist)
        menuProj()


    if opcao == 5:
        mydb = myclient["Plataforma_departamental"]
        mycol = mydb["Publicacao"]
        mylist = [{ "id": "110", "titulo": "teste0", "data_finalizacao": "2015-01-10","local_realizacao": "Local0","tipo" : "artigo"},
                  { "id": "111", "titulo": "teste1", "data_finalizacao": "2015-01-11","local_realizacao": "Local1","tipo" : "livro"},
                  { "id": "112", "titulo": "teste2", "data_finalizacao": "2015-01-12","local_realizacao": "Local2","tipo" : "cronica"},
                  { "id": "113", "titulo": "teste3", "data_finalizacao": "2015-01-13","local_realizacao": "Local3","tipo" : "revista"},
                  { "id": "114", "titulo": "teste4", "data_finalizacao": "2015-01-14","local_realizacao": "Local4","tipo" : "livro"},
                  { "id": "115", "titulo": "teste5", "data_finalizacao": "2015-01-15","local_realizacao": "Local5","tipo" : "livro"}]
        x = mycol.insert_many(mylist)
        menuPub()

main()



