class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)

        parent = list(range(n))
        size = [1] * n

        provinces = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # Path Compression
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False

            # Union by Size
            if size[px] < size[py]:
                parent[px] = py
                size[py] += size[px]
            else:
                parent[py] = px
                size[px] += size[py]

            return True

        # Visit only the upper triangle of the matrix
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    if union(i, j):
                        provinces -= 1

        return provinces