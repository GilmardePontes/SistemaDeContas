import os.path


def qtdelem(lista):
        cont=0
        for i in lista:
                cont=cont+1
        return cont
def somaColuna(mat,qtdLinhas,qtdColunas,indiceColunas):
        soma=0
        for i in range(qtdLinhas):
                soma=soma+mat[i][1]
        return soma


def menordaColuna(mat,qtdLinhas,qtdColunas,indiceColunas):
        menor=mat[0][indiceColunas]
        for i in range(qtdLinhas):
                if menor>mat[i][indiceColunas]:
                                menor=mat[i][indiceColunas]
        return menor




def maiordaColuna(mat,qtdLinhas,qtdColunas,indiceColunas):
        maior=mat[0][indiceColunas]
        for i in range(qtdLinhas):
                if maior<mat[i][indiceColunas]:
                                maior=mat[i][indiceColunas]
        return maior

def apagar(mat,index):
        while index<qtdelem(mat)-1:
                mat[index]=mat[index+1]
                index=index+1
        del mat[qtdelem(mat)-1]


def menu():
        print "---"
        print "1.Cadastrar conta"
        print "2.Pagar conta"
        print "3.Visualizar todas as informacoes de todas as contas"
        print "4.Mostrar todas as informacoes da(s) conta(s) com maior valor"
        print "5.Mostrar todas as informacoes da(s) conta(s) com menor valor"
        print "6.Apresentar o valor total da(s) conta(s) a pagar"
        print "7.Sair do Programa"
        return "---"

print "1.Cadastrar conta"
print "2.Pagar conta"
print "3.Visualizar todas as informacoes de todas as contas"
print "4.Mostrar todas as informacoes da(s) conta(s) com maior valor"
print "5.Mostrar todas as informacoes da(s) conta(s) com menor valor"
print "6.Apresentar o valor total da(s) conta(s) a pagar"
print "7.Sair do Programa"
print "---"
bd=[]
if os.path.isfile("contas.txt")== True:
        arq=open("contas.txt","r")
        elemento=arq.readline()
        while elemento!='':
                x=elemento.split(";")
                y=float(x[1])
                x[1]=y
                bd.append(x[0:-1])
                elemento=arq.readline()
opcao=input()
while opcao!=7:
        if opcao==1:
                nome=raw_input("digite o nome da conta:")
                valor=input("digite o valor da conta:")
                data=raw_input("digite a data de vencimento entre /:")
                conta=[]
                conta.append(nome)
                conta.append(valor)
                conta.append(data)
                bd.append(conta)
                print "cadastro feito com sucesso!"
                print menu()
                opcao=input()
        if opcao==2:
				pagar=raw_input("digite o nome da conta para pagar:")
				i=0
				flag=False
				while i < qtdelem(bd):
					if bd[i][0]==pagar:
						apagar(bd,i)
						print "conta paga com sucesso!"
						flag=True
					else:
						i=i+1
				if flag==False:
					print "conta nao encontrada"
				print menu()
				opcao=input()
        if opcao==3:
                print "---"
                for i in range(qtdelem(bd)):
                        print "nome:",bd[i][0]
                        print "valor:",bd[i][1]
                        print "data de vencimento:",bd[i][2]
                        print "---"
                if qtdelem(bd)==0:
                        print "nao ha contas cadastradas!"
                print menu()
                opcao=input()
        if opcao==4:
                if qtdelem(bd)!=0:
                    qtdColunas=3
                    maiorvalor=maiordaColuna(bd,qtdelem(bd),qtdColunas,1)
                    for i in range(qtdelem(bd)):
                            if bd[i][1]==maiorvalor:
                                    print "**MAIOR VALOR**"
                                    print "nome:",bd[i][0]
                                    print "valor:",bd[i][1]
                                    print "data de vencimento:",bd[i][2]
                    print menu()
                    opcao=input()
                else:
                    print "nao ha contas cadastradas!"
                    print menu()
                    opcao=input()
        if opcao==5:
                if qtdelem(bd)!=0:
                    qtdColunas=3
                    menorvalor=menordaColuna(bd,qtdelem(bd),qtdColunas,1)
                    for i in range(qtdelem(bd)):
                            if bd[i][1]==menorvalor:
                                    print "**MENOR VALOR**"
                                    print "nome:",bd[i][0]
                                    print "valor:",bd[i][1]
                                    print "data de vencimento:",bd[i][2]

                    print menu()
                    opcao=input()
                else:
                    print "nao ha contas cadastradas!"
                    print menu()
                    opcao=input()
        if opcao==6:
                qtdColunas=4
                soma=somaColuna(bd,qtdelem(bd),qtdColunas,1)
                print "a soma dos valores das contas eh:",soma
                print menu()
                opcao=input()
arq=open("contas.txt","w")
for i in range(qtdelem(bd)):
        arq.write(bd[i][0]+";"+str(bd[i][1])+";"+bd[i][2]+";"+"\n")
arq.close()
print "obrigado por utilizar nosso sistema, volte sempre!"
raw_input()
