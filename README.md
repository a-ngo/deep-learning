# deep-learning-w-python
These are my personal notes and code snippets while reading Deep Learning with Python from Francois Chollet.
(see https://github.com/fchollet/deep-learning-with-python-notebooks)


## Setup
This setup is based on:
 - [dev apple: get started with tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/)
 - [jeff heaton course](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-mac-metal-jan-2023.ipynb)

### Requirements
- Mac computers with Apple silicon or AMD GPUs
- macOS 12.0 or later (Get the latest beta)
- Python 3.8 or later
- Xcode command-line tools: `xcode-select --install`

### Get started

#### 1. Install miniconda
Install `miniconda` from https://docs.conda.io/en/latest/miniconda.html 

#### 2. Create environment

```shell
conda deactivate

# create environment from file
conda env create -f setup/tensorflow_mac_metal.yaml -n tensorflow
```

#### 3. Verify
Run test script to verify correct installation.
``` shell
conda activate tensorflow

python3 setup/test_setup.py
```

#### 4. Personal configruation
Don't automatically activate base.
``` shell
conda config --set auto_activate_base false
```
