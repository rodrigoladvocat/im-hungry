# I'm hungry!

## O que é isso???

  Essa automação se trata de um assistente de voz que recebe o pedido do
cliente e executa todos os passos de adição do pedido à sacola do iFood!

## Isso é mágica?

  A parte do reconhecimento de voz é simples. A função **activate_mic()** da file **alfred_class.py**
identifica o a fonte de entrada de áudio (microfone padrão), o inicia, faz um certo tratamento
de ajuste a ruídos do ambiente e, por fim, se não houver exceções, o texto gerado pela funcao 
**recognize_google()**, que recebe a entrada de áudio do microfone e converte em texto.
  
  Já a automaçao funciona com um *web scraping* simples da página do iFood.
O script inicializa uma sessão no navegador usando o *WebDriver* e loga
na plataforma do ifood com o e-mail do cliente. Para completar o login, 
o código que é enviado deve ser confirmado. No caso dessa automação, o código
é enviado pelo e-mail, que, por sua vez, é acessado pela automação, utilizando 
Google OAuth 2.0, API do GMail e algumas bibliotecas de acesso aos e-mails. Depois,
alguns botões são clicados, alguns redirecionamentos são feitos, blá blá blá...

  Então, sim, **é mágica**...

## Como rodo isso???

  Depois de instalar o python e todas as dependencias desse script, é necessário
instalar o **msedgedriver** (driver do navegador Microsoft Edge). No entanto, o código pode
ser facilmente modificado para rodar no Chrome, ou em qualquer outro navegador. Após a enxurrada
de instalações, é preciso ter uma credencial OAuth 2.0 e habilitar a API do GMail. Com a credencial
OAuth 2.0, basta baixar o arquivo json como **client_secret.json** e mover para o diretório **atual**.
Por fim, coloque seu endereço de e-mail do ifood em uma file **.env** e modifique os endereços de pedido
no dicionário **order_options**.

Ok, agora é só rodar o comando <sub>python alfred_class.py</sub> ou <sub>python3 alfred_class.py</sub>
no terminal e fazer os pedidos!
