from setuptools import find_packages, setup

setup(
    name='{{ repo_name }}',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    package_dir={'': 'src'},
    author='{{ cookiecutter.author_name }}',
    license='proprietary',
)
