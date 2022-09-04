---
permalink: different-ways-of-installing-arduino-package
categories:
    - Engineering
tags:
    - embedded-system
    - arduino
    - microcontroller
---


Most python packages are designed to be compatible with the python-pip package manager. pip is the default CLI for managing python packages. All the popular packages can be installed using pip. But some old package does not support pip installation. In such a case, you have to install the package manually. Actually, the package installation also depends on which python package you are using for your project. In this blog, I will explain three ways of installing python package. 

## 1. Install package manually
The most common method for manually installing a package is using `setup.py` file provided by the package developer. [setup.py](http://setup.py) file normally resides inside the package folder. First, you need to navigate into the directory which contains the `setup.py` file. 
```
cd /package/setup.py
```
Then you can install the package using the following command.
```
python setup.py install
```
To install the package in python 2
```
python2 setup.py install
```

## 2. Install the package using pip
Almost all the packages provide the command for installing the package using pip. Here is the default command for installing a package using pip.
```
pip install package_name
```

## 3. Install the package using conda
If you use the Anaconda environment for you project, you can manage packages easily using `conda` CLI. To install `scikit-learn` in anaconda, you have to put the following command in conda CLI. 
```
conda install -c anaconda scikit-l
```

