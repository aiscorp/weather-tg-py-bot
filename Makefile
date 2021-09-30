.ONESHELL: ;
.NOTPARALLEL: ;
default: help;

FRMT_NORM=\033[0m
FRMT_INVRS=\033[7m

.PHONY: help
help: ## Информация о доступных командах
	@egrep -h '\s##\s' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: run-db-test
run-db-test: ## Подготовить среду разработки для localhost
	export GOOGLE_APPLICATION_CREDENTIALS="./env/google-service-account.json"
	python3 dbtest.py