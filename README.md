# projetoYoutan

Esse projeto é parte de um teste feio em poucos dias.

A ideia é criar um sistema de leilões, onde pessoas possam cadastrar, dar lances
e ver leilões de imóveis e automóveis.


## Requisitos do projeto:

O projeto é todo composto pro Django + Vue

As depedências do backend ficam em requirements.txt
E as dependências do frontend ficam em package.json e package-log.json

Se você está querendo rodar o projeto existem dois caminhos: Na unha, com docker.

Eu pessoal prefiro subir o projeto na mão, mas cada um tem sua preferência.


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
docker compose up --build
```
Isso já irá criar os containers e subir as aplicações 

## Considerações sobre o projeto

Conforme dito, esse é um projeto base, de uma única sprint e feito em poucos dias
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
Fique a vontade para entrar comigo e tentamos resolver o problema juntos :)
