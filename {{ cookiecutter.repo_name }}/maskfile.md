# Tasks

Tasks running for [mask](https://github.com/jacobdeichert/mask).


## freeze
> record pip and conda requirements

~~~sh
source activate {{ cookiecutter.repo_name }}
mkdir -p requirements
conda env export --no-builds --from-history > requirements/environment.min.yaml
conda env export > requirements/environment.max.yaml
python -m pip freeze > requirements/pip.conda.txt
cd requirements && conda-lock -f environment.max.yaml -p linux-64
~~~

## create_environment

~~~sh
set -x -e
export PROJECT_NAME={{ cookiecutter.repo_name }}
@echo ">>> Detected conda, creating conda environment."
conda env create --name $(PROJECT_NAME) python=3 -f ./requirements/environment.yaml
@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)"
~~~
