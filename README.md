# GravitySimulation

I've always been passionate about simulations and space, and in 2022 I thought that it would be fun to join them together into a simple simulation of a solar system.
<br><br>
![image](https://github.com/user-attachments/assets/efbe8b31-c6b3-4155-9dd1-f0e06dcdf2d2)<br><br>
![image](https://github.com/user-attachments/assets/7709dfcb-de3d-45e4-b7b2-d06cb7e18c0b)<br><br>
![image](https://github.com/user-attachments/assets/f48f06d5-9842-4575-a1f3-bc459599ba71)<br><br>


## How It Works

bodies are initialized by their position in 2D space, their initial velocity in 2D space, and their mass. Radius is computed based on mass to be proportional to the cube root. I chose the cube root and not the square root because I want the simulation to represent 3D objects taken from a 2D reference frame. This makes it more realistic. <br>
Another reason for this change is because I want the gravitational field to fall off proportional to r^2. In a 2D universe, gravity would weaken according to 1/x, and this includes a host of issues to orbital realism. Orbits in 2D precess much faster than ones in 3D, and escape velocity is always infinite (assuming infinite speed of light).

## Creation Process

While I'm familiar with the Agile design philosophy, I wanted to have a concrete plan when creating this project. I started off with making the pygame window draw circles at a location.<br>

Afterwards, I created the Body class and worked on displaying the bodies.<br>

The final step was the simulation part. I created one function to update velocities of the bodies, and another one to move and draw them.<br>

One unplanned aspect I added later was the camera focusing on the system's centre of mass. The system kept slowly drifting off, so I added a shift to the display that would re-centre it.
Another unplanned thing I added later was the variable camera zoom. I didn't like how sometimes the camera would lose a body if it went too far, or how it would be too far zoomed out to see anything clearly. Now it takes the farthest body and zooms to fit it in the window.


# Next Steps

I plan on next making the simulation 3D, and have bodies able to collide and merge. Maybe I can add bodies breaking apart if hit too hard, in reference to how the Moon was formed.
