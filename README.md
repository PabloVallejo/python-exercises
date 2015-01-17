Simple Python exercises
================

[![Build Status](https://travis-ci.org/PabloVallejo/python-exercises.png?branch=master)](https://travis-ci.org/PabloVallejo/python-exercises)

Set of solutions for [46 Simple python exercises](https://github.com/PabloVallejo/python-exercises/blob/master/exercises-list.md), a list of exercises to introduce people to the
Python programming language.

This list of exercises comprises logical operators, loops, input and output, regular expressions and
more in order for people to have a basic overview of the language.

In order for better categorization, the exercises have been divided into 4 sections.

1. Very Simple Exercises
2. Higher Order Functions and List Comprehension
3. Simple exercises including Input and Output
4. Somewhat harder exercises

## Getting started
To execute a function from the set, just clone the repository or download the .zip containing all the files, then change directory into `python-exercises/sections`, open the python command line and import the module in
which the exercise you want to run is in and then call it.

```bash
$ git clone https://github.com/PabloVallejo/python-exercises.git
$ cd python-exercises/sections
$ python

Python 2.7 (r27:82525, Jul ......
>>> import module_1
>>> module_1.historygram( [ 1, 2, 3 ] )
   *
   **
   ***
```


## Running tests

There is also a test suite for this exercises, the purpose of it is first, so that users can refactor
things without breaking something, and second, for having a basic reference on how to test
functions and use the basic unittests methods.

```bash
$ cd python-exercises
$ python tests.py
.........................................
----------------------------------------------------------------------
Ran 41 tests in 0.218s

OK
```

## Contributing
Everyone is welcome to contribute. Feel free to submit a pull request, issue or suggestion you may find relevant.


## Reference
The original collection of exercises was created by Torbjörn Lager (torbjorn.lager@ling.gu.se)
and can be found [here](http://www.ling.gu.se/~lager/python_exercises.html).
