from cython.parallel import parallel, prange
import numpy as np
cimport numpy as np

def vector_by_scalar(np.ndarray[np.float64_t, ndim=1] vec, double scalar):
    cdef int i
    cdef int n = vec.shape[0]
    
    with nogil:
         with parallel():
            for i in prange(n, schedule='dynamic'):
                vec[i] *= scalar
    return vec

