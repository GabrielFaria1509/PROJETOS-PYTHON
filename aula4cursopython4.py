#Título : Hashzap
#Botão: Inicar Chat
  #pop-up/modal/alerta
    #título : bem vindo ao hashzap 
    #Campo de texto : escreva seu nome no chat
    #Campo de texto : escreva seu nome no chat

#flet = pacote para aplicativo/site/programa de compitador
#pip install flet

#Passo 1 - importar flet
import flet as ft

#Passo 2 - criar função principal do sistema
def main(pagina):                                            #CRIO ELEMENTOS FORA DA FUNÇÃO E DEPOIS ADICIONO DENTRO
  #criar alguma coisa e dpepois colocar na página
  #título
  titulo = ft.Text("Hashzap")

  #criar um tunel de comunicação(primeiro cria a função que o tunel vai executa(def...(evento)), segundo cria o tunel passando a função que ele vai executar(.pubsub.subscribe(função)),usar comando para enviar as coisas(.pubsub.send_all(oq deseja enviar)))
  def enviar_mensagem_tunel(mensagem):
    chat.controls.append(ft.Text(mensagem)) #adiciona na coluna de chat no tunel de comunicação , aparece mensagem para todo mundo
    pagina.update() #preciso atualizar a página para todos
    
  pagina.pubsub.subscribe(enviar_mensagem_tunel)    #cria o tunel de comunição
  



  titulo_janela = ft.Text("Bem vindo ao hashzap")             #coisas que aparecem na janela
  campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat") #textfield o usuariuo que preenche
  
  #criar o campo de texto enviar mensagem
  texto_mensagem = ft.TextField(label="Digite sau mensagem")  #on_submit é o on_click para tecla enter

  def enviar_mensagem(evento):
    texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
    #enviar mensagem no chat:
    
    

    #enviar mensagem no tunel
    pagina.pubsub.send_all(texto)    #envia mensagem no tunel
    
     # limpar campo de mensagem
    texto_mensagem.value=""

    pagina.update()
  
  #criar o botão enviar mensagem
  botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)
  chat = ft.Column()

  #colunas e linhas
  linha_mensagem = ft.Row([texto_mensagem,botao_enviar])          #ft.Row(oq quero colcoar na linha) adiciona linhas
  
  
  def entrar_chat(evento):
    #tirar o título da página

    pagina.remove(titulo)
   
    #tirar o botão inciar
    
    pagina.remove(botao_inciar)
    #fechar o popup/janela

    janela.open=False                  #exceção #não adiciona e removo # ele sempre tá ali , só escolho exibir ou n # é o dialog da página
    #criar o chat
    pagina.add(chat)
    #adicionar linha de mensagem
    pagina.add(linha_mensagem)
    
    
    #escrever que usuario entrou no chat
    texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"                             #f uso para valores dinâmicos , mudam td hr, coloco oq quero q seja dinÂmico em chaves{... .value}
    pagina.pubsub.send_all(texto_entrou_chat)               #adiciona item na lista do chat #.append adiciona elemento
    
    pagina.update()
  
  
  
  botao_entrar = ft.ElevatedButton("Entrar no chat",on_click=entrar_chat)


  janela = ft.AlertDialog(           #insiro o que eu quero que tenha na janela #AlerDialog é a caixa de diálogo
    title=titulo_janela,
    content=campo_nome_usuario,
    actions=[botao_entrar]
  )
  
  
  def abir_popup(evento):                        #funções de botão precisa de um evento
    pagina.dialog = janela        #caixa de diálogo da página é o popup
    janela.open=True          #abro a janela
    pagina.update()          #TODA VEZ QUE FAÇO UMA EDIÇÃO VISUAL PRECISO FALAR PRO CÓDIGO ATUALIZAR A PÁGINA
              
  
  
  botao_inciar = ft.ElevatedButton("Iniciar Chat",on_click=abir_popup )             #botões precisam de um parametro/evento ,nesse caso é on_click=função q vai ser executada #ao clicar executa a função tal
  
  pagina.add(titulo)
  pagina.add(botao_inciar)


#Passo 3 - executar o sistema
ft.app(main , view=ft.WEB_BROWSER)      #view. é como quero ver