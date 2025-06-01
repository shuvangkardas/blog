---
Title: Design of Electronic Switch using BJT Transistor
Author: Shuvangkar Das
Date: 2015-03-02
aliases: 
tags: 
Status:
---
Normally the function of a switch is either turning on or off close path of current flow and carry current at any direction. If there were no switches, we would have to disconnect or connect every time from main power supply whenever we need to turn off or on light, fan etc. These are all mechanical switches which mechanically disconnect appliances from main power supply.

BJT(Bipolar Junction Transistor) is a solid state electronic switch which can perform switching operation without mechanically disconnected. It is the great invention in the field of electronics. This solid state switch is used for

1. Controlling high power devices like motors, solenoids , Relays etc.
2. Digital electronics and logic gate circuits and many others.

By observing a microcontroller model atmega32 datasheet, I found, it can provide maximum current of 40mA at guaranteed operating condition. So when we need to Run a relay(requires about 80mA current) DC motor(Requires more than 150mA current) what is the solution????

Then BJT is the simplest and low cost solution as I found from study.

## How to design BJT as a electronic switch?

Before we start our main discussion, let's see the schematic how I control a dc motor using 5 voltage pulse(Microcontroller pulse) but motor(In circuit motor is indicated by yellow light) is originally powered up by a 9 voltage battery.

![Image](/assets/images/featureimage_zpscbb63641.webp)

For my convenience I guess, you know the basic operating principal of BJT,how it works and you solved BJT related problems but right now you don't know how to design circuit using BJT to solve your real life problem.

## Some basic discussion regarding BJT

if you have the basic idea regarding cut-off mode and saturation mode you can skip fundamentals and go to DESIGN PROCEDURES.

Output characteristic of BJT is given below.

![Image](/assets/images/Pasted-image-20250601131946.png)

We know BJT works in three region

1. Cut-off region
2. Saturation region
3. Active region

Cut-off mode characteristic

1. BJT is fully off
2. Emitter-Base voltage Vbe<0.7 , So Emitter-Base Junction is reversed biased
3. Collector-Base Junction is also reverse biased
4. Zero base and collector current
5. Collector Emitter voltage Vce will be high or maximum

As a result in cut-off mode BJT works as a **open switch** just given below.

![Image](/assets/images/Pasted-image-20250601132007.png) Saturation Mode characteristics

1. BJT is fully on
2. Maximum base and collector flows( depletion layer decreses)
3. Collector emitter voltage is minimum (100mV to 300mV). In diagram 134mV
4. Emitter-base and collector Base junction are forward biased.

As a result The Transistor works as a **Closed switch** given below.

![Image](/assets/images/BJTsaturationmode_zpsaaba0e47.webp)

**N.B:**

> - In both cut-off and saturation mode BJT dissipates minimum power.
>     
> - So now one thing is clear that using cut-off mode and saturation mode behavior we can use BJT as a **SPST switch**
>     

### **Design Procedures:**

**Now we start our main discussion on How you precisely design BJT as a switch for your project.**

## Design Cut-off Mode:

Designing Transistor as cut-off mode is very simple. When any high current device(Motor, Solenoid, Relay) is running under BJT switch just make Vbe< 0.5(EBJ and CBJ are reversed biased) or **connect** **the base with ground.**

![Image](/assets/images/Cutoffmodedesign_zpsf9d0fda0.webp)

## Design Saturation mode

BJT will go to saturation when Emitter-Base and Collector Base junction are forward biased. It is a little bit tricky to design BJT in saturation mode. We need to Increase Base voltage sufficiently large enough for collector Base junction to become forward biased and transistor leave the active region and enters the saturation region.

We know BJT is not symmetric, So voltage drops different for two forward biased junctions are as follow.

![Image](/assets/images/Pasted-image-20250601132109.png)

**EOS (Edge of saturaion)** = This is the critical point between active region and saturation region.  
Before start our design we need to focus our problems and requirements.

> - We will run a 6V DC motor motor which equivalent circuit resistance is 20ohms and requires **230mA curent** to operate in the rated condition.
>     
> - So we need to operate the BJT in saturation region so that it can supply maximum current.
>     

![Image](/assets/images/saturationmodedesign_zps9dcdaffb.webp)

STEP 1:  
Calculate the Collector current **assuming the Transistor in saturation mode**. We know, in saturation mode Collector to emitter voltage is 0.2v . Using this voltage value we can calculate edge of saturation(EOS) collector current.  
In our design we use PN2222 transistor. [Click here](https://www.fairchildsemi.com/datasheets/PN/PN2222.pdf) to download datasheet.

$$V_{ce|saturation} = 0.2v$$

$$R_C = 20\Omega$$

$$I_{C(EOS)} = \frac{V_{CC} - V_{ce|saturation}}{R_C}$$

$$I_{C(EOS)} = \frac{5 - 0.2}{20}$$

$$= 240mA$$

which is less then our transistor model PN2222's collector current. It can handle 600mA of collector current

STEP 2:  
Calculate Base current from collector current. So we need minimum beta which we find from manufacture datasheet. For PN2222 transistor minimum Dc current gain beta is 100

$$I_{B(EOS)} = \frac{I_{C(EOS)}}{\beta_{min}}$$

$$= \frac{240}{100}$$

$$= 2.4mA$$

This is the minimum base current which keeps the transistor at the edge of saturation region. If we increase the base current more by a factor, we are driving the Transistor further into saturation. The factor is known as Overdrive factor(ODF).

$$ODF = \frac{I_B}{I_{B(EOS)}}$$

We let ODF=10 which means we are forcing the transistor go deep into saturation 10 times than edge of saturation.

$$I_B = ODF \times I_{B(EOS)}$$

$$= 24mA$$

STEP 3:  
The standard format of the preceding circuit is given below. Now we calculate Base resistor Rb value so that the transistor stays saturation mode.

![Image](/assets/images/saturationmodestandardmodel_zps5eba4362.gif)

$$I_B = \frac{V_B - V_{BE}}{R_B}$$

$$R_B = \frac{V_B - V_{BE}}{I_B}$$

$$= \frac{5v - 0.7v}{24mA}$$

$$= 179\Omega$$

Nearest available value for **Rb is 200** Ohm.

In the simulation we notice that all the values are close to our calculated value. So design is complete.

## Checking Saturation region:

No we will check whether the transistor is operating in the saturation region or not.  
If transistor operates in the saturation region, then saturation mode Dc current gain will be much less than Active mode minimum DC current gain .

$$\beta_{forced} = \frac{I_C}{I_B}$$

$$= \frac{240mA}{24mA}$$

$$= 10 < 100$$

$$\beta_{forced} < \beta_{min}$$

As Beta is much less than Active mode minimum beta, so our design is perfect and the transistor is operating in the saturation region.


**[Check this tutorial for advance BJT application!]({% post_url 2015-03-02-Automatic-Water-pump-controller-using-BJT %})**