def knows(a: int, b: int) -> bool:
    graph = [
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]

    return graph[a][b] == 1


class Solution:
    def findCelebrity(self, n: int) -> int:
        possible_celebrityies = [True] * n

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if knows(i, j) or not knows(j, i):
                    possible_celebrityies[i] = False

                    break

            if possible_celebrityies[i]:
                return i

        return -1
