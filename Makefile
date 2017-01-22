VENV_NAME=venv

VENV_ACTIVATE = ./$(VENV_NAME)/*/activate

# if `python` command is Python 3, use that, otherwise attempt to use `python3`
# only needed outside of venv; virtualenv sets up "python" symlink accordingly
ifeq ($(shell python --version | sed -e 's/Python\s\([0-9]\).*/\1/'),3)
PYTHON = python
else
PYTHON = python3
endif

.PHONY: help configure pip-install pip-uninstall upgrade clean test run debug stop build build-debug

.DEFAULT_GOAL := help

# this brilliant bit taken from http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## Show this help text
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

configure: ## set up virtualenv, pip. Installs virtualenv globally
	$(PYTHON) -m pip install virtualenv
	$(PYTHON) -m virtualenv -p $(PYTHON) $(VENV_NAME)
	. $(VENV_ACTIVATE) && pip install -r requirements.txt && deactivate

pip-install: ## install pip pkg to venv. ex: `make pip-install PKG=<pkg>`
	. $(VENV_ACTIVATE) && pip install $(PKG) && pip freeze > requirements.txt && deactivate

pip-uninstall: ## remove pkg from venv. ex: `make pip-uninstall PKG=<pkg>`
	. $(VENV_ACTIVATE) && pip uninstall $(PKG) && pip freeze > requirements.txt && deactivate

upgrade: ## upgrade pip packages in venv
	. $(VENV_ACTIVATE) && pip install --upgrade -r requirements.txt && pip freeze > requirements.txt && deactivate

clean: ## clean up all build artifacts, including packages and venv
	rm -Rf __pycache__/
	rm -Rf $(VENV_NAME)/
	rm -f *.pid

run: ## start bot service
	./run.sh & echo $$! > site.pid

stop: ## stop service
	kill $$(cat *.pid) && rm *.pid

install: clean ## set up linux daemon (assumes ubuntu/systemd)
	./install.sh
