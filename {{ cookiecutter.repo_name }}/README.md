# {{cookiecutter.project_name}}

{{cookiecutter.description}}


Project status: TODO

Project plan:

- [x] Init
- [ ] Fill out README
- [ ] ???
- [ ] Profit


## Install requirements

This project uses [poetry](https://python-poetry.org/) for requirement and is set up for torch using cuda.
~~~
poetry install
~~~

## How to get data

TODO document how to get the data


## How to run

This project uses [just](https://github.com/casey/just)

~~~
just --list
~~~


## Project Organization

Note this project uses

- [Justfile](https://github.com/casey/just): Command runner with commands like `just data` or `just train`
- data: [data directory ](https://cookiecutter-data-science.drivendata.org/#directory-structure)
    - ./10_raw            <- The original, immutable data dump.
    - ./20_interim        <- Intermediate data that has been transformed.
    - ./30_processed      <- The final, canonical data sets for modeling.
- nbs: upyter notebooks. Name with creator's initials, a number (for ordering), and short `-` delimited description, e.g.  `jqp-1.0-initial-data-exploration`.
- pyproject.toml:   defines poetry project dependencies and build configuration
- {{cookiecutter.project_name}}:    Source code for use in this project.


## How to cite

~~~bibtext
@software{wassname2024{{ cookiecutter.project_name.lower().replace(' ', '_') }},
  author = {Clark, M.J.},
  title = { {{cookiecutter.project_name}} },
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  url = {https://github.com/wassname/{{ cookiecutter.project_name.lower().replace(' ', '_') }} },
  commit = {<commit hash>}
}
~~~


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
