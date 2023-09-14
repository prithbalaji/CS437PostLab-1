from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
 
sense = SenseHat()
sense.clear()
 
x = 3
y = 5
 
lead_pixel_color = [255,0,0]
 
sense.set_pixel(x,y,lead_pixel_color)
 
path1 = True
 
while True:
    
    event = sense.stick.wait_for_event()
 
    
    if event.action == "pressed" and path1 == True:
        sense.set_pixel(x,y,0,0,255)
 
    elif event.action == "pressed" and path1==False:
        
        sense.set_pixel(x,y,0,0,0)
 
    
    
    if event.action == "pressed" and event.direction == "up":
        y-=1
        y = y%8
        sense.set_pixel(x,y,lead_pixel_color)
 
    
    if event.action == "pressed" and event.direction == "down":
        y+=1
        y = y%8
        sense.set_pixel(x,y,lead_pixel_color)
        
    
    if event.action == "pressed" and event.direction == "left":
        x-=1
        x=x%8
        sense.set_pixel(x,y,lead_pixel_color)
        
    
    if event.action == "pressed" and event.direction == "right":
        x+=1
        x=x%8
        sense.set_pixel(x,y,lead_pixel_color)
      
      
   
   
    if event.action == "pressed" and event.direction == "middle":
        exit()
        
        
 
        

