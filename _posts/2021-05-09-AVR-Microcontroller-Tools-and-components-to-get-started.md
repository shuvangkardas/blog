---
title: AVR Microcontroller-Tools and Components to Get Started
permalink: 
date: 2022-07-16
excerpt: A beginner-friendly guide to essential software, hardware, and components for learning AVR microcontroller programming
type: Blog
categories:
-
tags:
-
status: 
---


![Image](/assets/images/Pasted-image-20220807102419.png)
So in this blog, I will provide you the list of components and software for learning AVR microcontroller. In the last tutorial, we discussed the microcontroller. If you miss the last writing please read from here.

So, the first thing you need for learning a microcontroller is a basic understanding of C programming. This is mandatory because we are not going to discuss C programming in this series. We are going to leverage C programming to write a program for the microcontroller and C is the most popular language for writing code for the microcontroller. Nowadays, most microcontrollers also support C++, and a few support micro-python. The question is how much do you need to know about c programming for understanding this series.

## Software and Hardware

1.  **Microchip Studio:** This is the main IDE(Integrated development environment) for AVR microcontrollers. If you don’t know about the IDE please do a quick google search. The good thing about this IDE is it is completely free. Whereas you have to pay to use a few popular microcontroller IDEs.
2.  **Proteus:** Proteus is a simulation software especially popular for simulating microcontroller circuits. Proteus has a rich set of AVR microcontroller libraries. So when we build a program for the AVR microcontroller, first we will simulate the circuit using proteus. If the simulation successful then we will build the circuit in the breadboard of PCB.
3.  **Burner Software:** So we write our code for the microcontroller and simulate it using proteus. Everything is ok to build the real circuit. After building the circuit we need to write the code into the microcontroller. Writing the code into the microcontroller memory is called burning program. For burning the program into the microcontroller, we need two things a special software and special hardware. The software is called Burner Software. We are going to use the Extreme burner in this tutorial.
4.  **Programmer or burner:** We understand that we need special hardware for burning the program into the microcontroller. This is called programmer. The programmer we are going to use throughout this blog series is USBasp. This programmer is low cost and available in most of the country. Don’t worry if you do not have one and cannot manage one. We can build our programmer using the Arduino Uno board.

## Components

1.  Atmega328: This is the main microcontroller we are going to use throughout this blog series
2.  7805:  5V linear regulator IC.
3.  Capacitor: 0.1uF, 1uF, 4.7uF, 100uF
4.  Switch: Push Button, Slide Switch
5.  L293D: Motor Driver IC
6.  Light Sensor: LDR(Light-dependent Resistor), IR sensor(Rx+Tx)
7.  Resistor:100Ω, 220Ω, 330Ω, 1kΩ, 4.7kΩ, 10kΩ, 1MΩ
8.  Potentiometer: 10kΩ, 1kΩ, 1MΩ
9.  Op-AMP: LM324, LM358
10.  Crystal Oscillator: 16Mhz, 8Mhz
11.  Led light: 3mm, 5mm (different colors like red, green, yellow)
12.  Display: 7 segment display(1digit,2digit,4digit), 16×2 LCD display
13.  Diode: 1N4007, zenor diode(5.1v, 3.6v)
14.  Transistor: BC 547, 2n2222,BC548
15.  Motor: 12V DC gear motor, Servo motor
16.  Battery: Battery rating should be more than 7V, close to 1000mA
17.  Rail: IC rail, rail connector(male+female)

## Tools & Appliances

1.  Multimeter:
2.  Breadboard:
3.  Vero board:
4.  Soldering Component: Soldering Iron, Soldering resin, soldering lead, Soldering sucker
5.  Component Box: Here you keep all your components.
6.  Connecting wire: (1)Male to male type (2)Male to female type (3)female to female type connecting wire requires for your projects.
7.  Programmer: For uploading code from PC to microcontroller you need a mid-level converter. Nowadays USB programmer gets popularity. Previously parallel programmer was used. USBasp developed by Thomas Fischl is the most popular USB Programmer. This is low cost programmer. You can collect this from here.  
    Wire stripper: It is used to trip the electrical insulation from electrical wire.

That’s all you need to start learning AVR Microcontroller. Please google to know more about these components.  
This is our series tutorial on AVR microcontroller. So like our Facebook page to keep an update.



---

Shuvangkar Das,PhD
Knoxville, Tennessee, USA

### 🚀 Hey! what's cool I'm doing now
I am making a very interesting video series on "smart personal knowledge management(SPKM)"". The idea is to make learning and knowledge-work easy and effective. Everybody does some form of knowledge work but most of the time does that inefficiently. As a result, despite working hard, we ended up with questionable results. I will address this problem in this course. So, do subscribe on [YouTube](https://www.youtube.com/ShuvangkarDas) 

### ☎ Connect with me
- Twitter: [https://twitter.com/shuvangkar_das](https://twitter.com/shuvangkar_das)
- LinkedIn: [https://www.linkedin.com/in/ShuvangkarDas/](https://www.linkedin.com/in/ShuvangkarDas/)
- YouTube: [https://www.youtube.com/ShuvangkarDas](https://www.youtube.com/ShuvangkarDas)

### References
1. 





