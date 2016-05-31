
## O que foi feito?



- Primeiramente, deverão ser criados dois modelos. Um modelo base que terá dois atributos, 1 inteiro e um de texto e um modelo de log que servirá como utilitário da aplicação. ![alt text][done]



2 - Deverão ser criadas utilizando as Class-Based Views do Django páginas onde possam ser criados, deletados, atualizados, detalhados e listados itens do modelo base. A listagem dos itens deve ser paginada por 500.

3 - Deverá haver um campo de busca com "autocomplete" no topo. Quando o usuário digitar 3 letras deverá ser trazido no "autocomplete" os itens com esses

caracteres dispostos consecutivamente no campo de texto.

4 - Deverá ser criado uma página de lista para o log onde as últimas modificações

deverão ficar aparentes no topo além de uma interface de busca para a mesma.

5 - Uma tarefa assíncrona deverá adicionar 1000 novos itens no modelo base a cada 2 minutos (o tempo pode mudar de acordo com a preferência do candidato). Os valores inteiros deverão ser gerados randomicamente. Já os valores de texto deverão ser obtidos através de uma api *.

6 - Para cada novo modelo criado, visualizado ou atualizado deverá ser registrado no modelo de log através de um sinal do Django.

7 - Para cada modelo deletado deverá ser registrado no modelo de log assíncronamente através do Celery.

8 - As buscas deverão utilizar o ElasticSearch.

9 - Provisionar um servidor (Amazon/Heroku/DigitalOcean) e realizar o deploy para teste na web.

10 - O código deverá ser disposto no Github com instruções para a montagem em um arquivo README.md. Comentários podem ser adicionados no COMMENTS.md.

* Os valores de texto deverão ser os nomes gerados por quaisquer api dos sites abaixo.

- http://namey.muffinlabs.com/

- http://uinames.com/

- https://randomuser.me/

Aconselhamos a utilização das tecnologias abaixo:

    - Celery + Django-Celery

    - ElasticSearch + Django-Haystack

    - Integração com libs JS como Chosen, Select2 ou selectize.js

    - Django Rest Framework

    - Requests + Scrapy + Selenium



[done]: http://interactive.snm.org/img/icons/application_basics/16x16/plain_gif/check.gif