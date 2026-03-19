class Solution(object):
    def carFleet(self, target, position, speed):
        cars = []
        
        for i in range(len(position)):
            time = (target - position[i]) / float(speed[i])
            cars.append((position[i], time))
        
        # sort by position descending
        cars.sort(reverse=True)
        
        fleets = 0
        prev_time = 0
        
        for pos, time in cars:
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets