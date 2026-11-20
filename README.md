# Arduino-Project
This repo is going to be about an Arduino project I am making using an Arduino and AI


# Hand Signal Computer Controller (Arduino Uno R3 + ML)

## Goal

Build a system that lets me control my computer with hand signals, using the Arduino Uno R3 from my Super Starter Kit. A distance sensor watches my hand, a small machine learning model recognizes the signal (hand up, hand down, swipe, hold), and my computer reacts, starting with volume up/down, play/pause, and skipping tracks.

## Why

I wanted a project where the Arduino and my computer work together instead of the Arduino doing everything alone. It also turned out to be the right way to do ML on an Uno: the board is too small to train a model, but it can run one that was trained elsewhere.

## Hardware

- Arduino Uno R3 (ATmega328P, 2 KB SRAM, 32 KB flash) from a Super Starter Kit
- HC-SR04 ultrasonic distance sensor (from the kit) - main input
- USB cable to connect the Uno to my computer
- Jumper wires and breadboard (from the kit)
- Optional/stretch: MPU-6050 (GY-521) motion module, if my kit has one

## How it works, end to end

1. The HC-SR04 on the Uno constantly measures how far my hand is.
2. While I do a hand signal, the readings stream to my laptop over USB serial.
3. I record many examples of each signal on the laptop and label them.
4. I train a small classifier in Python on the laptop (the laptop does the training, not the Uno).
5. The trained model is converted to C code and uploaded to the Uno.
6. From then on, the Uno runs the model itself: sensor in, recognized signal out, sent over serial.
7. A small Python program on my computer reads the recognized signal and turns it into an action (volume, play/pause, skip).

## The ML part, simply

The Uno R3 has only 2 KB of RAM, so training on the board is not possible. The standard approach for boards like this is: collect data, train on a computer, shrink the model down, and deploy it to the board so recognition happens on the Uno in real time. The model stays small on purpose: a few sensor readings per step, a handful of signal classes.

## Milestones

1. Get live distance readings from the HC-SR04 into the laptop over serial.
2. Record a dataset of my hand signals.
3. Train the classifier on the laptop and check its accuracy.
4. Convert the model to C and run it on the Uno.
5. Map recognized signals to computer actions (volume, media keys).
6. Demo: control my computer with hand signals, no keyboard.

## Risks and limits

- 2 KB of RAM limits model size and how many signals I can support.
- One distance sensor only sees one axis, so signals have to be designed so they look different from that one viewpoint (height changes, approaches, holds).
- Accuracy will depend on how consistent my signals are and how much data I record.

## Stretch ideas

- Use the MPU-6050 (if the kit has one) to recognize tilt and rotation gestures, not just distance.
- More actions: scroll, switch apps, control YouTube playback.
- Visual feedback on the computer showing what the model thinks it sees.
