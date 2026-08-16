class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        min_idx=-1
        min_distance=float('inf')
        tx,ty=target
        for i,(dx,dy,max_range) in enumerate(drones):
            curr_distance=abs(dx-tx)+abs(dy-ty)
            if curr_distance<=max_range and curr_distance<min_distance:
                min_idx=i
                min_distance=curr_distance
                if min_distance==0:
                    return min_idx
        return min_idx