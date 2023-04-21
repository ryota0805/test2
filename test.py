import torch
x = torch.rand(5, 3)
print(x)
print(torch.__version__, torch.cuda.is_available())