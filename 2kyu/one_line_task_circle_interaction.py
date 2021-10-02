from numpy import*;circleIntersection=lambda a,b,r:(lambda c:int(max(0,r*r*(c-sin(c)))))(arccos(hypot(*array(a)-b)/2/r)*2)
