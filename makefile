## makefile automates the build and deployment for python projects


## build config

# type of project
PROJ_TYPE =		python
PROJ_MODULES =		git
INFO_TARGETS +=		appinfo

include ./zenbuild/main.mk

.PHONY:			appinfo
appinfo:
			@echo "app-resources-dir: $(RESOURCES_DIR)"


.PHONY:			testrun
testrun:
			$(eval PY_CLI_ARGS=doit $(PY_CLI_ARGS) --outdir ${MTARG}/fake-path)
			@make PY_CLI_DEBUG=1 PY_CLI_ARGS="$(PY_CLI_ARGS)" pycli
