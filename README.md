# Sampling-Studio

- [Sampling-Reconstruction-Signals](#sampling-reconstruction-signals)
  - [Features](#features)
  - [Demos](#demos)
    - [Reconstruction Demo](#reconstruction-demo)
    - [Composer Demo](#composer-demo)
  - [Run-App](#run-app)

## Features
- Developing an illustrator for the signal recovery that shows Nyquist rate.
- read csv signal and see the sampled points highlighted on top of the signal.
- Change the sampling rate via a slider that range from 0 Hz to 3f max
- Reconstruct/recover the signal from the sampled points.
- Application has a Composer to generate basic signals to test and validate on the app
- One graph to display the sinusoidal to be generated
- One graph to display the sum of the generated sinusoidals. 
- A combobox to select one of the contributing sinusoidals and remove it via a delete button.
- After making a synthetic signal then moving it to the main illustrator graph to start the sampling/recovery process.

## Demos

### Composer Demo 
![Composer](doc/videos/Project_composer_part.gif)

### Reconstruction Demo 
![Sampler](doc/videos/Project_sampler_part.gif)

## Run-App
1. **_install project dependencies_**
```sh
pip install -r requirements.txt
```
2. **_Run the application_**
```sh
python main.py

