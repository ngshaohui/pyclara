# Pip and virtual environments

## `pip` package manager

https://packaging.python.org/en/latest/tutorials/installing-packages/

The `pip` package manager is a tool that can be used to manage and keep track of external packages we need in our project.

## Installing packages

In order to obtain external packages, we can use the `install` command to obtain it.

```bash
pip install <PACKAGE_NAME>
```

We can use the `list` command to list down what are all the installed packages on `pip`.

```bash
(venv) ngshaohui@shaohui-mbp-202 dgd-callback-server % pip list
Package            Version
------------------ ---------
APScheduler        3.7.0
astroid            2.6.6
attrs              21.2.0
autopep8           1.5.7
certifi            2021.5.30
charset-normalizer 2.0.4
click              8.0.1
...
```

### Uninstalling

Uninstalling is the opposite of installing, with the `uninstall` command.

```bash
pip uninstall <PACKAGE_NAME>
```

### `requirements.txt`

If we want to work on the project on a different machine, we will need the same packages to be installed on that machine as well.

While we can create the list of dependency packages by using the `freeze` command and writing the output to a file.

```bash
pip freeze > requirements.txt
```

This will generate a list of dependency packages, as well as their specific version numbers.

The `requirements.txt` file is to be located in the project's root directory, and is one of the ways we can identify repositories as Python projects.

#### Installing dependencies from `requirements.txt`

When a `requirements.txt` file is included, we will be able to install the pages listed within with the `install` command.

This is required to set up the development environment, as we might not have all the required packages to run our project.

Since the file contains a list of packages, we will need to include the `-r` flag to install multiple packages recursively.

```bash
pip install -r requirements.txt
```

### Upgrading packages

If we wish to upgrade a package to its latest version, we need to utilise the `upgrade` command.

```bash
pip install --upgrade <PACKAGE_NAME>
```

This will install the latest possible version of a package, if any are available.

#### Specific package versions

If we require a specific version of a package, we can use the install command and specify a version number to install.

```bash
pip install <PACKAGE_NAME>==<VERSION_NUMBER>
```

### Uninstalling all packages

To start over from a clean slate, we can uninstall all the packages we installed with `pip`.

```bash
pip freeze | xargs pip uninstall -y
```

This works by listing out all the installed packages with `freeze`, then piping its output to `pip uninstall`.

### Source

By default, `pip` obtains the packages [from the PyPI repository](https://pypi.org/).

Other possible sources include:

1. Alternative indexes (universities often host repository mirrors)
2. Private indexes (companies might publish internal libraries)
3. Wheel files

Using the default PyPI repository will suffice for most people, so we do not need to worry about alternate sources at this juncture.

### Alternatives to `pip`

There are other Python distributions out there that come with their own package managers.

For example, Anaconda is one of the distributions that is geared towards scientific computing, data science, and machine learning.

It [comes with the Conda package manager](https://www.anaconda.com/blog/understanding-conda-and-pip), which handles the installation differently from `pip`.

However, this also means that some packages may be available on one but not the other.

## Virtual environments

https://docs.python.org/3/library/venv.html

By default, `pip` installs all the packages globally.

This could potentially cause compatibility issues, if we have 2 projects that require different versions of the same package.

We can overcome this issue by setting up a virtual environment, which keeps our python packages installed relative to that project only.

### Initialising your virtual environment

```bash
python3 -m venv <VIRTUAL_ENVIRONMENT_NAME>
```

This initialises the virtual environment, creating all the relevant files needed to launch our virtual environment.

#### Naming your virtual env

A common way is to name your virtual environment `venv`.

```bash
python3 -m venv venv
```

### Activating the virtual environment

After creating the virtual environment files, we will need to activate it with the activation script that has been created.

On macOS, this will be located at `venv/bin/activate`.

```python
sh@mbp poems % source venv/bin/activate
(venv) sh@mbp poems %
```

This activates the virtual environment for the current shell.

One indicator that the virtual environment has been activated is the `(venv)` on the left of the terminal prompt, where `venv` corresponds to the virtual environment name.

When we run `pip list`, we will notice that only 2 packages will be included.

```bash
(venv) sh@mbp poems % pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 67.6.1
```

These are the only 2 required minimally for Python to install other packages.

All remaining packages that were installed globally will be unavailable within the virtual environment unless you install them manually.

#### Windows

On Windows, this can be done by running:

```powershell
venv\Scripts\activate.bat
```

Do note that it is possible to run it with `venv\Scripts\activate`, ommitting the `.bat` extension.

### Deactivating the virtual environment

We can deactivate it by using the `deactivate` command.

```python
(venv) sh@mbp poems % deactivate
sh@mbp poems %
```

Conversely, we know the virtual environment has been deactivated as the `(venv)` will disappear from future terminal prompts.

If we examine the activation script, we will see that the `deactivate` command has been added by it, allowing us to restore the shell to its previous state.

```bash
sh@mbp poems % cat venv/bin/activate     
# This file must be used with "source bin/activate" *from bash*
# you cannot run it directly

deactivate () {
    # reset old environment variables
    if [ -n "${_OLD_VIRTUAL_PATH:-}" ] ; then
        PATH="${_OLD_VIRTUAL_PATH:-}"
        export PATH
        unset _OLD_VIRTUAL_PATH
...
```

### VSCode

When a virtual environment is initialised, VSCode will detect it and ask if you wish to use it in your current workspace.

(TODO screenshots in slides)

When running the python scripts with VSCode, it will automatically run it from within your virtual environment.

## Further reading

- Installing from alternative indexes
- Installing from wheel files
