class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        near_x=max(x1,min(xCenter,x2))
        near_y=max(y1,min(yCenter,y2))
        dx=xCenter-near_x
        dy=yCenter-near_y
        return (dx*dx+dy*dy)<=radius*radius
        