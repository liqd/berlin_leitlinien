VIRTUAL_ENV ?= venv
NODE_BIN = node_modules/.bin

.PHONY: install
install:
	npm install --no-save
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

.PHONY: makemessages
makemessages:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -l de

.PHONY: server
server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8008

.PHONY: lint-quick
lint-quick:
	. $(VIRTUAL_ENV)/bin/activate && $(NODE_BIN)/polylint -SF

.PHONY: release
release: export DJANGO_SETTINGS_MODULE ?= berlin_leitlinien.settings.build
release:
	npm install --silent
	npm run build:prod
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py compilemessages -v0
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0

