# Intro

This is a small starting repository for python project in Data Science context. The project contains gitignore file with initial ignore filters such as `__pycache__`. It also included functionality to store settings related to the project. That makes keeping settings nice and clean in one place. For now it works for Linux systems.

The aim of this project is to reduce amount of time to initialize Data Science project repository. Every repository need the same setting that is why generalized template is appropriate. This project is this kind of template.

The goal of this project is provide you the tool to quickly init the project in environment. You are free to make any project structure you like. The only rule is having directory in the root directory (anyways is due to PEP8). Though if you like to have something additionally please feel free to put the issue or fork this repository and add specifics you would like to have.

After making all steps you will have initial repository ready for your task. `init.py` will append `PYTHONPATH` with full path to your repository such that you will be able to import modules together with system ones. That will also help avoiding anti-pattern with `import ..module.func as func`.

Together with that your repository will have settings file and project variables out of the box.

`sets.yaml` is a settings file which is being ignored by git and can be used for defining path to data and other important configurations. From python code you can access content of this setting file as a dictionary by following import: `from  mrcnn.variable import user_settings` (assuming you did all the steps described below).

# Set up
1. Download this repository as a zip archive. When you unzip it, it will be your project repository directory. Let's say you implement Mask-RCNN. Let's call this directory `repo`.
2. Rename `dummy_project` (inside `repo` directory) to your project name. For instance `mrcnn`. Read Note 1.
3. Rename gitignore to .gitignore
4. Run `python init.py`. See Note 2.
5. Install packages inside requirements.txt

After all steps are done The following files can be changed or removed if needed:
* README.md
* LICENCE.txt

`init.py` is something what other participant into the project will use so that should be kept.

**Note 1**: Good example why to do so is Mask-RCNN implementation by [Matterport, Inc
](https://github.com/matterport): https://github.com/matterport/Mask_RCNN. It is possible that your repository name an directory name will duplicate. It will make sense when you initialize `PYTHONPATH`. Then when you do import it will be just `import mrcnn`. Keep in mind that name you choose will be used in python import commands. So follow the modules naming convention.

**Note 2**: init.py will append environmental variables inside your operation system. In case of Linux system you need to restart you terminal or refresh environment by running `source ~/.bashr`. Jupyter lab should be restarted after refreshing as well such that to get access to updated environment variables.

# TODO

* Pass project name into `init.py` - to rename `dummy_project`
* Generate `test.py` by `init.py`
* Add Windows support.