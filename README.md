# Octave Notebook (Jupyter)

Docker image combining [Jupyter](https://jupyter.readthedocs.io/en/latest/) and [Octave](https://www.gnu.org/software/octave/).


## Usage

```sh
 docker run -d --name onb -p 8888:8888 -v $(PWD)/notebooks:/home/jovyan/work arnau/octave-notebook
```

## Credits

All notebooks in this repository are extracted from [Octave's documentation](https://www.gnu.org/software/octave/doc/interpreter/index.html).
Copyright notice below:

> Copyright © 1996-2016 John W. Eaton.
>
> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies.
>
> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one.
>
> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions.
