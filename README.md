# Projeto-Integrador-II-Back
1. Introdução
O sistema será implementado visando atender todas as necessidades da biblioteca, dando suporte a todas as atividades inerentes ao ambiente da biblioteca. Tal sistema tem por finalidade controlar entrada e saída de acervos, controle de usuários, e emissão de relatórios gerenciais, pesquisa com direito a localização de onde existem determinados livros.
O sistema deve facilitar o gerenciamento da biblioteca, tornando os processos mais ágeis e eficazes, trazendo benefícios para os alunos, professores e para as instituições, melhorando assim o controle das movimentações de livros. Além disso, trará facilidades ao acesso das informações importantes para o auxílio na administração da biblioteca. Como a informática hoje é essencial em qualquer ramo de atividade, o software irá suprir toda necessidade de organização, fornecendo relatórios gerenciais que são de extrema importância para uma eventual tomada de decisão, assim garantindo a qualidade de serviço prestado.

1.1 Funcionalidades:
Manter Livro : Criação, edição e exclusão do item citado.
Realizar Empréstimo: Criação e edição do item citado.
Realizar Devolução: Criar e editar registro de devolução de livros que foram emprestados, para constar no sistema.
Manter Categoria: Criação, edição e exclusão do item citado.
Pesquisar por categoria;
Autenticação: Efetuar login de usuários
Registro de Movimentação como: empréstimo e devolução de obras.

2 - Casos de Uso
![caso de uso int  II](https://github.com/keilanyg/Projeto-Integrador-II-Back/assets/112432902/c8c9fb9d-d805-4ad7-bac9-60124ee6d6e7)

3 - Modelo Lógico
![modelo lógico](https://github.com/keilanyg/Projeto-Integrador-II-Back/assets/112432902/99a8161e-c736-495d-b51b-33bad1112365)

4. Processo de Software - Desenvolvimento Incremental
O Processo de Desenvolvimento Incremental foi escolhido pois o sistema está sendo desenvolvido em partes menores, onde elas são entregues por etapas, e a cada etapa será acrescentado ou aprimorado uma nova funcionalidade.

5. Arquitetura de Software -  Arquitetura baseadas em multicamadas
Foi utilizada pois ela usa a interface para executar seus procedimentos, o que torna o sistema independente de localização, podendo estar tanto na mesma máquina como em máquinas separadas. A aplicação pode ser dividida por partes, cada uma responsável por determinadas funções. 
Uma aplicação desenvolvida neste modelo apresenta várias vantagens, dentre elas pode-se destacar a modularização, a facilidade de redistribuição, a economia de conexões no servidor e a escalabilidade.
