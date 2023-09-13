# python-template-project
A template python project for open-sourcing your research project


## Dependency management

The easiest way to handle dependencies in python is creating and maintaining a requirements.txt.


```console
foo@bar:~$ pip install -r requirements.txt
```

## Notation and Coding Guideline

Python provides a short guide for notation: https://peps.python.org/pep-0008/

- Repository names: As concise as possible, should be descriptive. Lower case with hyphens `lowercase-title-with-hyphens`
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

### Overall recommendation:
- Functions' names should start with a verb.
- Avoid mathematical notations.
- Each method and class input and output should be typed.
- A function (or a class) should not take more than 5 arguments, otherwise use data classes instead.
- Write out input names `compute_solution(arg1=arg1, arg2=arg2)`
- Use f-strings for string formatting `f"Evaluation metric: {metric}"` (https://realpython.com/python-f-strings/)

## Comments and Documentation
> Without proper documentation your code is basically useless for other people and also for you (after some time).

- Always add a docstring documentation for each function. This can be later on used in Sphinx or other package documentation generator.
- Add meaningful documentation. Avoid unnecessary comments and instructions or boilerplate information.
- Add URLs or cititations if you use the code of others. Some licenses require that you copy the license into your code, if you use or modify the code of someone.

### Sphinx Documention Generator

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
Overall recommendations:
- Use list comprehension when it is possible.

## Unit Testing

## Collection of useful programming tools

## Managing your repo


## Containerization
Providing finished containers for installation could greatly help other people testing your module. I recommend two containerization solutions: 
- Singularity https://docs.sylabs.io/guides/latest/user-guide/
- Docker https://docs.docker.com/get-started/

Example files are provided in this template project later on.

## Acknowledgements

## Citing and Referencing
