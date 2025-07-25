Indian Currency Number Formatter

================================



Description:

------------

Problem: Convert number into a comma separated Indian currency format

In Indian numbering system the terms used are different from what is used in the western numbering system. 

Terms like Lakh to represent one hundred thousand and Crore to represent 10 Million.

Write code that takes as input a floating point number and returns an indian number string representation with commas separating the digits.

Eg: 123456.7891 should return 1,23,456.7891





\## Features

\- Handles positive and negative numbers

\- Supports decimal/fractional parts with exact precision using Python's `decimal` module

\- Correctly formats large numbers with lakhs and crores separators

\- Easily testable with included unit tests



\## Example

| Input                | Output               |

|----------------------|----------------------|

| `123456.7891`        | `1,23,456.7891`      |

| `1234567890.12`      | `1,23,45,67,890.12`  |

| `-9876543.21`        | `-98,76,543.21`      |



\## Usage

1\. Include the function `indian\_currency\_format(number)` in your Python project.

2\. Call the function with a number (int, float, Decimal, or string) as input.

3\. The function returns a formatted string.



Example code snippet:



formatted\_str = indian\_currency\_format("1234567890.12")

print(formatted\_str) # Output: 1,23,45,67,890.12



text



\## Testing

\- The project includes a unittest test file `test\_indian\_currency\_format.py`.

\- To run the tests, use the command:

&nbsp; 

python -m unittest test\_indian\_currency\_format.py



text





\## Requirements

\- Python 3.x (tested on Python 3.7+)

\- No external dependencies



\## Author

Nandala Bhanadithya





