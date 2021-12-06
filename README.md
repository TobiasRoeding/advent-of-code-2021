# Advent of Code 2021
Python solutions for the advent of code 2021

## Install all dependencies for development
```
pipenv install --dev
```

## Setup pre-commit and pre-push hooks
```
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## run pre-commit hook manually
```
pipenv run pre-commit run --all-files
```
