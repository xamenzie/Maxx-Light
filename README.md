# Maxx Utilities

A "go to" light to use in almost every situation. Meant to be used as an assets.

Overall Features

- Strenght : Adjust the intensity of the light
- Gradient intensity : Adjust the gradient of the light, 0 = no gradient at all, this parameter work in combination with the strenght to get the perfect gradient/intensity match
- Width/Height : Adjust the scale and the aspect ratio, better than scaling manually cause it keep the perfect border radius
- Rounded radius : Adjust the size of the rounded radius, 0 = perfect rectangular, 1 = perfect spherical
- Gradient Shift : Offset the gradient position to create intersting reflection on glossy surface for exemple
- Obj to follow : Select an object which the light will follow, no object = feature disable
- Color : Change the color of the light
- View camera : The light show as wireframe in the viewport, we can see the gradient in render preview mode or hide it when checking this box, in every case the source light will be hided in the final render
- Only one side : Switch between only one side that emit light and the two side
- Spread Angle : Adjust the angle of the light, with a low angle the light will be very sharp with sharp shadow

v0.2.1 Logs

Features

- Spread Angle slider to change the angle of the spot light
- Rounded Radius to smoothly switch between a square and circle shape
- Add width and height to change the aspect ratio keeping same rounded radius

Fix

- Fix no light in render when un-check "View Camera"
- Some renaming, ordering of the nodes
- Display switch to wire to have a clean overview of the scene when using a lot of lights
- Rewriting the gradient algorithm for better quality

