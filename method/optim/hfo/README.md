# HFO: Hessian-free optimization
* aka "Hessian-free" because 
  * we never construct the Hessian matrix explicitly, 
  * we directly compute the Hessian-matrix vector product, where the vector here is the search direction vector.
  * for the Hessian matrix, $\nabla^2 f(x)$, then the Hessian matrix-vector product is given by
    $\big(\nabla^2 f(x) \big) \cdot v = \nabla_x \big( \nabla_x f(x) \cdot v \big)$
* aka "truncated Newton method" because
  * we truncate the linear CG iteration for some `max_cg_iter`
  * the inner linear CG loop solves the linear equation $\nabla^2 f(x) p = \nabla f(x)$,
    which is equivalent to solving a minization of local quadratic approximation of $f(x)$
  
# Gauss-Newton matric vector product
* Efficient Calculation of the Gauss-Newton Approximation of the Hessian Matrix in Neural Networks, Michael Fairbank, 2012
* Fast Curvature Matrix-Vector Products for Second-Order Gradient Descent, Nicol N. Schraudolph, 2002

# Misc
* http://andrew.gibiansky.com/blog/machine-learning/gauss-newton-matrix/
* http://andrew.gibiansky.com/blog/machine-learning/hessian-free-optimization/
* https://justindomke.wordpress.com/2009/01/17/hessian-vector-products/
* https://studywolf.wordpress.com/2016/04/04/deep-learning-for-control-using-augmented-hessian-free-optimization/
  * https://github.com/studywolf/blog/blob/master/train_AHF/train_hf.py