# deep-learning-w-python
These are my personal notes and code snippets while reading Deep Learning with Python from Francois Chollet.
(see https://github.com/fchollet/deep-learning-with-python-notebooks)


## Mac Setup



## Ubuntu Setup

### Installation
Refer to https://www.tensorflow.org/install/pip to setup `miniconda` and `tensorflow`.


### Getting Started
Create environment from saved file

```shell
# Install miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Verify installation of NVIDIA GPU driver
nvidia-smi

# Configure system paths.
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/

# for convenience - configure automatically when conda environment is activated
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

# Install dependencies from yaml file
conda env create --file environment.yaml

# Activate env
conda activate valhalla

# Verify CPU setup
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# Verify GPU setup. Should output a list of GPU devices.
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"



