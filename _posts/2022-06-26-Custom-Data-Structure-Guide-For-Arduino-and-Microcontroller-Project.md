Data structure provides an efficient way of organizing data and functionality in the computer system. Good data structure design makes the system efficient and fast. It also helps to write modular code. You might be familiar with these types of data structure, Queue, Stack, Array, List, Tree. Apart from these standard data structures, we can design our custom data structure according to project requirements. It is very important to learn how to create custom data structures and build the functions around them. It will ease your firmware development and makes the code more portable and readable. 

I learned embedded system programming in 2013. I used to use a lot of global variables at the beginning. As a result, I had no choice other than writing messy code at that time. Gradually, I learned how to write modular and efficient code simply by designing a good data struct or utilizing object-oriented programming. This data structure design pattern can be used with any microcontroller and Arduino project. Previously, I have employed these techniques in many projects including AVR microcontroller, PIC microcontroller, MSP430 microcontroller, ESP32, ESP8266, and ARM microcontrollers as well as Arduino.


### Why do you need to design a custom data structure?
Consider you are going to design a toy data acquisition system for temperature and humidity. You will put the timestamp and device id with the sensor data. So, you need to allocate these four variables for this system. 

```c
int devideId;
uint32_t unixTime;
float temperature;
float humidity
```

Yes, you can use these variables as a global variable and build your whole system. In this way, you cannot make a modular system. Because, whenever you want to build any pure function you have to pass all the variables as a function parameter. A pure function is a type of function that does not depend on global variables. Moreover, you have to use these four variables in different files. That will result in less readable and maintainable code. Think about a scenario, where you want to send the sensor data to a web server and you have written a function as follows.

```c
void sendData(int devId, uint32 time, foat temp, float hum)
{
    //code for sending data to the server
}
```

See!, you have to pass a bunch of variables to design a send function. When you have a lot of data, it would be very difficult to deal with. Of course, you can put all the variables into an array and pass the pointer. But that is less intuitive. Also, you can use a global variable for the data and use that variable in the send function. Remember one thing, the more you use global variables in your system, the more your code loses readability and portability. Also global variable performs slower than the local variable. So it is not a good programming practice to use many global variables in any project. Of course, you cannot neglect global variables in embedded system design because you also have to care about the RAM. Nevertheless, you should avoid using too many global variables.

### Design custom data structure
Designing custom data structures in C and C++ is fairly straightforward. You can use `structure` to design the data structure for your toy data acquisition system.

```c
struct sensorData_t
{
    int deviceId;
    uint32_t unixTime;
    float temperature;
    float humidity;
};
```


Now `sensorData_t` structure holds all the related variables. You also need to remember carefully that `struct sensorData_t` is a derived structure data type, not a structure variable, just like `int` data type. using the `struct sensorData_t` data type you can declare as many variables as you want. 

```c
struct sensorData_t sensorData1;
struct sensorData_t sensorData2
```

Now the question is how can you use this simple data structure to modularize your whole system? We are going to explore that in the subsequent discussion. 

### Read Sensor Data
Let’s consider that you have implemented these functions to read all the sensors and store the variables. You also performed unit testing on these functions to make sure everything is working fine.

```c
int getDeviceId();
uint32_t getUnixTime();
float readTemperature();
float readHumidity();
```

Now I am going to utilize these functions to build a sensor read function for your toy data acquisition system. I discussed earlier that `struct sensorData_t` is the derived data type and `sensorData` is the variable of that type. So don't be confused about function parameters. If you do, please put your comment below. 

```c
void readSensors(struct sensorData_t sensorData)

{
    sensorData.deviceId = getDeviceId();
    sensorData.unixTime= getUnixTime();
    sensorData.temperature = readTemperature();
    sensorData.humidity = readHumidity();
}

```

Now, you can write the `readSensor()` function to collect all the sensor's data and metadata. Consider, in your system, you are collecting data every second and after a one-minute interval, you will send all the data to the server because you want to reduce the communication burden. Moreover, it is not efficient to communicate with the server every second.
Let’s write the pseudocode to collect one minute(60 seconds) of data.

```c
//for 60 seconds 60 buffers of sensorData_t
struct sensorData_t sensorBuffer[60];  
for(uint8_t i= 0; i< 60; i++)
{
    readSensors(sensorBuffer[i]);
    //using delay is not efficient. This is just for demo
    delay(1000); 
}

```

After one minute interval, you will have a big buffer that contains data for the last 60 seconds. Here, the big! is considered concerning a microcontroller. This is how you simplify all the data management using a simple structure. Most newbies in the embedded systems are supposed to use big arrays for different variables. Now you can send this `sensorBuffer` using any communication channels such as a Wi-Fi module(ESP32), SIM module(SIM800L), or any custom radio module such as nRF24L01, ZigBee, etc.

But still, there is a problem with this approach. Whenever your data structure has a lot of variables and strings, it is not going to work depending on our microcontroller register size. If you look into the `void readSensors(struct sensorData_t sensorData)` function, you may observe that every time, you are calling the function it is passing the 14 bytes(size of `sensorData_t`) of data as the function input. This will be super slow and inefficient and what will happens if the data structure is bigger than the size of registers?

You can solve this problem easily by leveraging the pointer concept. If you are afraid of hearing the word pointer, I was in your shoe a few years back. Let me tell you a secret about the pointer. Pointer just keeps the location information of variable. That means the size of a pointer is the same irrespective of data type. For example, For `int` pointer variable size and a `float` pointer variable size is the same, 2 bytes for AVR/Arduino Uno microcontroller. I will write in detail about the pointer and plan to make a YouTube video on my channel. Up to this point, you don't have to worry much about pointer. 

Let’s redefine the `void readSensors(struct sensorData_t sensorData)` function using pointer. You need to remember one thing, in the case of accessing a member of a structure, normally I useed dot(`.` )operator before. For structure pointer, you have to use the `->` operator for accessing members. That's the little change you have to accept for now, if you are afraid of the pointer. I believe you can do this. 

```c
void readSensors(struct sensorData_t *sensorPtr)
{
    //accesing deviceId member of the structure pointer
    sensorPtr->deviceId = getDeviceId(); 
    sensorPtr->unixTime= getUnixTime();
    sensorPtr->temperature = readTemperature();
    sensorPtr->humidity = readHumidity();
}

```

Yeah!!, now see, the new `readSensors()` function takes the pointer of the `struct sensorData_t` type as input. If you analyze the size of input that should not be more than 4 bytes depending on the CPU architecture. For the AVR microcontroller, the pointer size is 2 bytes. That is far less than the previous 14 bytes as whole structure input. Let’s rewrite the previous code for reading sensor data in 60 seconds intervals.

```c
//for 60 seconds 60 buffers of sensorData_t 
struct sensorData_t sensorBuffer[60]; 
for(uint8_t i= 0; i< 60; i++)
{
    //Just & operator for passing pointer of sensorbuffer[i]
    readSensors(&sensorBuffer[i]);
    delay(1000);
}

```

See!, you just need to do one single change to get the code memory efficient and faster than before. Now you need to pass the pointer of each `struct sensorData_t` variable. If you use `&` operator before any variable, it means the address of that variable, not the variable itself. In this way, you can pass the pointer(address) of the variable.

### Print Sensor data
Now you have a custom data structure for sensor data payload. Leveraging the structure, you can build a bunch of functions for doing the different tasks on the sensor data. For debugging the data, you need a print function. So that you can use the same function throughout the whole codebase for debugging the sensor data. Let’s see, how can we write such a function for doing such a task? For demonstrating the printing, I am going to use the Arduino default print function, but the method is the same for different microcontroller platforms.

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

Voila! you can write any function using the same data structure. Now you can organize our code in a good manner no matter how many sensors you want to log. Another good point of using such a design pattern is that the code would be portable and manageable. Imagine, next time you need to add another sensor such as a voltage sensor, you don’t have to change your whole codebase. You will just add the variable inside your data structure and makes changes inside the function. You don't have to work on the upper layer function that you have already built on top of this file.

In the next part, I will add more functionality using the same data structure. Happy coding!! and don't forget to subscribe to my channel.
