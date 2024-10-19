import pygame
import math

WINDOW_WIDTH = 800 #pygame window width in pixels
WINDOW_HEIGHT = 800 #pygame window height in pixels

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #pygame window
pygame.display.set_caption('Gravity Simulation') #window caption

body_id = 0 #used to keep track of id of body created

class Simulation:
    def __init__(self):
        bodies = []
        bodies.append(Body(2,0,0,0.95,50))
        bodies.append(Body(-10,0,0,-0.73,1))
        bodies.append(Body(50,0,0,-0.00001,1))

        self.bodies = bodies


        self.min_zoom = 1 #highest zoom in
        self.max_zoom = 100 #highest zoom out
        centre = [0, 0]
        for body in bodies:
            centre[0] += body.position[0]*body.mass
            centre[1] += body.position[1]*body.mass
        centre[0] /= len(bodies)
        centre[1] /= len(bodies)
        self.centre = centre #centre of mass
        
        self.background_colour = (0,0,0) #pygame window background colour
        self.body_colour = (100,100,100) #colour for drawing bodies
        self.step_size = 1 #simulation step size
        self.g = 1 #grav constant

    """
    runs the simulation for 1 timestep
    """
    def timestep(self):
        self.draw_bodies()
        self.move_bodies()
        

    def move_bodies(self):
        #updates speed of each body
        for body in self.bodies:
            for other in self.bodies:
                if body.id != other.id:

                    distance_x = body.position[0] - other.position[0]
                    distance_y = body.position[1] - other.position[1]
                    distance = math.sqrt(distance_x**2 + distance_y**2)
                    

                    acceleration = -self.g*other.mass/distance**2


                    component_x = distance_x/distance
                    component_y = distance_y/distance


                    acceleration_x = acceleration*component_x
                    acceleration_y = acceleration*component_y


                    body.velocity[0] += acceleration_x*self.step_size
                    body.velocity[1] += acceleration_y*self.step_size

        #moves bodies
        for choice in self.bodies:
            choice.position[0] += choice.velocity[0] * self.step_size
            choice.position[1] += choice.velocity[1] * self.step_size
        
    def draw_bodies(self): 
        self.centre = [0, 0]
        total_mass = 0

        # Calculate the center of mass
        for body in self.bodies:
            self.centre[0] += body.position[0] * body.mass
            self.centre[1] += body.position[1] * body.mass
            total_mass += body.mass

        # Avoid division by zero
        if total_mass > 0:
            self.centre[0] /= total_mass
            self.centre[1] /= total_mass
        else:
            # Default to the origin if no mass
            self.centre = [0, 0]

        # Get zoom factor
        dx, dy = 0, 0
        for body in self.bodies:
            dx = max(dx, abs(body.position[0] - self.centre[0]) + body.size/2)
            dy = max(dy, abs(body.position[1] - self.centre[1]) + body.size/2)

        distance_to_farthest = math.sqrt(dx**2 + dy**2)

        # Calculate the zoom factor
        if distance_to_farthest > 0:
            zoom_factor = (WINDOW_HEIGHT / 2) / distance_to_farthest
        else:
            zoom_factor = 1  # Default zoom if no distance

        zoom_factor /= 1.3  # Zoom out a bit

        # Clamp zoom factor to min and max
        zoom_factor = max(self.min_zoom, min(zoom_factor, self.max_zoom))

        # Clear the window
        window.fill(self.background_colour)

        # Draw the bodies
        for body in self.bodies:
            c_x = WINDOW_WIDTH / 2 + (body.position[0] - self.centre[0]) * zoom_factor
            c_y = WINDOW_HEIGHT / 2 + (body.position[1] - self.centre[1]) * zoom_factor
            pygame.draw.circle(window, self.body_colour, (int(c_x), int(c_y)), int(body.size * zoom_factor))

        pygame.display.update()


        
class Body:
    def __init__(self,posx,posy,velx,vely,mass):
        global body_id
        self.position = [posx,posy]
        self.velocity = [velx,vely]
        self.mass = mass
        self.size = self.mass**(1/3)
        self.id = body_id
        body_id += 1

    def __repr__(self):
        return("ID: "+str(self.id)+"\n"+"POS: "+str(self.position)+"\n"+"VEL: "+str(self.velocity)+"\n"+"MASS: "+ str(self.mass)+"\n")



clock = pygame.time.Clock()

simulation = Simulation()

while True:

    simulation.timestep() #update then draw

    clock.tick(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
