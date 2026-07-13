
from controller import Robot

def run_robot(robot):

    time_step = 32
    max_speed = 6.28
    left_motor = robot.getDevice('left wheel motor')
    
    left_motor.setPosition(float('inf'))
  
    left_motor.setVelocity(0.0)
   
    while robot.step(time_step) != -1 :
        
       
        
        left_motor.setVelocity(1.5) 
           
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
    