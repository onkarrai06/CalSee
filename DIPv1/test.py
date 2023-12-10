import torch

print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name())
print(torch.cuda.device_count())

import torchvision

print(torchvision.__version__)
print(torchvision.version.cuda)