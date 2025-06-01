---
title: What is a Microcontroller
permalink: what-is-microcontroller
date: 2022-08-07
excerpt: 
type: Blog
categories: 
tags: 
status:
---

![Image](/assets/images/Pasted-image-20220807102919.png)
After Inventing Transistor in 1948 and Integrated circuit in 1960, a revolutionary change came into circuit design. People started solving real life problems using analog electronic components like Transistor, diode,OP-Amp  etc.  
After a while people realized solving real life problems, circuit requires some qualities.  
such as:

-    Arithmetic calculating ability,
-   Decision making ability, 
-   Time measuring ability
-   Data saving ability  for future use etc.

For all these advantages available in digital circuits, it got popularity in the field of electronics industry. One question may be arise in your mind.

**what is the fundamental difference between analog and digital circuits????**

> **Analog circuits** are basically operated by continuous type signal.In diagram given below, green signal is analog continuous sinusoidal signal.

> **Digital circuits** are operated by a signal exist only two discrete voltage levels, such as low and high voltage. This signal is also called binary signal(two states signal), because two voltage level are expressed in two binary digit 1’s and 0’s. Here blue signal is digital signal. It has only two states: High(10V) & Low voltage(-10V) level.


![Image](/assets/images/analog-20vs-20digital_zps007v5du4.webp)



Analog & Digital signal

We will discuss in details succeeding tutorials about digital circuits

-   Digital circuits
-   How does microcontroller perform complex calculation using logic circuits 
-   logic Implementation
-   Why binary system is used in digital circuit instead of decimal system etc. 
-   How to program a microcontroller to performer specific task.

For now our discussion is limited to Microcontroller!.

### What is Microcontroller?

![Image](/assets/images/Pasted-image-20220807103225.png)

Frankly speaking, **Microcontroller is a computer**. You may be wondered how does this tiny chip be a computer?. For this, at first you have to know what are the main parts of a computer? . 

**Generally a personal computer contains these parts**

![Image](/assets/images/Pasted-image-20220807103245.png)

-   Central Processing Unit(CPU) i.e Intel core i3 speed 3.1 GHz
-   RAM -> 2GB
-   Memory(Hard disk) -> 500GB
-   Input devices like mouse, keyboard etc.
-   Output device like monitor, printer etc.

**A Microcontroller([Atmega 32](https://www.google.com.bd/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CBwQFjAA&url=http%3A%2F%2Fwww.atmel.com%2Fimages%2Fdoc2503.pdf&ei=A5cSVdOVJpGQuATFvoHwDQ&usg=AFQjCNG1k6mR6bQZIQsf2zqLvRXzf4DIPQ&sig2=t9vTYrESAPMLqCZkmWb_FA)) contains these parts**

-   A CPU -> speed 0 to 16MHz
-   RAM -> 2KB
-   Memory 1024 Byte
-   32 Input/ Output Pins
-   Peripherals like Timer, ADC(Analog to Digital converter), Interrupt, SPI, USART, RTC, 
-   To know more, please read first page of [this Microcontroller datasheet](https://www.google.com.bd/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CBwQFjAA&url=http%3A%2F%2Fwww.atmel.com%2Fimages%2Fdoc2503.pdf&ei=A5cSVdOVJpGQuATFvoHwDQ&usg=AFQjCNG1k6mR6bQZIQsf2zqLvRXzf4DIPQ&sig2=t9vTYrESAPMLqCZkmWb_FA)

So there is no basic structural differences between a computer & Microcontroller. Microcontroller has every element a computer has but little amount. 

> A conclusion may be given that **_Microcontroller=CPU+Peripherals+RAM+Memory+Input/Output pins_**  
> **_Peripherals=Timer+ADC+Interrupt+SPI+USART+RTC etc._**

►Good news is that, Microcontroller is a low cost computer in a single chip .

### Example of usages

One thing is clear that microcontroller is a tiny computer and it is used instead of personal computer where real time automation is need in a low cost and small space.
![Image](/assets/images/Pasted-image-20220807103303.png)

1.  Think about this [Android Controlled Robot](http://www.eeetechbd.com/2015/02/Android-controlled-Robot-using-AVR-Microcontroller.html)(please see the video in the link to visualize). Here Android smartphone sending data through bluetooth. According to data received by microcontroller, the CPU takes action which tasks it will execute. Here executing these tasks we don’t need a high processing speed intel core i3 processor(3.1GHZ) and 4GB of RAM. All these actions can be easily and smoothly operated by a microcontroller. Here we use a Microcontroller model [Atmega 32](https://www.google.com.bd/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CBwQFjAA&url=http%3A%2F%2Fwww.atmel.com%2Fimages%2Fdoc2503.pdf&ei=A5cSVdOVJpGQuATFvoHwDQ&usg=AFQjCNG1k6mR6bQZIQsf2zqLvRXzf4DIPQ&sig2=t9vTYrESAPMLqCZkmWb_FA), which operates in 16Mhz and has only 2KB of RAM. So it saves cost maintaining efficiency. Price of a microcontroller is close to [few dollars](http://www.ebay.com/itm/1PCS-ATMEGA32A-ATMEGA32A-PU-MCU-AVR-32K-FLASH-16MHZ-40-PDIP-NEW-/251887380044?pt=LH_DefaultDomain_0&hash=item3aa5a8664c) 
2. Think about air conditioned in your home.Cooling system is controlled by sensing indoor temperature of your room using a temperature sensor. We don’t need to set a personal computer to automate this task. All the task can be automated by a Microcontroller rather than manual remote control.
    
![Image](/assets/images/Pasted-image-20220807103313.png)
    
3.  Microcontroller is widely used in industrial automation, home automation, Robotics, Embedded devices, control system etc.

### Microcontroller Types

Please check [wikipedia link](http://en.wikipedia.org/wiki/List_of_common_microcontrollers) to know microcontroller manufactures. In our tutorila we use popular [Atmel AVR](http://www.atmel.com/)  8 bit microcontroller. Atmel produces 3 types of 8 bit Microcontroller

1.  XMEGA AVR
2.  Mega AVR
3.  Tiny AVR

Most of the tutorials we use [Mega AVR](http://www.atmel.com/products/microcontrollers/avr/megaavr.aspx) microcontroller.

**Why Microcontroller is used instead of analog circuits??**

→A system developed using Microcontroller is known as **embedded system.**

→**Embedded system** is an electrical system which operates with help of circuit and code.

-   Microcontroller is a low cost computer, so it can perform calculations, can make decision, process data, save data. It is quite impossible using analog circuit.
-   You can maintain your your copyright, system developed using Microcontroller. Think about the situation. You design a system using analog circuits like [this](http://www.eeetechbd.com/2015/03/automatic-water-pump-controller-using-bjt.html) and start selling final product. but it can be easily copied if you haven’t licensed it. But if you design the same system using Microcontroller you can protect your code using password lock. 

This is our series tutorial on AVR microcontroller. Next tutorials are listed below:

1.  Software and Hardware requires for starting AVR Microcontroller
2.  Your first AVR Microcontroller Program














---

Shuvangkar Das, PhD
Knoxville, Tennessee, USA

### 🚀 Hey! what's cool I'm doing now
I am making a very interesting video series on "smart personal knowledge management(SPKM)"". The idea is to make learning and knowledge-work easy and effective. Everybody does some form of knowledge work but most of the time does that inefficiently. As a result, despite working hard, we ended up with questionable results. I will address this problem in this course. So, do subscribe on [YouTube](https://www.youtube.com/ShuvangkarDas) 

### ☎ Connect with me
- Twitter: [https://twitter.com/shuvangkar_das](https://twitter.com/shuvangkar_das)
- LinkedIn: [https://www.linkedin.com/in/ShuvangkarDas/](https://www.linkedin.com/in/ShuvangkarDas/)
- YouTube: [https://www.youtube.com/ShuvangkarDas](https://www.youtube.com/ShuvangkarDas)

### 📚References




