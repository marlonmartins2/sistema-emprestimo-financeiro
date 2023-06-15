TEST_TARGET=./src
FLAKE8_FLAGS=--ignore=W503,E501
ISORT_FLAGS=--profile=black --lines-after-import=2
PROJECT=./back_end/
MANAGE =python ./back_end/manage.py
DJANGO_SETTINGS_MODULE=DJANGO_SETTINGS_MODULE=src.settings

.PHONY: all help install clean
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
install: ## Instala / Atualiza os pacotes python no virtualenv instalado.
	pip install --no-cache -U pip setuptools wheel
	pip install --no-cache -r requirements-dev.txt
	pip install --no-cache -r requirements.txt
clean:
	@py3clean .
## @ Running
.PHONY: run shell migrations migrate empty admin up show_urls
run: ## Executa o servidor em ambiente de desenvolvimento
	${MANAGE} runserver
shell: ## Inicializa o shell
	${MANAGE} shell_plus
migrations: ## Cria as migrações
	${MANAGE} makemigrations
migrate: ## Aplica as migrações
	${MANAGE} migrate
empty: ## cria migração zerada na app escolhida.
	${MANAGE} makemigrations --empty ${APP}
admin:   ## altera senha do admin
	${MANAGE} changepassword admin
up: migrate admin run  ## Roda toda ação necessária para começar o desenvolvimento.
show_urls: ## Mostra todos os reverses das urls.
	${MANAGE} show_urls

## @ testes
.PHONY: test cover
test: ## Executa os testes
	pytest
cover: ## Executa os testes e gera o arquivo de report
	pytest

## @ lint
.PHONY: lint_black flake lint_isort lint git_lint
lint_black:
	black --check ${PROJECT}
flake:
	flake8 ${FLAKE8_FLAGS} ${PROJECT}
lint_isort:
	isort ${ISORT_FLAGS} --check ${PROJECT}
git_lint:## Executa o lint somente nos arquivos alterados (git)
	@flake8 ${FLAKE8_FLAGS} $$(git diff --name-only | grep .py)
	@isort ${ISORT_FLAGS} $$(git diff --name-only | grep .py)
lint: lint_black flake lint_isort ## Realiza a análise estática do código: black, flake, mypy e isort

## @ format python files
.PHONY: black isort format git_format
black:
	black ${PROJECT}
isort:
	isort ${ISORT_FLAGS} ${PROJECT}
git_format:## formata somente os arquivos alterados (git)
	@black $$(git diff --name-only | grep .py)
	@isort ${ISORT_FLAGS} $$(git diff --name-only | grep .py)
format: isort black ## Formata os arquivos python usando black e isort

## @ docker
.PHONY: docker_up docker_run docker_stop docker_clean
docker_up: ## Builda a imagem do docker
	@cd back_end && docker-compose up --build
docker_run: ## Roda a imagem do docker
	@cd back_end && docker-compose up
docker_stop: ## Para a imagem do docker
	@cd back_end && docker-compose stop
docker_clean: ## Limpa a imagem do docker
	@cd back_end && docker-compose down --rmi all --volumes --remove-orphans