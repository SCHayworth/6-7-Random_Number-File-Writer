# 6-7-Random_Number-File-Writer
 Writes a user-supplied amount of random integers between 1-500 to a file.

## Scope
Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold.

*Hint:* Make sure to use a for loop, and don't forget to convert the int to a str before writing to the file.

## Pseudocode
### Main logic
START
  IMPORT math module
  OPEN a file called random.txt in append mode
  INPUT amount of numbers to write to the file
  FOR each number in amount
    CALL the random number method to generate an integer between 1 and 500
    CONVERT the integer to a string
    WRITE the string to random.txt
  ENDFOR
  CLOSE random.txt
END
