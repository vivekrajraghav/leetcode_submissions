class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxlight=max(lights)
        maxlightidx=lights.index(maxlight)
        penalty=0
        for t in arrivalTime:
            r=t%period
            if r>=maxlight:
                penalty=max(penalty,period-r)
        return penalty