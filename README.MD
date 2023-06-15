
<h1 align="center">Sistema de emprestimo financeiro</h1>

<h3 align="center">
  # Sistema de emprestimo financeiro para pessoa física.
</h3>

## :rocket: Stack

- Docker / docker-compose
- Python 3.11 (slim)
- Postgres 12.7 (alpine)
- RabbitMQ 3.9 (alpine)
- Gunicorn 20.x

## :train2: Considerações - Makefile

O `Makefile` está totalmente configurado para rodar ambas as frentes do sistema (back-end e front-end) 
execute o comando 

```bash
make
```

para ver as opções disponíveis.

## 🏃Preparando para execução

> clonando repositório:

```shell
git config pull.rebase true
git clone git@github.com:marlonmartins2/sistema-emprestimo-financeiro.git

ou com htts

git clone https://github.com/marlonmartins2/sistema-emprestimo-financeiro.git
cd sistema-emprestimo-financeiro/
```

## :train2: Rodando o Projeto

Use o Makefile para instalar e iniciar o sistema localmente com suas dependências:

```bash
make docker_up
```

## :evergreen_tree: Branchs

O projeto por hora só contem uma _branch_:

- [_master_](https://github.com/marlonmartins2/sistema-emprestimo-financeiro/tree/master) : contento a ultima versão estável do projeto.
