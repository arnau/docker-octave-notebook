image := arnau/octave-notebook
name := ioctave

build: configure
	docker build -t $(image) .
.PHONY: build

configure:
	@$(if $(shell cat .git/config | grep .gitconfig),, \
          git config --add include.path $(PWD)/.gitconfig)
.PHONY: configure

install:
	docker run -d \
               --name $(name) \
               --publish 8888:8888 \
               --volume $(PWD)/notebooks:/home/jovyan/work \
               $(image)
.PHONY: install

clean:
	docker rm -vf $(name)
.PHONY: clean

logs:
	docker logs -f $(name)
.PHONY: logs
