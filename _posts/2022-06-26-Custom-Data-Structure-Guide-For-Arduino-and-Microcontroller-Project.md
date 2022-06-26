Data structure provides an efficient way of organizing data and functionality in the digital system. Good data structure design makes the system efficient and fast. There are few standard data structures in computer literature.

-   Queue
-   Stack
-   Array - One dimension as vector
-   Array - Multi dimension as Matrix
-   List
-   Tree

Apart from the standard data structure, we can design our own custom data structure according to project requirements. Design custom data structure makes our life easy and makes the code more portable and readable. In this document, I will focus on custom data structure design for embedded systems. This data structure design pattern can be used with any microcontroller and Arduino project. Previously I have employed these techniques in many projects including AVR microcontroller, PIC microcontroller, MSP430 microcontroller, ESP32, ESP8266, and ARM microcontrollers as well as Arduino.

### Why do we need to design a custom data structure?

Consider we are going to design a toy data acquisition system for temperature and humidity. We are going to put timestamp and device id with the sensor data. So, for this system, we need to allocate four variables

```c
int devideId;
uint32_t unixTime;
float temperature;
float humidity
```

Yes, we can use these variables as a global variable and build our whole system. In this way, we cannot make a modular system. Because whenever we want to build any pure function we have to pass all the variables as a function parameter. Moreover global variable always performs slower than the local variable. Think about a scenario, we want to send the sensor data to a web server and we have a function like following

```c
void sendData(int devId, uint32 time, foat temp, float hum)
{
	//code for sending data to the server
}
```

See, we have to pass a bunch of variables to design a send function for sending data into the server. When we have a lot of data it would be very difficult to deal with. Of course, we can put all the variables into an array and pass the pointer. But that is less intuitive. Also, we can use a global variable for the data and use the variable in the send function. Remember one thing, the more we use global variables in your system, the more our code loses readability and portability. Also global variable performs slower than the local variable. So it is not a good programming practice to use many global variables in any projects. There are a lot of problems with using global variables. Of course, we cannot neglect global variables in embedded system design. Nevertheless, we should avoid using too many global variables.

### Design custom data structure

Designing custom data structures in C and C++ is fairly straightforward. We can use `structure` to design the data structure for our data acquisition system.

```c
struct sensorData_t
{
	int deviceId;
	uint32_t unixTime;
	float temperature;
	float humidity;
};
```

Now `sensorData_t` structure holds all the related variables for our toy data acquisition system. We also need to remember carefully that `struct sensorData_t` is a derived structure data type not a structure variable. Just like `int` data type. using the `struct sensorData_t` data type we can declare variable like following.

```c
struct sensorData_t sensorData1;
struct sensorData_t  sensorData2
```

Now the question is how can we use this simple data structure to modularize our whole system.

In the next section, I will demonstrate the ways how we can fulfill this purpose using pseudocode.

### Read Sensor Data

Let’s consider we have implemented these functions to read all the sensors and store in the variables. We also tested these functions ins and out and made sure everything is working fine.

```c
int getDeviceId();
uint32_t getUnixTime();
float readTemperature();
float readHumidity();
```

Now we are going to utilize these functions to build our final sensor read function for reading all sensor data in a combined way. We discussed earlier that `struct sensorData_t` is derived data type and `sensorData` is the variable of that type.

```c
void readSensors(struct sensorData_t sensorData)
{
	sensorData.deviceId = getDeviceId();
	sensorData.unixTime= getUnixTime();
	sensorData.temperature = readTemperature();
	sensorData.humidity = readHumidity();
}
```

We have written the `readSensor()` function to collect all the sensor's data and metadata. In our system, we are collecting data every second and after one-minute interval, we will send all the data to the server because we want to reduce the communication burden. Moreover, it is not efficient to communicate with the server every second.

Let’s write the pseudocode to collects one minute(60 seconds) data

```c
//for 60 seconds 60 buffers of sensorData_t
struct sensorData_t sensorBuffer[60];  

for(uint8_t i= 0; i< 60; i++)
{
	readSensors(sensorBuffer[i]);
	delay(1000); //using delay is not efficient. This is just for demo
}
```

After one minute interval, I will have a big buffer of all my data for the last 60 seconds. This is how we simplified all the data management using a simple structure. Most newbies in the embedded systems are supposed to use big arrays for different variables. Now we can send this `sensorBuffer` using any communication channels such as Wi-Fi module(ESP32), SIM module(SIM800L), or any custom radio module such as nRF24L01, ZigBee, etc.

But still, there is a problem with this approach. Whenever our data structure is big in size, it is not going to work depending on our microcontroller register size. If we look into the `void readSensors(struct sensorData_t sensorData)` function, we can observe that every time, we are calling the function we are passing the 14 bytes(size of `sensorData_t`) of data as the function parameter. This is going to be super slow and inefficient and what if the data structure is big and more than the size of registers?

We can solve this problem easily by leveraging the pointer concept. The good point about pointer is that we don’t need to worry about data structure size because pointer variable size is always same for any variable type.

Let’s redefine the `void readSensors(struct sensorData_t sensorData)` function using pointer. We need to remember one thing, in this case, is that for accessing a member of a structure, normally we use `.` operator. In the case of structure pointer, we have to use the `->` operator for accessing a member of the structure pointer.

```c
void readSensors(struct sensorData_t *sensorPtr)
{
	sensorPtr->deviceId = getDeviceId(); //accesing deviceId member of the structure pointer
	sensorPtr->unixTime= getUnixTime();
	sensorPtr->temperature = readTemperature();
	sensorPtr->humidity = readHumidity();
}
```

Yeah!!, now see, the new `readSensors()` function takes the pointer of the `struct sensorData_t` type data type as input. If we analyze the size of input that should not be more than 4 bytes depending on the CPU architecture of the microcontroller. For the AVR microcontroller the pointer size is 2 bytes. That is far less than the previous 14 bytes as whole structure input.

Let’s rewrite our previous code for reading sensor data for 60 seconds intervals.

```c
struct sensorData_t sensorBuffer[60]; //for 60 seconds 60 buffers of sensorData_t 

for(uint8_t i= 0; i< 60; i++)
{
	readSensors(&sensorBuffer[i]); //Just & operator for passing pointer of sensorbuffer[i]
	delay(1000); //using delay is not efficient. This is just for demo
}
```

See, we just need to do one single change to get the code memory efficient and faster than before. Now we need to pass the pointer of each `sensorData_t` variable. If we use `&` operator before any variable, it means the address of that variable, not the variable itself. By this way, we can pass pointer of the variable.

### Print Sensor data

Now we have a custom data structure for our sensor data payload. Leveraging the structure, we can build a bunch of functions for doing the different tasks on the sensor data. For debugging the data, we need a print function. So that we can use the same function throughout the whole codebase for debugging the sensor data. Let’s see, how can we write such a function for doing such a task. For demonstrating the printing, I am going to use the Arduino default print function, but the method is the same for different microcontroller platforms.

```c
printSensor(struct sensorData_t *sensorPtr)
{
	Serial.println(F("<---------Sensor Data----------------->"));
	Serial.print(F("Time: ")); Serial.println(sensorPtr-> unixTime);
	Serial.print(F("Device ID: "));Serial.println(sensorPtr -> deviceId);
	Serial.print(F("Temperature: "));Serial.println(sensorPtr -> temperature)
	Serial.print(F("Humidity: "));Serial.println(sensorPtr -> humidity)
}
```

Voila! We can write any function using the same data structure. Now we can organize our code in a good manner no matter how many sensors we want to log. Another good point of using such a design pattern is that the code would be portable. Image, next time you need to add another sensor such as voltage sensor. you don’t have to change your whole codebase. you will add the variable inside your data structure and all the functions related to the data structure.

In the next part, I will add more functionality using the same data structure. Happy coding!!

