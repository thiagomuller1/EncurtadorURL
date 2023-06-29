Documentação do Projeto de Encurtador de URL
Arquitetura do Sistema
O projeto de encurtador de URL é uma aplicação web que permite aos usuários encurtar URLs longas em URLs curtas e amigáveis. A arquitetura do sistema é composta por diferentes componentes que trabalham juntos para fornecer essa funcionalidade.

Componentes do Sistema:

API Gateway: O API Gateway é responsável por receber as solicitações dos clientes, autenticar e direcionar as solicitações para os serviços apropriados. Ele atua como um ponto de entrada para a aplicação e gerencia as rotas e autenticação.
Serviço de Encurtamento: Este serviço é responsável por receber a URL longa fornecida pelo cliente, gerar uma URL curta exclusiva, armazenar a correspondência entre as URLs longa e curta em um banco de dados e retornar a URL curta para o cliente.
Serviço de Redirecionamento: Este serviço é responsável por receber uma URL curta do cliente, pesquisar no banco de dados a URL longa correspondente e redirecionar o cliente para a URL longa.
Banco de Dados: O banco de dados é responsável por armazenar as informações de mapeamento entre as URLs longa e curta. Pode ser utilizado um banco de dados relacional, como o PostgreSQL ou SQLite, para essa finalidade.
Cache: O cache é responsável por armazenar em memória as URLs curtas mais acessadas, a fim de melhorar o desempenho e reduzir a carga nos serviços de redirecionamento.
Tecnologias Utilizadas
O projeto utiliza as seguintes tecnologias:

Python: A linguagem de programação principal utilizada para desenvolver a aplicação.
Flask: Um framework leve e fácil de usar para desenvolvimento de aplicações web em Python. É utilizado para criar a API e gerenciar as rotas e requisições HTTP.
SQLAlchemy: Uma biblioteca de mapeamento objeto-relacional (ORM) que simplifica a interação com o banco de dados e permite a modelagem de objetos Python como tabelas no banco de dados.
PostgreSQL: Um banco de dados relacional utilizado para armazenar as informações de mapeamento entre as URLs longa e curta.
Redis: Um sistema de cache em memória utilizado para armazenar as URLs curtas mais acessadas, melhorando o desempenho e a eficiência da aplicação.
Docker: Uma plataforma de contêinerização que permite empacotar a aplicação e suas dependências em contêineres isolados, facilitando a implantação e execução em diferentes ambientes.
Decisões de Design
Separar Responsabilidades: O sistema foi projetado para seguir o princípio de separação de responsabilidades. O API Gateway é responsável pelo roteamento e autenticação, enquanto os serviços de encurtamento e redirecionamento são responsáveis por suas respectivas funcionalidades. Isso permite escalabilidade e manutenção mais fácil dos componentes individuais.
Uso de Cache: Para melhorar o desempenho e reduzir a carga nos serviços de redirecionamento, foi implementada uma estratégia de cache utilizando o Redis. As URLs curtas mais acessadas são armazenadas em cache, proporcionando tempos de resposta mais rápidos para essas URLs.
Autenticação via API Key: Para garantir a segurança das chamadas à API do encurtador de URL, foi implementado um mecanismo de autenticação baseado em API Key. Os clientes devem fornecer uma chave de API válida para acessar os serviços. Isso ajuda a proteger contra acesso não autorizado aos recursos do sistema.
Diagrama da Arquitetura
Aqui está um diagrama simplificado que ilustra a arquitetura do sistema:

              +--------------+
              |  API Gateway |
              +------+-------+
                     |
                     | (autenticação, roteamento)
                     |
              +------+-------+
              | Encurtamento |
              +------+-------+
                     |
                     | (encurtamento de URL, armazenamento no banco de dados)
                     |
              +------+-------+
              | Redirecionar |
              +------+-------+
                     |
                     | (pesquisa no banco de dados, redirecionamento)
                     |
              +------+-------+
              |   Banco de   |
              |    Dados     |
              +------+-------+
                     |
                     | (armazenamento de URLs longas e curtas)
                     |
              +------+-------+
              |    Cache     |
              +--------------+
