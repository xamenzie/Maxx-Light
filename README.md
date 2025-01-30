# Maxx Utilities

It's a Blender Addon that help to save time with some tools. It presents as a Pie Menu accessible with Ctrl + D shortcut.

## Maxx Light

An Aera light with some added features.

Maxx Light Features :

  - Keep all benefice of the aera light, still can be used as Square or Disk shape
  - Gradient power : create a gradient and can be adjust with this setting (useful in reflection for exemple and with a little spread)
  - Round Corner : to break the sharp corner of the Square
  - WB coloration : to rapidly colored the light based on kelvin temperature
  - Procedural Gobo shape and animation

<img src="https://github.com/xamenzie/Maxx-Utilities/assets/50946132/d1a1adcb-d02b-4441-824e-1f98978f3fd5)" width="250" height="250"/> <img src="https://github.com/xamenzie/Maxx-Utilities/assets/50946132/cc348784-4695-470a-86e4-492ea0c11ce7" width="250" height="250"/> <img src="https://github.com/xamenzie/Maxx-Utilities/assets/c4e9fad3-6366-4490-bd8f-904ab934a3b9" width="250" height="250"/>


## Quick render settings

Set the basics render settings for a nice and quick render, which change automatically these settings when used :

  - Set the device to GPU
  - Set adaptive sampling with a threshold at 0.02 and 800 samples
  - Activate Denoise in the render
  - Desactivate the denoising in render (meant to use another denoiser like SID denoiser addon)
  - Desactivate light tree
  - Setup simple bounces for the lights
  - Set the render output to PNG RGBA 16bits
  - Activate persitent data

## Basic Collections structure

Create basic collection strucure to keep organised. It presents with this tree structure :

__ Scene<br>
__ Tech<br>
_____ gr_Lights<br>
_____ gr_Cam<br>

## To do

  - Add the ability the add image texture or noise pattern in the light very easily
  - Import the light at the current cursor position
  - Exponant the light power

## Updates

### v0.3.2

  Features & Fix

  - The Aera light is now imported at the 3d cursor
  - Added Animation and Still quick render settings, changing between Optix (for anime) and Openimagedenoise and switching noise threshold between 0.02 and 0.01
  - Activate persitent data
  - Removed Gobo texture, too much bugs for now

### v0.3.0

  Features & Fix

  - New system of light, based on the aera light which is more fast and stable in the render, still WIP for now
  - Adjust the Gradient Power from 0 to 3
  - Add round corner settings to the square light
  - Add "WB coloration" and "White Balance" to switch between the colour of the light and Kelvin colour based
  - The gradient is automatically adjusted if the light is in Square or Disk mode
  - Change basic settings, noise threshold from 0.04 to 0.02, sample from 1000 to 800 and activate the denoise in the render

### v0.2.2

  Features

  - Addon switch to a Pie menu instead of a button, which is even more quick to use
  - Quick render settings
  - Basic Collections structure

  Fix

  - new way of calculating the spread angle for the light, with less noise

### v0.2.1

  Features
  
  - Spread Angle slider to change the angle of the spot light
  - Rounded Radius to smoothly switch between a square and circle shape
  - Add width and height to change the aspect ratio keeping same rounded radius
  
  Fix
  
  - Fix no light in render when un-check "View Camera"
  - Some renaming, ordering of the nodes
  - Display switch to wire to have a clean overview of the scene when using a lot of lights
  - Rewriting the gradient algorithm for better quality

