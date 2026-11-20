# Arduino-Project
This repo is going to be about an Arduino project I am making using an Arduino and AI


# Arduino-Project
This repo is going to be about an Arduino project I am making using an Arduino and AI

# Five Tiny ML Models on an Arduino Uno R3

## Goal

Train 5 small machine learning models that each do a separate thing on the Arduino Uno R3 from my Super Starter Kit. Every model reads one sensor, learns a pattern, and reacts on its own. The first one is my own idea: a hand-signal controller for my computer.

## Why

One model was fun, but five is a real project. It forces me to solve the same problem once (how to record data, train on my laptop, and get a model small enough for the Uno) and then reuse that pipeline for everything else. The Uno R3 is too small to train models, but it can run ones that were trained elsewhere, so that is the whole setup.

## Hardware

- Arduino Uno R3 (ATmega328P, 2 KB SRAM, 32 KB flash) from a Super Starter Kit
- USB cable to connect the Uno to my computer
- Jumper wires and breadboard (from the kit)
- Sensors from the kit, one per model (see below)

## The 5 models

1. Hand-signal computer controller (my idea): the HC-SR04 distance sensor watches my hand, the model recognizes signals (hand up, hand down, swipe, hold), and a Python program on my computer turns them into actions, starting with volume up/down, play/pause and skipping tracks.
2. Smart fan decision (proposed): the DHT11 reads temperature and humidity, and the model learns when a fan should turn on instead of a simple fixed threshold.
3. Light pattern reader (proposed): the photoresistor reads light levels, and the model learns patterns like day vs night, or a flashlight signal, and reacts.
4. Motion gestures (proposed, only if my kit has the MPU-6050/GY-521 module): the motion sensor learns tilt and movement gestures.
5. Sound patterns (proposed): the sound sensor learns to tell apart sounds like a clap, a snap or silence.

Models 2-5 are my proposed list from kit parts. I can swap any of them as I go; the point is 5 models, each with one job and a different sensor.

## How it works, end to end

The pipeline is the same for every model:
1. Wire the sensor to the Uno and stream its readings to my laptop over USB serial.
2. Record many labeled examples on the laptop.
3. Train a small classifier in Python on the laptop (the laptop does the training, not the Uno).
4. Convert the trained model to C and upload it to the Uno.
5. From then on the Uno runs the model itself: sensor in, decision out, either on the board (LED, buzzer) or over serial to a small Python program on my computer.

## The ML part, simply

The Uno R3 has only 2 KB of RAM and 32 KB of flash, so training on the board is not possible, and five models make that limit tighter. Every model has to stay tiny: a small decision tree or a very small network, a few sensor readings in, a handful of classes out. If all five do not fit on the board at once, that is fine: the Uno can run one at a time, and I swap which one is loaded.

## Milestones

1. Build the shared pipeline: live sensor readings over serial, recording and labeling data on the laptop, training, converting to C, running on the Uno.
2. Model 1 (hand-signal controller): distance readings, gesture dataset, training, deploy to the Uno, map signals to volume and media actions, demo controlling my computer with no keyboard.
3. Models 2-5, one at a time, reusing the pipeline from step 1.
4. Final demo: all 5 models working, even if they take turns on the board.

## Risks and limits

- 2 KB of RAM limits model size, so each model supports only a few classes.
- 32 KB of flash may not hold all five models at once; running one at a time is the backup plan.
- Each model only sees one simple sensor, so patterns have to be designed to look different from that sensor's point of view.
- Accuracy will depend on how consistent my examples are and how much data I record.
- Model 4 depends on my kit actually having an MPU-6050; if it does not, I will swap it for another kit sensor.

