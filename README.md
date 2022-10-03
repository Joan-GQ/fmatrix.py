# Flat Matrix

![](./assets/fmatrix.png)

# Example usage

```python
from fmatrix import *

r = random_matrix()

#  [[209, 111, 96, 9],
#  [224, 59, 99, 36],
#  [99, 118, 118, 191],
#  [194, 174, 32, 210]]

m = Matrix(r)

print(m.flat())
# [209, 111, 96, 9, 224, 59, 99, 36, 99, 118, 118, 191, 194, 174, 32, 210]

print(m.size) # 4

print(r[2][3]) # 91

print(m[2,3])  # 91
```
