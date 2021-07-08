import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import random
import sys
import pytest
import math

"""A simple test for confirming the square root of a number"""
def test_sqrt():
    num = 16
    assert math.sqrt(num) == 4
