import torch
print(torch.cuda.get_device_name())
print(torch.__version__, torch.cuda.is_available())
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)
for i in range(500):
    a = torch.randn(5)
    b = torch.randn(5)

    a = a.to(device)
    b = b.to(device)

    print(a + b)