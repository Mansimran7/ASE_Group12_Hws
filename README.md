# Automated Software Engineering (2023) Lua to Python
![DOI](https://zenodo.org/badge/589421644.svg)
![GitHub](https://img.shields.io/github/license/Mansimran7/ASE_Group12_Hws)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![GitHub language count](https://img.shields.io/github/languages/count/Mansimran7/ASE_Group12_Hws)
![Discord](https://img.shields.io/discord/1065117667415044118)
![GitHub forks](https://img.shields.io/github/forks/Mansimran7/ASE_Group12_Hws?style=social)
![GitHub issues](https://img.shields.io/github/issues/Mansimran7/ASE_Group12_Hws)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Mansimran7/ASE_Group12_Hws)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Mansimran7/ASE_Group12_Hws)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Mansimran7/ASE_Group12_Hws)
![GitHub contributors](https://img.shields.io/github/contributors/Mansimran7/ASE_Group12_Hws)
![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/Mansimran7/ASE_Group12_Hws/LUA2Python.yml?branch=main)

<img src="https://github.com/Mansimran7/ASE_Group12_Hws/blob/main/etc/img/luatopython_group12.gif" width="400" height="320"/>

## Table of Contents:
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [License](#license)
4. [Directory Structure](#directory-structure)
5. [Contributors](#contributors)

## Introduction
LUA is an ultra lightweight scripting language comprising less than two dozen keywords: and, break, do, else, elseif, end, false, for, function, if, in, local, nil, not, or, repeat, return, then, true, until, while.

LUA has a considerably smaller footprint than other programming languages (with its complete source code and documentation taking a mere 1.3 MB).

This repository contains the source code cnversion from lua to python scripting language.

## Getting Started
Check whether python is installed in your system. You can check that through:
```bash
python --version
```

Clone this repository using

```bash
git clone https://github.com/Mansimran7/ASE_Group12_Hws.git
```

Now you just need to run the following line inside /src folder to run all its test cases:
```bash
python main.py -g all
```
You can also choose a single test to test from ["num","sym","rand","the"] by the following command line:
```bash
python main.py -g [name-of-test-case]
```

## License
This project is licensed under [MIT](https://mit-license.org/).
Further details regarding the license can be found [here](https://github.com/Mansimran7/ASE_Group12_Hws/blob/main/LICENSE.md).

## Directory Structure
    C:.
    │   .gitignore
    │   CITATION.cff
    │   CODE_OF_CONDUCT.md
    │   CONTRIBUTING.md
    │   LICENSE.md
    │   README.md
    │   requirements.txt
    │
    ├───.github
    │   └───workflows
    │           LUA2Python.yml
    │
    ├───docs
    │       docs.md
    │
    ├───etc
    │   ├───data
    │   │       auto93.csv
    │   │
    │   ├───img
    │   │       Discord_server_proof.png
    │   │       luatopython_group12.gif
    │   │
    │   └───out
    │           cluster.out
    │           data.out
    │           script.out
    │
    ├───src
    │   ├───Hw1-script
    │   │   │   help.py
    │   │   │   main.py
    │   │   │   misc.py
    │   │   │   num_class.py
    │   │   │   sym_class.py
    │   │   │   utils.py
    │   │   │   __init__.py
    │   │
    │   ├───Hw2-data
    │   │   │   cols_class.py
    │   │   │   DATA_class.py
    │   │   │   help.py
    │   │   │   main.py
    │   │   │   misc.py
    │   │   │   num_class.py
    │   │   │   row_class.py
    │   │   │   sym_class.py
    │   │   │   utils.py
    │   │   │   __init__.py
    │ 
    │   ├───Hw3-cluster
    │   │   │   cols_class.py  
    │   │   │   DATA_class.py
    │   │   │   help.py
    │   │   │   main.py
    │   │   │   misc.py
    │   │   │   num_class.py
    │   │   │   row_class.py
    │   │   │   sym_class.py
    │   │   │   utils.py
    │   │   │   __init__.py
    │
    └───tests
        │   testEngine.py
        │   test_add.py
        │   __init__.py 

## Contributors
1. [Devanshi Savla](https://github.com/devanshi39)
2. [Indranil Banerjee](https://github.com/indranil1)
3. [Mansimran Singh Anand](https://github.com/Mansimran7)

To find out how you can contribute to this project, read the [CONTRIBUTING.md](https://github.com/Mansimran7/ASE_Group12_Hws/blob/main/CONTRIBUTING.md) file

The discord chat channel link is included in the file [CONTRIBUTING.md](https://github.com/Mansimran7/ASE_Group12_Hws/blob/main/CONTRIBUTING.md)
