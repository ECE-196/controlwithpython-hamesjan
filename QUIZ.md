### How does the DevBoard handle received serial messages? How does this differ from the naïve approach?
The devboard uses interupt handlers to receive serial messages. We define an event for the interupt to go off (ARDUINO_HW_CDC_RX_EVENT)
which triggers when the devboard receives bytes over serial and the receive buffer is not empty. Then, we define a function in the firmware that handles this 
event, such as writing to an LED. This differs from the naive approach in the way that the loop function does not need to be populated because it is all
driven by interupt handlers.

### What does `detached_callback` do? What would happen if it wasn't used?
The detached callback enables the UI to stay interactable in the case that serial code takes a long time or freezes. It makes all the functions marked with the 
detached_callback decorator run in a detached thread rather than the main thread. If it wasn't used, the UI would freeze up if serial code was taking too long or freezed or there was a bug.

### What does `LockedSerial` do? Why is it _necessary_?
The LockedSerial creates a semaphore to enforce concurrency and prevention of race conditions for usage of my port. This is necessary because if multiple threads using detached_callback tried to access the same port at the same time, undefined behavior would arrise due to the race conditions created by simultaneous access.