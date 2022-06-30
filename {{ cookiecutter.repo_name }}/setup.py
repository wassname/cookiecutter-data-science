from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    package_dir={'{{ cookiecutter.repo_name }}': 'src'},
    author='{{ cookiecutter.author_name }}',
    license='proprietary',
)
