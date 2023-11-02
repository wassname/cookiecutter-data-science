# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

    ├── Justfile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── 30_processed      <- The final, canonical data sets for modeling.
    │   ├── 20_interim        <- Intermediate data that has been transformed.
    │   └── 10_raw            <- The original, immutable data dump.
    │
    │
    ├── notebooks          <- Jupyter notebooks. Namiwith creator's initials, a number (for ordering), and short `-` delimited description, e.g.
    │                         `jqp-1.0-initial-data-exploration`.
    │
    ├── pyproject.toml    <- defines project dependencies and build configuration
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
           └── visualize.py


## Install requirements
```
poetry install
```

## How to get data

TODO document how to get the data

## How to run

TODO document how to run the code

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
