# Descomplicando o Prometheus

## DAY-9

### O que iremos ver hoje?
Hoje é dia de falar sobre o relabeling, uma sensacional técnica para deixar as suas métricas ainda mais organizadas e fáceis de serem consultadas.

Com o relabeling você consegue adicionar novas labels, remover labels, juntar labels, e muito mais.

Tenho certeza que depois do dia de hoje você irá ver com outros olhos as métricas e como elas podem ser organizadas.

Basicamente hoje vamos brincar com o nosso ServiceMonitor/PodMonitor  e brincar com as labels, regras e relabelings... Relabeling tudo que é lugar. hahaha :D

Bora lá! 

### Conteúdo do Day-9

<details>
<summary class="summary">DAY-9</summary>

- [Descomplicando o Prometheus](#descomplicando-o-prometheus)
  - [DAY-9](#day-9)
    - [O que iremos ver hoje?](#o-que-iremos-ver-hoje)
    - [Conteúdo do Day-9](#conteúdo-do-day-9)
    - [O que é Relabeling?](#o-que-é-relabeling)
      - [Como funciona o Relabeling?](#como-funciona-o-relabeling)
      - [Exemplos de uso do Relabeling](#exemplos-de-uso-do-relabeling)
        - [ Removendo uma métrica baseado em uma label](#removendo-uma-métrica-baseado-em-uma-label)
        - [Junta duas labels em uma só](#junta-duas-labels-em-uma-só)
        - [Adicionando uma nova label](#adicionando-uma-nova-label)
        - [Armazenando somente métricas específicas](#armazenando-somente-métricas-específicas)
        - [Mapeando todas as labels do Kubernetes](#mapeando-todas-as-labels-do-kubernetes)
    - [As meta labels do Prometheus](#as-meta-labels-do-prometheus)

</details>


#### O que é Relabeling?

Hoje iremos falar sobre o relabeling, que é uma das funcionalidades mais poderosas do Prometheus. O relabeling é uma funcionalidade que permite que você faça alterações nos metadados de seus targets, como por exemplo, adicionar labels, remover labels, modificar labels, etc.

Por exemplo, você pode usar o relabel para renomear uma label ou removê-la completamente, ou para adicionar uma nova label com um valor específico. O relabel também pode ser usado para filtrar métricas com base em suas labels ou para ajustar seus valores.

##### Como funciona o Relabeling?

O relabeling é feito através de regras que são aplicadas a cada target. Essas regras são definidas no arquivo de configuração do Prometheus, no bloco `relabelings` conforme o exemplo abaixo:

```yaml
      relabelings: # regras de relabeling
        - sourceLabels: [__meta_kubernetes_service_label_team] # label original que será usada como base para a regra
          regex: '(.*)' # regex que será aplicada na label original
          targetLabel: team # label que será criada
          replacement: '${1}' # valor que será atribuído a label criada, neste caso, o valor da label original
```

Somente para ficar mais claro, vou colocar abaixo todo o nosso arquivo de configuração do `ServiceMonitor`:

```yaml
apiVersion: monitoring.coreos.com/v1 # versão da API
kind: ServiceMonitor # tipo de recurso, no caso, um ServiceMonitor do Prometheus Operator
metadata: # metadados do recurso
  name: nginx-servicemonitor # nome do recurso
  labels: # labels do recurso
    app: nginx # label que identifica o app
spec: # especificação do recurso
  selector: # seletor para identificar os pods que serão monitorados
    matchLabels: # labels que identificam os pods que serão monitorados
      app: nginx # label que identifica o app que será monitorado
  endpoints: # endpoints que serão monitorados
    - interval: 10s # intervalo de tempo entre as requisições
      path: /metrics # caminho para a requisição
      targetPort: 9113 # porta do target
      relabelings: # regras de relabeling
        - sourceLabels: [__meta_kubernetes_service_label_team] # label original que será usada como base para a regra
          regex: '(.*)' # regex que será aplicada na label original
          targetLabel: team # label que será criada
          replacement: '${1}' # valor que será atribuído a label criada, neste caso, o valor da label original
```

Percebe, somente adicionamos o bloco `relabelings` e dentro dele adicionamos as regras de relabeling. Agora, vamos entender como funciona cada uma dessas regras.

* `sourceLabels`: é a label original que será usada como base para a regra. Neste caso, estamos usando a label `__meta_kubernetes_service_label_team` que vou explicar logo menos o que significa.
* `regex`: é a regex que será aplicada na label original. Neste caso, estamos usando a regex `(.*)` que significa que será aplicada a regex em toda a label original.
* `targetLabel`: é a label que será criada. Neste caso, estamos criando a label `team`.
* `replacement`: é o valor que será atribuído a label criada. Neste caso, estamos atribuindo o valor da label original.

Simples demais, né? Evidente que existem outras regras que podem ser usadas, e tudo vai depender da sua necessidade e da sua criatividade! Acessar a documentação oficial do projeto com certa frequência é super importante, portanto, o faça!

##### Exemplos de uso do Relabeling

###### Removendo uma métrica baseado em uma label

Essa regra de relabeling está definindo que a etiqueta endpoint será removida (drop) das métricas coletadas pelo Prometheus. Isso significa que todas as métricas coletadas que possuem essa etiqueta serão descartadas e não estarão disponíveis para consulta posterior.

É sempre muito bom usar essa regra com muita atenção, pois ela pode fazer com que você perca muitas métricas que podem ser muito importantes para você.

```yaml
      relabelings: # regras de relabeling
        - sourceLabels: [app] # label original que será usada como base para a regra
          action: drop # ação que será aplicada na label original
```

Com isso, toda métrica que possuir a label `app` não será coletada pelo Prometheus.


###### Junta duas labels em uma só

Caso queira juntar duas labels em uma só, é super simples. 

Em nosso exemplo, vamos unir as labels app e team para criar um label chamado `app_team`:

```yaml
      relabelings: # regras de relabeling
        - sourceLabels: [app, team] # labels originais que serão usadas como base para a regra
          targetLabel: app_team # label que será criada
          regex: (.*);(.*) # regex que será aplicada nas labels originais, neste caso, estamos usando uma regex que irá separar as labels originais em dois grupos
          replacement: ${1}_${2} # junção das labels originais
```

Com isso, criamos uma terceira label chamada `app_team` que é a junção das labels `app` e `team`.


###### Adicionando uma nova label

Vamos imaginar agora que queremos adicionar uma nova label em nossa métrica. No nosso exemplo, nós estamos com o nosso cluster EKS rodando na região `us-east-1`, certo? E se nós adicionarmos uma label chamada `region` com o valor `us-east-1` em todas as nossas métricas para esse `target`? Seria legal hein!

Para fazer isso, basta adicionar a seguinte regra:

```yaml
      relabelings: # regras de relabeling
        - sourceLabels: [] # Valor vazio, pois não estamos usando nenhuma label original
          targetLabel: region # label que será criada
          replacement: us-east-1 # valor que será atribuído a label criada
```

###### Armazenando somente métricas específicas

Agora é o seguinte, eu somente quero armazenas as métricas que possuem a label `app` com o valor `nginx` ou `redis`. Como eu faço isso?

Bom, é super simples, basta adicionar a seguinte regra:

```yaml
      relabelings: # regras de relabeling
        - sourceLabels: [app] # label original que será usada como base para a regra
          regex: '(nginx|redis)' # regex que será aplicada na label original
          action: keep # ação que será aplicada na label original
```

Perceba que estamos usando a regex `(nginx|redis)` que significa que iremos armazenar somente as métricas que possuem a label `app` com o valor `nginx` ou `redis` e ainda estamos usando a ação `keep` que significa que iremos armazenar somente as métricas que possuem essas labels.


###### Mapeando todas as labels do Kubernetes

Uma forma super simples de adicionar todas as labels que estão declaradas em um service ou pod é usando a meta label `__meta_kubernetes_service_label_<nome_da_label>` ou `__meta_kubernetes_pod_label_<nome_da_label>`. 

Porém e se quisermos fazer isso de forma dinâmica? Como podemos fazer isso?

Vamos para um exemplo onde iremos pegar todas as labels de um service e adicionar em uma métrica. Vamos supor que temos um service com o seguinte arquivo:

```yaml
apiVersion: v1 # versão da API
kind: Service # tipo de recurso, no caso, um Service
metadata: # metadados do recurso
  name: nginx-svc # nome do recurso
  labels: # labels do recurso
    app: nginx # label para identificar o svc
    team: platform-engineering
    environment: production
    version: 1.0.0
    type: web
spec: # especificação do recurso
  ports: # definição da porta do svc 
  - port: 9113 # porta do svc
    name: metrics # nome da porta
  selector: # seletor para identificar os pods/deployment que esse svc irá expor
    app: nginx # label que identifica o pod/deployment que será exposto
```

Adicionamos algumas tags em nosso arquivo somente para ficar mais fácil de entender o exemplo.

Agora vamos adicionar a nossa regra para pegar todas as labels desse service e adiciona-las como labels da nossa métrica.

```yaml
      relabelings: # regras de relabeling
        - action: labelmap # ação que será aplicada na label original
          regex: __meta_kubernetes_service_label_(.+) # regex que será aplicada na label original
```

No exemplo acima, usamos a `action` `labelmap` que irá mapear todas as labels do service para labels da métrica. Usamos a regex `__meta_kubernetes_service_label_(.+)` que irá pegar todas as labels do service, e através do `.+` irá mapear todas as labels para labels da métrica.

Com isso, todas as labels que estão declaradas no service serão adicionadas como labels da métrica. \o/


#### As meta labels do Prometheus

Um coisa que é super importante é ter um bom entendimento sobre as meta labels que o Prometheus disponibiliza. Essas meta labels são labels que são adicionadas automaticamente pelo Prometheus e que podem ser usadas para criar regras de relabeling entre outras coisas.

Por exemplo, temos a meta label `__meta_kubernetes_service_label_team` que usei no exemplo anterior. Essa meta label é adicionada automaticamente, e possui a seguinte estrutura: `__meta_kubernetes_service_label_<nome_da_label>`.

No caso, em meu service eu adicionei a label `team` com o valor `platform-engineering`. Vamos dar um olhada como ficou o arquivo onde definimos o service:

```yaml
apiVersion: v1 # versão da API
kind: Service # tipo de recurso, no caso, um Service
metadata: # metadados do recurso
  name: nginx-svc # nome do recurso
  labels: # labels do recurso
    app: nginx # label para identificar o svc
    team: platform-engineering
spec: # especificação do recurso
  ports: # definição da porta do svc 
  - port: 9113 # porta do svc
    name: metrics # nome da porta
  selector: # seletor para identificar os pods/deployment que esse svc irá expor
    app: nginx # label que identifica o pod/deployment que será exposto
```

Veja que agora nós temos a label `team` com o valor `platform-engineering`, sendo assim o Prometheus vai adicionar a meta label `__meta_kubernetes_service_label_team` com o valor `platform-engineering` em todas as métricas que forem coletadas a partir desse service.

Simples demais, como tudo no Prometheus e Kubernetes!


Abaixo vou listar algumas das meta labels que o Prometheus disponibiliza:

* `__meta_kubernetes_pod_name`: nome do pod
* `__meta_kubernetes_pod_node_name`: nome do node onde o pod está rodando
* `__meta_kubernetes_pod_label_<labelname>`: valor da label do pod
* `__meta_kubernetes_pod_annotation_<annotationname>`: valor da annotation do pod
* `__meta_kubernetes_pod_container_name`: nome do container
* `__meta_kubernetes_pod_container_port_number`: número da porta do container
* `__meta_kubernetes_pod_container_port_name`: nome da porta do container
* `__meta_kubernetes_service_name`: nome do service
* `__meta_kubernetes_service_label_<labelname>`: valor da label do service
* `__meta_kubernetes_service_annotation_<annotationname>`: valor da annotation do service
* `__meta_kubernetes_endpoint_port_name`: nome da porta do endpoint
* `__meta_kubernetes_namespace`: namespace do pod/service/deployment
* `__meta_kubernetes_node_name`: nome do node
* `__meta_kubernetes_node_label_<labelname>`: valor da label do node
* `__meta_kubernetes_node_annotation_<annotationname>`: valor da annotation do node
* `__meta_kubernetes_node_address_<addressname>`: valor do endereço do node

A lista é enorme e você pode conferir no link abaixo:

https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config


E claro que nem tudo é sobre Kubernetes! Existem me labels que não são específicas do Kubernetes, como por exemplo, caso você esteja utilizando a AWS, você pode usar a meta label `__meta_ec2_instance_id` para pegar o ID da instância ou ainda o `__meta_ec2_public_ip` para pegar o IP público de uma instância.

Agora, se você estiver utilizando o GCP, você pode usar a meta label `__meta_gce_instance_id` para pegar o ID da instância ou ainda o `__meta_gce_public_ip` para pegar o IP público de uma instância, padrão é tudo, não é mesmo?

Se for Azure? Claro que temos e ainda, seguimos o mesmo padrão, ou melhor, quase o mesmo padrão. A meta label `__meta_azure_machine_id` é para pegar o ID da instância e o `__meta_azure_machine_public_ip` para pegar o IP público de uma instância.

Mais uma vez, da um olhada na documentação oficial do projeto para saber mais sobre as meta labels disponíveis.

Segue o link para a documentação oficial: https://prometheus.io/docs/prometheus/latest/configuration/configuration/