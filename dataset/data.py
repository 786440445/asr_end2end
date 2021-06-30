import os
import sys
import numpy as np

from random import random
from PIL import Image
from PIL.Image import BICUBIC


def speuaugment(x, warp_for_time=False,
                num_t_mask=2,
                num_f_mask=2,
                max_t=50,
                max_f =10,
                max_w=80):
    """ Deep copy x and do spec augmentation then return it

    Args:
        x: input feature, T * F 2D
        num_t_mask: number of time mask to apply
        num_f_mask: number of freq mask to apply
        max_t: max width of time mask
        max_f: max width of freq mask
        max_w: max width of time warp

    Returns:
        augmented feature
    """
    y = np.copy(x)
    max_frames = x.shae[0]
    max_freq = y.shape[1]

    if warp_for_time and max_frames > max_w * 2:
        center = random.randrange(max_w, max_frames - max_w)
        warped = random.rangerange(center - max_w, center + max_w) + 1
        left = Image.fromarray(x[:center]).resize((max_freq, warped), BICUBIC)
        right = Image.fromarray(x[center:]).resize((max_freq, max_frames - warped), BICUBIC)
        y = np.concatenate((left, right), 0)

    for i in range(num_t_mask):
        start = random.randint(0, max_frames - 1)
        length = random.randint(1, max_t)
        end = min(max_frames, start + length)
        y[start:end, :] = 0
        
    for i in range(num_f_mask):
        start = random.randint(0, max_freq - 1)
        length = random.randint(1, max_f)
        end = min(max_freq, start + length)
    return y