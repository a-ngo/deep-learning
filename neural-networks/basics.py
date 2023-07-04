#!/usr/bin/env python3

import torch
import numpy as np

# torch tensor
data = [[2,3], [6,7]]
data_tensor = torch.tensor(data)
print(data_tensor, type(data_tensor))

# numpy array
np_data = np.array(data)
print(np_data, type(np_data))


np_data_tensor = torch.from_numpy(np_data)
print(np_data_tensor, type(np_data_tensor))