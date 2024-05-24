import sys
import os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, "..")
sys.path.append(parent_dir)
from common.np import np



# print(sys.path)

print(np.array([1,2,3]))