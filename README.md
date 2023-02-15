# deep-learning-w-python
These are my personal notes and code snippets while reading Deep Learning with Python from Francois Chollet.
(see https://github.com/fchollet/deep-learning-with-python-notebooks)


## Mac Setup

### Install Miniconda
Install `miniconda` from https://docs.conda.io/en/latest/miniconda.html 

### Create Environment
```shell
conda deactivate

conda env create -f setup/tensorflow_mac_metal.yaml -n tensorflow
```

#### Test setup
``` shell
conda activate tensorflow

python3 setup/test_setup.py
```
