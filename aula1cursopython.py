#Passo 1 - entrar sistema da empresa 

#Passo 2 -Fazer login

#Passo 3 - Pegar base de dados

#Passo 4 - cadastrar todos os produtos

#Link : https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pyautogui                  #ferramenta #é um pacote de código #automatiza mouse,teclado,tela do pc
import pyautogui #estou importando o pacote
import time #bilbioteca . comtrola o tempo


#pyautogui.click-clica com o mouse
#pyautogui.write-escreve com o teclado/texto
#pyautogui.press-pressiona tecla
#pyautogui.hotkey-combinação de teclas (Crtl C)
#pyautogui.scroll - roller do mouse
pyautogui.PAUSE = 0.3 #pausa entre comandos do pyautogui  


#Passo1 - Entrar no sistema
#Passo2- Abrir navegador
#Passo3- Entrar no navegador

pyautogui.press("Win") #pressiona tecla windows
pyautogui.write("Navegador Opera GX")#escreve navegador
pyautogui.press("Enter") #abre navegador

pyautogui.click(x=617, y=51)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #digitar o link
pyautogui.press("Enter")#acessando o link

time.sleep(3)  #semelhante ao ao pyautogui.PAUSE , só que para um comando em específico 

#fazer login no sistema
pyautogui.click(x=844, y=387) #selecina eamil
pyautogui.hotkey("Ctrl","A") #seleciona campo email todo A
pyautogui.write("teste@oi.com.br")#escreve meu email

pyautogui.press("Tab")#passa direto pra senha
pyautogui.write("minha senha")

pyautogui.click(x=995, y=560)#clicando para logar

time.sleep(3)

#Passo4-importar base de dados
import pandas  #ferramenta para base de dados

tabela = pandas.read_csv("produtos.csv")   #comando para lercodigo  marca   tipo    categotia   preco   custo   obs 
#base de dados
#variável tabela recebe oq o pandas vai ler 
#Passo5-cadastrar o produto


for linha in tabela.index:
                #estrutura de epetição #.index é a lista #index é o número da linha
    #codigo produto
    pyautogui.click(x=1433, y=248)
    pyautogui.press("Tab")
    codigo = str (tabela.loc[linha,"codigo"])                    #.loc==localiza os dados #exceção que usa colchete  #str==string  #codigo é a variavel tipo string que vai receber a coluna dos dados referente ao código do produto
    pyautogui.write(codigo)

    #marca
    pyautogui.press("Tab")
    marca = str (tabela.loc[linha,"marca"])  
    pyautogui.write(marca)



    #tipo
    pyautogui.press("Tab")
    tipo = str (tabela.loc[linha,"tipo"])  
    pyautogui.write(tipo)


    #categoria
    pyautogui.press("Tab")
    categoria= str (tabela.loc[linha,"categoria"])  
    pyautogui.write(categoria)



    #preco unitário
    pyautogui.press("Tab")
    preco_unitario = str (tabela.loc[linha,"preco_unitario"])  
    pyautogui.write(preco_unitario)


    #custo
    pyautogui.press("Tab")
    custo = str (tabela.loc[linha,"custo"])  
    pyautogui.write(custo)


    #obs
    pyautogui.press("Tab")
    obs = str (tabela.loc[linha,"obs"])

    if obs != "nan":          #nan(not a number) informação que o python não reconheceu , informação vazia
        pyautogui.write(obs)

    #enviar dados produto
    pyautogui.press("Tab")
    pyautogui.press("Enter")

    
    pyautogui.scroll(5000)

    time.sleep(3)

#Passo6-repetir para todos os produtos