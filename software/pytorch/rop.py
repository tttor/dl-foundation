#!/usr/bin/env python3
# https://discuss.pytorch.org/t/adding-functionality-hessian-and-fisher-information-vector-products/23295
import numpy as np
import torch

def main():
    W = torch.tensor([[1., 1.], [1., 1.]], requires_grad=True)
    V = torch.tensor([[2., 2.], [2., 2.]])
    x = torch.tensor([0., 1.])
    y = W.mv(x)

    print(y.shape)
    print(W.shape)
    print(V.shape)

    JV = Rop(y, W, V)
    print(JV)

def Rop(ys, xs, vs):
    if isinstance(ys, tuple):
        ws = [torch.tensor(torch.zeros_like(y), requires_grad=True) for y in ys]
    else:
        ws = torch.tensor(torch.zeros_like(ys), requires_grad=True)

    gs = torch.autograd.grad(ys, xs, grad_outputs=ws, create_graph=True, retain_graph=True, allow_unused=True)
    print('gs=', gs)
    re = torch.autograd.grad(gs, ws, grad_outputs=vs, create_graph=True, retain_graph=True, allow_unused=True)
    return tuple([j.detach() for j in re])


# def Lop(ys, xs, ws):
#     vJ = torch.autograd.grad(ys, xs, grad_outputs=ws, create_graph=True, retain_graph=True, allow_unused=True)
#     return tuple([j.detach() for j in vJ])


# def HesssianVectorProduct(f, x, v):
#     df_dx = torch.autograd.grad(f, x, create_graph=True, retain_graph=True)
#     Hv = Rop(df_dx, x, v)
#     return tuple([j.detach() for j in Hv])


# def FisherVectorProduct(loss, output, model, vp):

#     Jv = Rop(output, list(model.parameters()), vp)
#     batch, dims = output.size(0), output.size(1)
#     if loss.grad_fn.__class__.__name__ == 'NllLossBackward':
#         outputsoftmax = torch.nn.functional.softmax(output, dim=1)
#         M = torch.zeros(batch, dims, dims).cuda() if outputsoftmax.is_cuda else torch.zeros(batch, dims, dims)
#         M.reshape(batch, -1)[:, ::dims + 1] = outputsoftmax
#         H = M - torch.einsum('bi,bj->bij', (outputsoftmax, outputsoftmax))
#         HJv = [torch.squeeze(H @ torch.unsqueeze(Jv[0],
#                                                  -1)) / batch]
#     else:
#         HJv = HesssianVectorProduct(loss, output, Jv)
#     JHJv = Lop(output, list(model.parameters()), HJv)


#     return torch.cat([torch.flatten(v) for v in JHJv])

if __name__ == '__main__':
    main()

# def _check_param_device(param, old_param_device):
#     r"""This helper function is to check if the parameters are located
#     in the same device. Currently, the conversion between model parameters
#     and single vector form is not supported for multiple allocations,
#     e.g. parameters in different GPUs, or mixture of CPU/GPU.

#     Arguments:
#         param ([Tensor]): a Tensor of a parameter of a model
#         old_param_device (int): the device where the first parameter of a
#                                 model is allocated.

#     Returns:
#         old_param_device (int): report device for the first time
#     """

#     # Meet the first parameter
#     if old_param_device is None:
#         old_param_device = param.get_device() if param.is_cuda else -1
#     else:
#         warn = False
#         if param.is_cuda:  # Check if in same GPU
#             warn = (param.get_device() != old_param_device)
#         else:  # Check if in CPU
#             warn = (old_param_device != -1)
#         if warn:
#             raise TypeError('Found two parameters on different devices, '
#                             'this is currently not supported.')
#     return old_param_device


# def vector_to_parameter_list(vec, parameters):
#     r"""Convert one vector to the parameter list

#     Arguments:
#         vec (Tensor): a single vector represents the parameters of a model.
#         parameters (Iterable[Tensor]): an iterator of Tensors that are the
#             parameters of a model.
#     """
#     # Ensure vec of type Tensor
#     if not isinstance(vec, torch.Tensor):
#         raise TypeError('expected torch.Tensor, but got: {}'
#                         .format(torch.typename(vec)))
#     # Flag for the device where the parameter is located
#     param_device = None
#     params_new = []
#     # Pointer for slicing the vector for each parameter
#     pointer = 0
#     for param in parameters:
#         # Ensure the parameters are located in the same device
#         param_device = _check_param_device(param, param_device)

#         # The length of the parameter
#         num_param = param.numel()
#         # Slice the vector, reshape it, and replace the old data of the parameter
#         param_new = vec[pointer:pointer + num_param].view_as(param).data
#         params_new.append(param_new)
#         # Increment the pointer
#         pointer += num_param

#     return list(params_new)
