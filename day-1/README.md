# Descomplicando o Prometheus

## DAY-1

### O que iremos ver hoje?

Durante o dia de hoje, nós iremos focar em o que é o Prometheus e qual problema ele resolve.
Iremos entender os diferentes tipos de monitoramento e as diferenças entre eles.
Hoje é dia de conhecer a história do Prometheus e também a motivação para a sua criação lá na SoundCloud.
Vamos entender a arquitetura do Prometheus e como ele se relaciona com outros aplicativos. Vamos entender o *data model* do Prometheus, descomplicando esse assunto e fazendo com que você domine esse assunto e afaste todos os seus medos. :D
E por fim, vamos instalar o Prometheus e fazer a nossa primeira configuração para o nosso serviço de monitoração.


### Por que precisamos de ferramentas como o Prometheus?

Sei que ainda não falamos sobre o que é monitoramento em si, mas acho importante trazer esse cenário para que você entenda depois o que é e para que serve o Prometheus e essa tal de monitoração.

Bem, como você sabe toda empresa possui um ambiente, onde uma ou mais aplicações estão em execução consumindo algum recurso computacional, seja local, em algum datacenter ou ainda em algum cloud provider, o que é mais comum hoje em dia.

Vamos imaginar que temos um loja online, o famoso e-commerce. Você consegue imaginar a quantidade componentes que temos que monitorar para ter a certeza, ou quase, de que tudo está funcionando como o esperado?

No caso do e-commerce, vamos imaginar algo bem simples e pequeno. Para ter um loja online você precisa de um servidor web, vamos pegar o Nginx.
Mas para rodar o Nginx nós vamos precisar de uma VM, container, Pod ou uma instancia no cloud, logo já temos mais coisas para nos preocupar.

Vamos imaginar que escolhemos rodar o Nginx em uma VM, somente para simplificar as coisas por enquanto. Se temos a VM, temos um hypervisor que está gerenciando a VM, temos o host onde a VM está sendo executada, temos o Linux que está instalado na VM onde o Nginx está rodando. Sem contar todos os elementos de redes envolvidos durante as requisições a essa nossa loja.

Com isso você já consegue imaginar o tamanho da encrenca, e olha que estamos falando de uma loja simples rodando em uma VM, sem se preocupar com ambientes complexos em alta disponibilidade, resilientes e que devem seguir normas para se adequarem a determinados nichos de mercado ou legislação local.

Se a gente parar para pensar somente nos itens que temos que monitorar somente no host que está hospedando essa VM já seria uma lista bem grande, e com bastante trabalho para os próximos dias.

Definitivamente o que não faltam são coisas que precisamos monitorar em nosso ambiente.

Se começar a pensar bem, vai ver que a monitoração é muito importante para as coisas do nosso dia-a-dia, onde não tem relação com o nosso trabalho. Por exemplo, agora enquanto escrevo esse material estou acompanhando o vôo de volta para o Brasil da minha Mãe e da minha sogra, tudo isso graças a algum sistema de monitoramento, que me traz esse informação em tempo real.

Perceba que monitoramento não é somente necessário para quando as coisas dão problema, o monitoramento é importante para acompanhar padrão, para entender como os seus sistemas estão operando, para acompanhar determinada atividade, como é o meu caso agora acompanhando o vôo.

Para nós profissionais de tecnologia, é fundamental ter um bom entendimento sobre a importância e como implementar um bom sistema de monitoramento para nossos serviços e sistemas.
Somente através do monitoramento vamos conseguir ter confiabilidade e eficiência em nossos serviços, trazendo muito valor ao negócio por conta da eficiência e disponibilidade de nossos sistemas.

Através da monitoração iremos entender se o nosso serviço está totalmente operacional ou se está degradado, entregando uma péssima experiência para os nossos usuários.

#### O que é monitorar?

No meu entendimento, monitorar significa ter o status atual sobre o item desejado. No caso de uma máquina física rodando Linux, eu quero monitorar o hardware para ter certeza de que problemas de aquecimento de CPU não irão atrapalhar a disponibilidade do meu sistema. Ainda usando esse exemplo, temos que monitorar o sistema operacional, pois não queremos que um disco cheio ou uma placa de rede sobrecarregada onerando o sistema inteiro.
Isso que ainda nem falamos do sistema operacional da VM e nem da própria aplicação, o Nginx.

Monitorar é você saber o que está acontecendo em sua infra, em sua app, em seu serviço em tempo real e em caso de falha ou anomalia, que as pessoas envolvidas para a recuperação daquele componente sejam notificadas com o máximo de informação para auxiliar o troubleshooting.

##### O monitoramento e a observabilidade

Agora que você já sabe o que significa monitorar (pelo menos no meu ponto de vista), acho que já podemos trazer um pouco mais de tempero nessa conversa, digo, trazer mais recursos para conseguir monitorar ainda melhor o nosso ambiente.

Usando ainda o exemplo do Nginx rodando em uma VM Linux, nós estávamos falando sobre possíveis **eventos** sobre falhas hardware ou coletando **métricas** sobre a carga de informações trafegando em nossa placa de rede, agora imagina descer um pouco mais o nível e poder **medir o tempo de cada requisição** que nosso servidor web está tratando?

Imagina ainda receber e armazenar todos **os logs** das requisições que retornaram erro para o nosso usuário ou que contenham informações sobre o desempenho de nossa aplicação?

Ou ainda, imagina fazer todo o **acompanhamento da requisição** do usuário, desde o momento que ela chegou no primeiro serviço de nossa infra, até o último milésimo de vida daquela requisição após ela passear por diversos serviços de nosso ambiente e ainda podendo entender e visualizar **métricas** internas sobre o comportamento e o consumo de recursos por sua aplicação?

E agora o melhor, imagine reunir toda essa informação e poder correlaciona-las, e ainda, visualizar essas informações de maneira **gráfica**, através de bonitos e informativos dashboards com gráficos e tabelas dos mais variados tipos?

Imaginou?

Pronto, você foi capaz de imaginar um ambiente onde seria possível ter a observabilidade em sua melhor forma! 

Observability normalmente é apoiada principalmente em 3 pilares:

- Logs
- Metrics
- Traces

Eu adiciono mais um item nessa lista, o Eventos. Ter os eventos que ocorrem em seu ambiente e correlaciona-lo com os demais pilares é sensacional demais e ajuda muito a entender o comportamento de um item no momento de um problema ou degradação do serviço. 
Então eu vou atualizar essa lista e adiciona-lo. :D

- Logs
- Métricas
- Traces
- Eventos

E para ser sincero, eu ainda adicionaria Dashboards pois acho que é fundamental ver de modo mais visual possível o resultado dos 4 pilares correlacionados através de gráficos que irão ajudar a entender o comportamento de determinado item em seu momento de falha ou degradação.

Se você possui um sistema para observar o seu ambiente que cobre esses 4 pilares, parabéns! \o/

Nos exemplos que eu listei acima e pedi para você imaginar, você pode verificar que temos exemplos para os quatro pilares da observabilidade. Volta lá e confere! 

Eu estava certo, né? haha

Ok, eu sei que você já entendeu tudo isso e agora está se perguntado:

E o que o Prometheus tem haver com tudo isso?

E eu te explico logo abaixo: :D


### O que é o Prometheus?

O Prometheus é um dos mais modernos sistemas de monitoramento, capas de coletar e guardar métricas dos mais variados componentes de suas infra-estrutura. O inicio de seu desenvolvimento se deu em 2012, porém somente foi anunciado oficialmente pela SoundCloud em 2015. Ele foi inspirado no Borgmon, plataforma de monitoramento no Google, responsável por monitor o Borg, plataforma de gerenciamento de containers do Google e conhecido também por ser o pai do Kubernetes.

O Prometheus além de ser uma ótima ferramenta para coletar métricas, ele também é capaz de armazena-las em seu próprio TSDB. Sim, ele também é um time series database! 

Eu não traduzi o time series database por que acho estranho falar banco de dados temporais, apesar de ser o certo em português. haha

Quando falamos de time series database, estamos basicamente falando sobre um banco de dados construindo para ter uma excelente performance no armazenamento e leitura de dados que são armazenados com data e hora. Sendo assim é um banco de dados projetado para lidar muito bem com dados, como por exemplo as métricas, onde é importante a data e hora. Seja na leitura e resgate de um minuto especifico durante o dia ou então na facilidade e performance para armazenar e organizar milhares, ou até milhões, de mensagens por hora. 

É possível ainda realizar riquíssimas queries para buscar a melhor correlação de métricas e visualizar através de dashboards, em sua bonita e intuitiva interface. Nós vamos falar muito mais sobre isso no decorrer do treinamento.

E antes que eu me esqueça, quando falamos em observabilidade, o Prometheus se encaixa no pilar *Métricas*, pois ele tem como função coletar e armazenar métricas de diferentes componentes em suas infra-estrutura.
E para não falar que eu não falei sobre opções de ferramentas para as outras pilastras, segue:

- Logs -> Graylog ou Datadog
- Métricas -> Prometheus
- Traces -> Jaeger ou eBPF
- Eventos -> Zabbix ou Datadog
- Visualização/Dashboards -> Grafana, Datadog ou Pixie


Pronto, agora acho que já sabemos o que é monitoração, observabilidade e o Prometheus, acho que já podemos começar a aprofundar o nosso conhecimento nessa sensacional ferramenta, o Prometheus!


#### A arquitetura do Prometheus

Fiz um desenho da arquitetura do Prometheus para que possamos ter um melhor entendimento de como ele funciona.

![Arquitetura do Prometheus](arquitetura-prometheus.jpg)





