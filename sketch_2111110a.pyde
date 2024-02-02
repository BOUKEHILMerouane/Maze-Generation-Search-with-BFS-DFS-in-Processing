from random import randrange

global gg
gg = 0
class Pix() : 
    def __init__(self, x, y):
       self.x=x
       self.y=y
    def eq(self, other) : 
      if (self.x == other.x and self.y == other.y) :
        return True

    
visited = [] 
queue = [] 
neighbors = [[Pix(-1,-1) for x in range(8)] for y in range(108)]
Bx = int(randrange(10))
By = int(randrange(7))
while 1 :
   Ex = int(randrange(10))
   if (Ex!=Bx) :
       break
while 1 :
   Ey = int(randrange(7))
   if (Ey!=By) :
       break

while 1 :
   rx = int(randrange(10))
   if (rx!=Bx and rx!=Ex) :
       break
while 1 :
   ry = int(randrange(7))
   if (ry!=By and ry!=Ey) :
       break
while 1 :
   bx = int(randrange(10))
   if (bx!=Bx and bx!=Ex and bx!=rx) :
       break
while 1 :
   by = int(randrange(7))
   if (by!=By and by!=Ey and by!=ry) :
       break
while 1 :
   gx = int(randrange(10))
   if (gx!=Bx and gx!=Ex and gx!=rx and gx!=bx) :
       break
while 1 :
   gy = int(randrange(7))
   if (gy!=By and gy!=Ey and gy!=ry and gy!=by) :
       break

def addNeighbors(i) :
    x = int(i/10)
    y = i%10
    if (x!=rx or y!=ry) and (x!=bx or y!=by) and (x!=gx or y!=gy):
        neighbors[i][0] = Pix(x+1,y)
        neighbors[i][1] = Pix(x,y+1)
        neighbors[i][2] = Pix(x+1,y+1)
        neighbors[i][3] = Pix(x-1,y)
        neighbors[i][4] = Pix(x,y-1)
        neighbors[i][5] = Pix(x-1,y-1)
        neighbors[i][6] = Pix(x+1,y-1)
        neighbors[i][7] = Pix(x-1,y+1)

def checkNeighbors(i) :
    for j in range(8) :
        if neighbors[i][j].x < 0 or neighbors[i][j].y < 0 or neighbors[i][j].y > 7 or neighbors[i][j].x > 10 :
           neighbors[i][j] = Pix(-1,-1)
    
    for j in range(8) :
        for visite in visited :
            if neighbors[i][j].eq(visite) : 
                neighbors[i][j] = Pix(-1,-1)
    
def Move(p) :
    index  = p.x*10 + p.y
    if not Pix(p.x,p.y).eq(Pix(rx,ry)) and not Pix(p.x,p.y).eq(Pix(bx,by)) and not Pix(p.x,p.y).eq(Pix(gx,gy)) :
       visited.append(p)
       for i in range(8) :
           if not neighbors[index][i].eq(Pix(-1,-1)):
              queue.append(neighbors[index][i])
    for queu in queue :
        for visite in visited :
            if (queu.eq(visite)) :
                queue.remove(queu)

def found(p) :
    if queue[0].eq(p) :
       return 0
    return 1

for i in range(len(neighbors)) : 
    addNeighbors(i)
    checkNeighbors(i)


Move(Pix(Bx,By))
f = found(Pix(Ex,Ey))
while f :
   Move(queue.pop(0))
   f = found(Pix(Ex,Ey))
visited.pop(0)
def setup():
 size(300,230)
 background(98,141,49)
 for i in range(11) :
   for j in range(8):
     fill(158,168,129)
     ellipse(25 + i*25, 25+j*25,20,15)

def draw() : 
        fill(0,0,0)
        ellipse(25 + Bx*25, 25+By*25,20,15)
        fill(0,255,0)
        ellipse(25 + gx*25, 25+gy*25,20,15)
        fill(0,0,255)
        ellipse(25 + bx*25, 25+by*25,20,15)
        fill(255,0,0)
        ellipse(25 + rx*25, 25+ry*25,20,15)
        fill(255,255,255)
        ellipse(25 + Ex*25, 25+Ey*25,20,15)
        global gg
        fill(150,183,43)
        ellipse(25 + visited[gg].x*25, 25+visited[gg].y*25,20,15)
        if gg<len(visited)-1 :
           gg = gg + 1
           delay(300)
