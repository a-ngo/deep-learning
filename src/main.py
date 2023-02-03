#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


def test_tensflow_installation():
    print(tf.config.list_physical_devices("GPU"))


def linear_classifier():
    num_samples_per_class = 1000
    negative_samples = np.random.multivariate_normal(
        mean=[0, 3], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class
    )
    positive_samples = np.random.multivariate_normal(
        mean=[3, 0], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class
    )

    inputs = np.vstack((negative_samples, positive_samples)).astype(np.float32)

    targets = np.vstack(
        (
            np.zeros((num_samples_per_class, 1), dtype="float32"),
            np.ones((num_samples_per_class, 1), dtype="float32"),
        )
    )

    plt.scatter(inputs[:, 0], inputs[:, 1], c=targets[:, 0])
    plt.show()


if __name__ == "__main__":
    test_tensflow_installation()

    linear_classifier()
