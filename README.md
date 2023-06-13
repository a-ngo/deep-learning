# Deep Learning
These are my personal notes and code snippets while doing the udacity course - deep learning (PyTorch) and reading "Deep Learning with Python" from Francois Chollet (Tensorflow/Keras - see also https://github.com/fchollet/deep-learning-with-python-notebooks).

The following topics are covered:
- deep learning from first principles
- image classification and image segmentation
- time series forecasting
- text classification and machine translation
- text generation, neural style transfer, and image generation

## Setup
This setup is based on:
pytorch:
- [dev apple: Accelerated PyTorch training on Mac-Metal](https://developer.apple.com/metal/pytorch/)
- [Start Locally | PyTorch](https://pytorch.org/get-started/locally/)

tensorflow:
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

# create torch environment from file
conda env create -f setup/torch_mac_metal.yaml -n torch

# alternative: create tensorflow environment from file
conda env create -f setup/tensorflow_mac_metal.yaml -n tensorflow
```

#### 3. Verify
Run respective test script to verify correct installation.

pytorch:
``` shell
conda activate torch

python3 setup/test_torch_setup.py
```

tensorflow:
``` shell
conda activate tensorflow

python3 setup/test_tensorflow_setup.py
```

#### 4. Personal configruation
Don't automatically activate base.
``` shell
conda config --set auto_activate_base false
```
