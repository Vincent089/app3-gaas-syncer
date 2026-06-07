install:
	pip install -e .

uninstall:
	pip uninstall -y gaas_syncer

run:
	python src/vlan_manager/main.py

unit-test:
	pytest tests/unit

integration-test:
	pytest tests/integration

test:
	pytest --cov-report term:skip-covered --cov-report html --cov=src tests

build-image:
	docker build . -f .\.devcontainer\Dockerfile -t app3-gaas-syncer

deploy:
	kubectl create configmap gaas-syncer-envconfig --from-env-file=.devcontainer/.env --dry-run=client -o yaml | kubectl apply -f -
	skaffold dev -f .devcontainer/skaffold.yaml
