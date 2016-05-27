# Payton's Binary-Unicode Translator



## Functional Specification

This document should become the functional specification of the project you are working on.

A functional specification describes in great detail how a device or program will appear to an
outside user. That is, it treats all hardware as a "black box", the contents of which are completely
unknown to the user. The functional specification should include sections with the following information:

Your specification **should include** the following types of information:

* A title. Replace the title at the beginning of this document.
* Summary or introduction. In general, in a few lines or less, what is your program about or what is it about?
* How does the user access your program? Is it shared via http://runpython.com? Is a web site? Embedded in 
  a single board computer? 
* If there are graphics screens involved, describe every screen that the user will experience: what is it for? 
  What did the user have to do to get there and how does she move on to the next?
* For each graphics screen, describe every active control input and what it does. What elements on the screen will
  change in response to user input?
* Does the program respond to mouse input? What, exactly, does the mouse do?
* Does the program respond to keyboard input? How?
* What graphical assets will be used?
* Does the user have to do anything to install the program?

Your specification should **not** include the following types of information:

* The language you will use to create it.
* Names of any specific files in the project.
* How you will structure the classes, functions and code in your program.
* The name of any files or tools that you will use to design the program.



In this program, you can choose to translate ascii or unicode characters to binary and also from binary back to ascii or unicode.  
It's accessed by using http://runpython.com. There are a few screens that will show up, the first one having a prompt telling you what to type in to reach the screen which corresponds with what you want the program to do. There are many keyboard inputs which the program will respond to. If "a" is entered, the screen changes to allow you to translate ascii to binary. If "u" is entered, the screen changes to allow you to translate Unicode to binary. If "ba" is entered, the screen changes to allow you to translate binary to ascii. If "bu" is entered, the screen changes to allow you to translate binary to Unicode. If "q" is entered, the program is ended and "Goodbye!" appears on the screen.
