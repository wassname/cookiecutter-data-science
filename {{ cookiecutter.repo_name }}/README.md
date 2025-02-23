# {{cookiecutter.project_name}}

{{cookiecutter.description}}


Project status: TODO

Project plan:

- [x] Init
- [ ] Fill out README
- [ ] ???
- [ ] Profit


## Install requirements

This project uses [uv](https://github.com/astral-sh/uv) for requirements.
~~~
uv sync
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
- nbs: Jupyter notebooks. Name with creator's initials, a number (for ordering), and short `-` delimited description, e.g.  `jqp-1.0-initial-data-exploration`.
- pyproject.toml:   defines poetry project dependencies and build configuration
- {{cookiecutter.project_name}}:    Source code for use in this project.


## If you used this work, please aknowledge it by citing this repository

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
