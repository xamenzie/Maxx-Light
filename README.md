It's a Blender Addon that help to save time with some tools. It presents as a Pie Menu accessible with Ctrl + D shortcut.

# Maxx Light

A "go to" light to use in almost every situation. Meant to be used as an assets.

Maxx Light Features :

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

# Quick render settings

Set the basics render settings for a nice and quick render, which change automatically these settings when used :

  - Set the device to GPU
  - Set adaptive sampling with a threshold at 0.04 and 1000 samples
  - Desactivate the denoising in render (meant to use another denoiser like SID denoiser addon)
  - Desactivate light tree
  - Setup simple bounces for the lights
  - Set the render output to PNG RGBA 16bits

# Updates

v0.2.2 Logs


#### v0.2.1 Logs

  Features
  
  - Spread Angle slider to change the angle of the spot light
  - Rounded Radius to smoothly switch between a square and circle shape
  - Add width and height to change the aspect ratio keeping same rounded radius
  
  Fix
  
  - Fix no light in render when un-check "View Camera"
  - Some renaming, ordering of the nodes
  - Display switch to wire to have a clean overview of the scene when using a lot of lights
  - Rewriting the gradient algorithm for better quality

