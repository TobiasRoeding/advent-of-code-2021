[![build](https://github.com/TobiasRoeding/advent-of-code-2021/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/TobiasRoeding/advent-of-code-2021/actions/workflows/build.yml)

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

## run the solution for a single day
```
pipenv run python -m src.day1
```

## run pre-commit hook manually
```
pipenv run pre-commit run --all-files
```
