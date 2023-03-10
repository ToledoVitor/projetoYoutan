# projetoYoutan

Esse projeto é parte de um teste feito em poucos dias.

A ideia é criar um sistema de leilões, onde pessoas possam cadastrar, dar lances
e ver leilões de imóveis e automóveis.



## Requisitos do projeto:

O projeto é todo composto pro Django + Vue

As depedências do backend ficam em requirements.txt
e as dependências do frontend ficam em package.json e package-log.json

Se você está querendo rodar o projeto existem dois caminhos: Na mão, no docker.

Eu gosto de subir o projeto na mão, mas cada um tem sua preferência.



## Subindo o projeto na mão:

Apesar de este não ser o caminho mais prático, existem algumas vantagens em subir
o projeto na mão.

Uma delas é que você fica menos preso as decisões do docker, tem mais acesso e
visibilidade do que está rodando, e consegue rodar isolado apenas uma parte ou 
outra do projeto. Além de ser mais fácil caso precise debugar algo em sua IDE.

### Se você vai seguir por esse caminho, primeiro crie sua virtualenv.

Com sua virtualenv, na raíz do projeto rode instale as dependências do backend com
`pip install -r requirements.txt`

Feito isso, instale o vue `npm install -g @vue/cli`, e as dependências do frontend
com `npm install`

Também é preciso instalar o axios `npm install axios` e bulma (pacote de css) usado
`npm install bulma`

Com os pacotes todos instalados, na raiz do projeto rode:
- `./manage.py runserver 8000` para subir o backend na porta 8000
- `npm run serve` para subir o frontend



## Subindo o projeto com docker compose:

Subir o projeto com docker possui a vantagem de ser mais prático, afinal, você
não precisa se preocupar com os requisitos de instalação, virtualenvs, portas,
tudo já está configurado para você.

### Se você vai seguir por esse caminho, o primeiro passo é instalar o docker compose.
Você pode testar a instalação com `docker compose version`

Se estiver tudo certo com sua instalação, o terminal deve lançar algo como:
```sh
Docker Compose version v2.14.1
```


Se precisar fazer a instalação, o seguinte link pode ser útil:
https://docs.docker.com/compose/install/linux/


Com o docker compose instalado, basta rodar
```sh
docker compose up --build # cria os containers e sobe as aplicações 
```


## Criando dados de teste

Como todo projeto, precisamos de dados falsos para testar a aplicação e conseguir desenvolver.
Para isso, existe um comando chamado `devdb` que fica em core/management/commands.

Esse comando popula alguns dados básicos, criando um superusuário, alguns leilões e alguns lances.
Se você estiver subindo o projeto pela primeira vez usando docker compose, o docker já deverá rodar
o comando sozinho, e no meio das mensagens do docker você deverá ver no terminal o output:

```sh
docker-django-backend     | SuperUser criado com sucesso
docker-django-backend     | Entidades Financeiras criadas com sucesso
docker-django-backend     | Imoveis criados com sucesso
docker-django-backend     | Veiculos criados com sucesso
docker-django-backend     | Leiloes criados com sucesso
docker-django-backend     | Lances criados com sucesso
```

Se você estiver subindo o projeto fora do docker, ou o comando não rodar sozinho, você pode
rodar ele com os seguintes comandos, nessa ordem.

```sh
python manage.py migrate
python manage.py devdb
```

## Usando o projeto

Se você não pulou o passo anterior, quando você tiver rodando o projeto, já irão existir alguns
dados prontos para serem usados.

Existem alguns imóveis, veículos, lances e leilões criados. Além de duas instituições
financeiras feitas para teste.

Como premissa, foi assumido que as instituições financeiras só podem ser criadas,
editadas e apagadas via admin. Elas não estão disponíves para o usuário comum.


### Acessando o admin

Com a aplicação rodando, acesse a url `/admin` para ver o painel de admin. Se você não
mudou a porta e subiu o django na porta 8000, a url que irá acessar é `http://127.0.0.1:8000/admin/`,
ou então `http://localhost:8000/admin/`

No painel de admin você pode fazer login com o usuário:
```py
Username="admin"
password="admin"
```

Esse usuário irá te dar acesso a todos as páginas e endpoints do site.
Você terá acesso a todos os dados criados, e poderá editá-los também caso queira.

Se preferir criar um novo super usuário, rode na raiz do projeto
`./manage.py createsuperuser` e insira seus dados.



### Logando seu usuário

Na url `/login` é possível fazer login com sua conta, ou cadastrar uma nova em `/signup`.

Já existe um usário criado com dados populados que sugire que use, assim, acesse
a url `/login` e faça login com o usuário:

```sh
usuario=user
senha=user_pass
```

Ao fazer o login você já será redirecionado para a página de perfil, onde existem
dados já criados.


## Considerações sobre o projeto

Esse é um projeto básico, de uma única sprint e feito em poucos dias
como um teste técnico

O projeto possui vários pontos de melhoria, alguns dos que já encontrei são:
- Melhorar tratamentos de erros
- Medir eficiência e número de queries dos endpoints
- Possibilitar resetar a senha
- Melhorar a UX do site deixando-o mais amigável
- Aviso sobre novos lances, leilões (aviso por email)
- Instalar ferramentas de observabilidade
- Instalar ferramentas de tracking

Alguns desses pontos são simples tecnicamente, mas tomariam algumas boas horas
ou alguns poucos dias para serem feitos.

É bem capaz que em um futuro retorne para refatorar alguns pedaços de códigos
feitos na pressa, e faça alguns desses items.

Mas não vou fazer nenhuma promessa por agora!


## Disclaimer

Se você por acaso estiver tentando rodar esse projeto e não esteja conseguindo
Fique a vontade para entrar em contato comigo e tentamos resolver o problema juntos :)
