import numpy as np
import matplotlib.pyplot as plt

n = 50000

points = np.random.uniform(0, 1, (2, n))

# idices of all points with distance < 1 from origin
idx = np.linalg.norm(points, axis=0) < 1
n_points_in_circle = np.sum(idx)
# print(idx)
print(n_points_in_circle)

# A_quartercircle = pi / 4
# A_square = 1

# A_quartercircle
# --------------- * 4  = pi
# A_square

print("Pi ist ungefähr {}".format(n_points_in_circle * 4 /n))

plt.scatter(points[0, idx], points[1, idx])
plt.scatter(points[0, idx==False], points[1, idx==False], c='r')
plt.show()
