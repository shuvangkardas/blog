---
categories:
    - Engineering
tags:
    - python
---

The `conda` is the command-line interface tool for managing installations of various packages in Anaconda. Of course, Anaconda has GUI to manage everything. Yet, GUI does not provide all the functionalities and automation facilities. 
## `conda` basic commands
-   `conda clean --all` It clean tarballs garbage create by environments and clean disk space
-   `conda update <package_name>` update a package inside environment
-   `conda list` list packages inside the environment
-   `conda install -n <env_name> pandas` Install package into an environment from default shell
-   `pip install <package_name>` Install a package from python repo in the current environment.
-   `conda install pandas=0.24.1` install package inside an environment
## `conda` Environment commands
-   `conda env list` list the available environments
-   `conda create --name <env_name> python` Create `conda` environment
-   `conda create -n <env_name> python=3.7` Create a environment based on Python 3.7
-   `conda activate <env_name>` Activate the environment
-   `conda deactivate` Deactivate the current environment


To reproduce the project including environment, `conda` has environment files. `conda` calls it environment files.
-   `conda env export --file environment.yml` export the current environment to the current working directory
-   `conda env create -n <env_name> environment.yml` recreate an environment from the environment file form current directory

**Note 1:** If a package is not available on Anaconda Repository it can be installed from the python default repository using pip. It is also mentioned that pip does not possess all the features of `conda` packages.

**Note 2:** It is recommended to install all the packages we want to include in an environment at the time of environment creation. It helps avoid dependency conflicts.

## Add `conda` environment to jupyter notebook
1.  `conda create --name myEnv`
2.  `conda activate myEnv`
3.  `conda install -c anaconda ipykernel`
4.  `python -m ipykernel install --user --name=myEnv`

---
Shuvangkar Das, Potsdam, New York
