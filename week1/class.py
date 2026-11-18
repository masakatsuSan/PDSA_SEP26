class point:
    def __init__(self,a=0,b=0):
        self.x = a 
        self.y = b 
    
    def transition(self,deltaX,deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY
        
    def disCal(self):
        import math
        d = math.sqrt(self.x*self.x + self.y*self.y)
        return d 
    
    def __str__(self):
        return ('('+str(self.x)+"   "+str(self.y)+')')
    
    def __add__(self,p):
        return (point(self.x+p.x,self.y+p.y))
    
    def __sub__(self,p):
        return (point(self.x-p.x,self.y-p.y))
    
p = point(10,3)
q = point(6,5)
print(p-q)
