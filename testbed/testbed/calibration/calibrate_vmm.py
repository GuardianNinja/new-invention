import numpy as np
from numpy.linalg import pinv

def design_cal_vectors(rows, cols):
    # Use Hadamard-like or identity basis for calibration
    N = max(rows, cols)
    I = np.eye(N)
    return I[:cols,:rows]

def compute_correction_matrix(raw_outputs, expected_outputs):
    """
    Fit linear correction matrix C such that expected = C @ raw.
    raw_outputs: (m, n) measured outputs for m calibration vectors
    expected_outputs: (m, n) ideal outputs
    Returns C (n x n)
    """
    # Solve least squares: expected = raw @ C^T  => C^T = pinv(raw) @ expected
    C_T = pinv(raw_outputs) @ expected_outputs
    C = C_T.T
    return C

def quantize_matrix(C, scale=2**12):
    # Fixed-point quantization for FPGA runtime
    Cq = np.round(C * scale).astype(np.int32)
    return Cq, scale
