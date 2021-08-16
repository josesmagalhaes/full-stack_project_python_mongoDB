# full-stack_project_Python_mongoDB
Simples formulário de Registros com Python + Flask + Mongo DB
 
![Full Stack com Python e Mongo DB](https://user-images.githubusercontent.com/31749933/129621260-6a79e0ee-9375-4bbe-8c64-75d0eb2e4b44.jpg)


### Configurações
Para começar, você precisará fazer com que o servidor MongoDB seja executado em sua máquina local. Baixe o servidor de edição da comunidade do MongoDB aqui e certifique-se de baixar e instalar a versão atual mais recente para o tipo de máquina em que está executando.

Para garantir que você tenha o MongoDB instalado corretamente, execute mongo --versione mongod --version. Se você receber um erro para qualquer um dos dois, precisará voltar e reinstalar o servidor de banco de dados.
Em seguida, para um fluxo de trabalho mais fácil, baixe o MongoDB Compass aqui e abra-o. Crie um cluster gratuito e conecte-se a ele.
### Estilização
Inicialização Felizmente pode ser mais fácil set e ele só tem que ser adicionado ao arquivo .html <link>em seu <head>antes de todas as outras folhas de estilo para carregar o nosso CSS.
Siga o procedimento em
Para o flask basta instalar o framework em seu Python
Instale e atualize usando pip :

`pip install -U Flask`
A chave secreta é necessária para manter as sessões do lado do cliente seguras. Você pode gerar alguma chave aleatória se quiser com os.random (24).
### Roteamento do aplicativo Flask
 
Agora faremos o roteamento, primeiro escreveremos a função de rota e, em seguida, o arquivo .html para o qual a rota será renderizada.
A rota do aplicativo define o nome da rota, sua prática comum para definir a página padrão como “/” o método GET é usado para solicitar dados de um recurso específico e o POST é para enviar dados a um servidor para criar / atualizar um recurso.

Crie variáveis que obtêm os dados de diferentes campos de entrada que foram feitos.
 
Se o usuário em sessão (logado) redirecionar para logado. Não queremos que o usuário logado se registre novamente enquanto na sessão duhhhhhh ...

Sessões

Ao contrário dos cookies, os dados da sessão (sessão) são armazenados no servidor. A sessão é o intervalo no qual o cliente efetua logon no servidor e efetua logoff no servidor. Os dados que devem ser salvos na sessão são armazenados temporariamente diretório no servidor.

O PS sugere não colocá-lo agora para o caso de teste o retorno (url_for (“logado”)) somente após a rota ter sido definida!

Como o MongoDB armazena dados em documentos, mais especificamente no formato JSON, é necessário pesquisar se o valor existe como pares de “chave” e “valor”. Encontrar na coleção do MongoDB `user_found = records.find_one({"name": user})`.

Consulte o usuário na coleção de registros, se existir, solicitará ao index.html que o usuário já existe. O mesmo acontece com o e-mail.
Caso contrário, a senha deve ser hash por razões de segurança, existem muitas bibliotecas de hash hashlib, passlib, sha256, bcrypt. Neste caso, escolho bcrypt.
A codificação ('utf-8') deve ser feita porque é a maneira mais eficaz de arquivar dados e também minimiza o tamanho dos dados, portanto, você deve ser capaz de economizar espaço em seu dispositivo de armazenamento.

Adicione-o em variáveis com pares de “chave” e “valor” que correspondam ao nome de sua coleção e adicione-o nos registros.

Com a conta recém-criada, redirecione para logging_in.html como o novo usuário.

![Capturar_2021_08_16_16_40_51_16](https://user-images.githubusercontent.com/31749933/129620887-6ed9b4e0-9bb5-481a-84a3-7be0c49b64cc.png)
 
### Design de superfície da página principal
 
Cada rota herdará o base.html e esse será o Navbar, porque precisamos de um Navbar estático em todos os roteadores, felizmente o Bootstrap nos cobre e você não precisa se concentrar profundamente no front end.
Portanto, o arquivo será denominado base.html, que será herdado em todos os outros arquivos .html.
 
Então, para começar `{% block content %}e{% endblock content %}` é usado para substituir partes específicas do modelo e, porque o {% block content%} está no final, outros arquivos poderão estender o arquivo base.html.  os <div class = ”navbar-nav”> a href destinam-se a redirecionar para as outras rotas definidas que serão definidas adiante. <link… bootstrap> e <scr bootsrap etc> para que você possa usar o template navbar do bootstrap.

###Landing Page
A página principal será http://127.0.0.1:5000/ quando você executa o app.py e se aplica à rota (“/”)
Começamos estendendo o “base.html”

No {% block content%} passamos os valores para formulário de inscrição.

Lembra-se de como passamos a variável message = '' no app.py e se o usuário já existe agregar valor à mensagem e render_template com message = message? bem, isso basicamente significa que o usuário pode ser notificado se o nome de usuário (a senha não corresponde ou falsa) para dar a notificação apropriada para o usuário com a ajuda de `{% if message %}{% endif %}` e dentro da senha {{mensagem}} para alterar a cor ou o estilo da caixa de mensagem.
![Capturar_2021_08_16_16_41_59_134](https://user-images.githubusercontent.com/31749933/129620820-449feb84-30da-49f6-bd51-d81b5923ebdf.png)

 
Agora finalmente estamos indo para a seção de formulários.
Nota: method = ”post” é necessário para que o formulário envie dados a um servidor. POS é um dos métodos HTTP mais comuns.
No formulário name = ”fullname” é o que está sendo recebido pela função index () user = request.form.get (“fullname”) o resto é para as propriedades de estilo.
 
### Logado
Os registrados ou logados redirecionam para '/ logging_in' e se o e-mail estiver na sessão atual renderizar o logging_in.html com o nome do e-mail, caso contrário, redirecionar para o login (porque não queremos ninguém apenas digitando '/ logging_in' para entrar sem autenticação como um usuário já registrado)
 
### Logado
Aqueles que registraram duas coisas devem acontecer

1. Você é redirecionado e exibido que efetuou login.
 
![Capturar_2021_08_16_16_40_51_16](https://user-images.githubusercontent.com/31749933/129620938-d6ddde60-0310-4044-bb74-9d71eb425c34.png)

2. No MongoDB , cada documento armazenado em uma coleção requer um campo _id exclusivo que atua como uma chave primária.
 
![Capturar_2021_08_16_16_44_24_487](https://user-images.githubusercontent.com/31749933/129620962-2fc1b8d3-dc56-4e59-8fb6-9cf969c63f8c.png)

A senha é definida como binária ('…') porque a criptografamos com bcrypt.
 
### Página de Login
Solicite a mensagem para fazer login primeiro. Como sempre obtenha os valores dos dados do formulário, neste caso apenas o email e a senha.

Verifique se o email existe em nossa coleção `email_found=records.find_one({"email": email})`
Em caso afirmativo, obtenha o valor do email e a senha desse email.

A última etapa é verificar se a senha fornecida corresponde à senha do usuário com `bcrypt.checkpw(password.encrypt('utf-8)`, passwordcheck)

Em caso afirmativo, redirecione para logado, pois esse usuário em particular irá solicitar uma mensagem correspondente para ele.

### Sair
Da mesma forma que antes, apenas os usuários que estão logados podem fazer logout. E para liberar uma variável de sessão, use o método pop ().
