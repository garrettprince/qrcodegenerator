# QR Code Generator

## Table of Contents

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Set Up](#set-up)
- [Usage](#usage)
- [Project Status](#project_status)
- [Acknowledgements](#acknowledgements)

## General Information

Simple QR Code Generator based on [@piyushtiwari515](https://auth.geeksforgeeks.org/user/piyushtiwari515)'s QR generator [article on geeksforgeeks](https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/) with additional help from [@caryne](https://auth.geeksforgeeks.org/user/caryne)'s comment in the discussion section concerning the Image library.

Concept: I was trying to find a place to create custom QRs without the headache of signing up for an account or paying monthly (qr.io I'm looking at you) for what should be a simple security and exploration feature. Thus, using the tutorial mentioned above, I've managed to create a working program to do just that.

I may come back at a later time to make a site for others to use, mainly for those with no coding experience. I have no interest in creating users or charging for what should be a free service.

## Technologies Used

- Python 3.10.~
- QRCode Library v7.~ (now deprecated)
- Python Image Library

## Set Up

Must have Python 3, and the QR Code and Image libraries installed

Using homebrew to install Python:
```
brew install python3
```
Once Python is installed on your machine, from the terminal run:
```
pip3 install qrcode
pip3 install image
```

## Usage

1. Clone this repository via the terminal:
```
git clone https://github.com/garrettprince/qrcodegenerator.git
```
2. Follow comments in qr.py to change the data section to reflect your own destination upon scan and the image.save section for file naming conventions
3. In the terminal, run to execute code:
```
python3 qr.py
```
4. Output of .png will be created and stored at root level


## Project Status

Version 1: _complete as of 12/20/22_ 

*potential v2 with front end site for others to use, no plans or timeline yet*


## Acknowledgements

Credit to [@piyushtiwari515](https://auth.geeksforgeeks.org/user/piyushtiwari515) and [@caryne](https://auth.geeksforgeeks.org/user/caryne) for instructions and additional info from this [article on geeksforgeeks](https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/).
