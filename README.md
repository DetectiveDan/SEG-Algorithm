# SEG Algorithm
This project was influenced by Luhn's Algorithm. SEG was designed to create a 18 digit number, that is secured via a checksum. This is done by starting out with a 12 digit random number. More detail will be posted later in this file. 

### Prerequisites

For the Python version I have provided, you must use Python 3.6 with the CSV, Time, and Random packages. 

### Detailed Explanation of the Algorithm

First, twelve digits are generated at random. This will be broken into 3 segments. 

725542635809

                SEG1 . SEG2 . SEG3
								
                7255   4263   5809
                
Then the sum of each segment is found

                SEG1 . SEG2 . SEG3
								
                7255   4263   5809
								
                 19     15     22
                 
Now if the sum is more than 1 digit, we take the sum and remove the first digit. 

                SEG1 . SEG2 . SEG3
								
                7255   4263   5809
								
                 19     15     22
								 
                 9      5      2
                 
Finally to create SEG4, we take the sum of the entire 12 digits, and divide it by the length of the initial string (12)

                SEG1 . SEG2 . SEG3
								
                7255   4263   5809
								
                 19  +  15  +  22   =  56 (56/12 = 4)
								 
                 9      5      2
                 
Once we have SEG4, we add the total sum (56) to the end creating SEG5. The number is complete. 

                SEG1 . SEG2 . SEG3 . SEG4 . SEG5
								
                7255   4263   5809   9524    56

To check if the string is true, we take in the number and remove everything but the first 12 digits. We run that through the algorithm, and if the two numbers end up being the same the number is genuine. 

## Author

* **Daniel C Smith**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

