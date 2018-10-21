# import ... (as ...)
import sys

print(sys.platform)
print(sys.maxsize)
#print(sys.path)

print("")

sys.path.append("modules") # Add searching module path
import geometry as g
print(g.distance(1,4,1,5))