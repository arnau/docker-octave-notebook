# Octave Notebook (Jupyter)

Docker image combining [Jupyter]() and [Octave]().


## Usage

```sh
 docker run -d --name onb -p 8888:8888 -v $(PWD)/notebooks:/home/jovyan/work arnau/octave-notebook
```
