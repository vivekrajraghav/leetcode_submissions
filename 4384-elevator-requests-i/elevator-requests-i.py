class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total = 0
        prev = 0
        for req in requests:
            total += abs(req - prev)
            prev = req
        return total