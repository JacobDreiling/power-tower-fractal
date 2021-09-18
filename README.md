# power-tower-fractal
A beautiful fractal I've never seen before

Everybody knows about the Mandelbrot set. Each point on the complex plane is denoted as c. Then you start with z = 0 and repeatedly replace z with z^2 + c. If the result remains bounded then you color the point c one color (usually black), otherwise color it something else.

But what if we took exponentials instead of squaring? Again, each point on the complex plane is denoted as c. Then you start with z = 0 and repeatedly replace z with c^z. If the result remains bounded then you color the point c one color (usually black), otherwise color it something else. These rules are what generate the fractal images in this repository.

In one of the images, the real and imaginary axes both range from -5 to 5. The other image shows the complex plane at some very specific coordinates I decided to zoom in on. Sadly, I forgot the exact values. The arguments for complex numbers were chosen to range from 0 to τ (i.e. 0° to 360°).
