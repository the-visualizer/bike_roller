from p5 import *
class Elements:
    #int x, y, x1, x2, x3
    #p_image biker, road, sky, river
    def __init__(self):
      road  = load_image('Images/Boulevard.png')
      sky   = load_image('Images/Clouds.png')
      river = load_image('Images/River.png')

    def backdrop(dir):
      image(river, x3, 0)
      image(river, x3 + river.width, 0)
      image(river, x3 - river.width, 0)
      image(sky, x1, 0)
      image(sky, x1 + sky.width, 0)
      image(sky, x1 - sky.width, 0)
      image(road, x2, 0)
      image(road, x2 + road.width, 0)
      image(road, x2 - road.width, 0)

      x1 = x1 - dir*1
      x2 = x2 - dir*2
      x3 = x3 - dir*5   

      if dir==1: 
         if x1 < -sky.width:   x1 = 0
         if x2 < -road.width:  x2 = 0
         if x3 < -river.width: x3 = 0
      else:   
         if x1 > sky.width:   x1 = 0
         if x2 > road.width:  x2 = 0
         if x3 > river.width: x3 = 0
      print (x1, "\t", x2, "\t", x3, "\n")
    def biker (x, y, dir):
      if dir == 1: 
         biker = load_image('Images/Biker1.png')
      else:
         biker = load_image('Images/Biker2.png')
      image(biker, x/2, y/2)        
         

