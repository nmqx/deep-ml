import torch

def matrixmul(a, b) -> torch.Tensor:
    """
    Multiply two matrices using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2D tensor of shape (m, n) or a scalar tensor -1 if dimensions mismatch.
    
    """
    if not isinstance(a,torch.Tensor):
        a = Torch.as_tensor(a)
    if not isinstance(b,torch.Tensor):
        b = Torch.as_tensor(b)
    if a.ndim != 2 or b.ndim !=2:
        return torch.tensor(-1)

    if a.shape[1] != b.shape[0]:
        return torch.tensor(-1)
    return a @ b
    return val
