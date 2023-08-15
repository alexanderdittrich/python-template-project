# python-template-project
A template python project for open-sourcing your research project


## Install Requirements

```console
foo@bar:~$ pip install -r requirements.txt
```

## Notation and Coding Guideline

Python provides a short guide for notation: https://peps.python.org/pep-0008/

- Repository names: As concise as possible, should be descriptive. Lower case with hyphens `lowercase-title-with-hyphens`.
- Types like classes, structs: 

```python
class FirstUpperCamelCase
```

- Function, methods: 
```python 
def lower_case_with_underscores()
```

- Internal function names: 

```python  
def _lower_case_with_underscores()
```

- Constants: 
```python 
UPPER_CASE_WITH_UNDERSCORES
```
- Variables: 
```python 
lower_case_with_underscores
```

## Sphinx Documentation Generator


## Using module outside the repository

For installing your Python code in your current python environment, run:
```console
foo@bar:~$ cd /PATH/TO/YOUR/PROJECT/
foo@bar:~$ pip install -e . 
```
-e stands for editable which tracks changes you make to your code.

If your module is feature-complete and sufficiently tested. You can now use:
```console
foo@bar:~$ cd /PATH/TO/YOUR/PROJECT/
foo@bar:~$ pip install . 
```

To officially open-source your code and after editing the necessary setup files, you can upload it to
https://pypi.org/. Congrats! 

## Code Optimization


## Unit Testing

## Acknowledgements


## Citing and Referencing


## Collection of useful programming tools