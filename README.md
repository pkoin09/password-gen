# PASSWORD GENERATOR WITH QR CODE

## [Video Demo](https://youtu.be/2p_tIesIkI0)

#### Description:

This Python program provides a solution for generating secure random passwords of any desired length. Along with generating the password, the program creates scannable QR code that corresponds to the generated password. For convenience, the password and QR code can be saved as a PDF file, making it easy to store and share. Moreover, the program offers a feature that allows users to seamlessly send the generated password and QR code PDF via email, using the sender's (the person who generated the password) Gmail account.

The program will create a strong and secure password, the longer the password, the more secure it will be. You can use the generated password for any app that requires a password. A good example would be the guest password to your wi-fi. This can be posted in the guest area or in your home for easy access to guests.

#### Install

Install the dependencies by running (python3 or python will work)

```sh
python3 install -r requirements.txt
```

#### Usage

**To use this project, follow these steps:**

1. In the terminal, enter and execute the following command:

```sh
python3 project.py
```

2. When prompted, enter the desired length for your password.
3. Choose whether or not you want to change the default file name for the QR code. If you choose not to change it, the default name "password_qr" will be used. If you choose to change it, you will be prompted to type a file name of your choosing.
4. The generated password will be displayed on the terminal. Copy and save it for future use.
5. The QR code will be saved in the root (project) folder as a PDF file and a PNG file.
6. You can also choose to send the QR code via email. If you choose to do this, you will be prompted to enter your
   1. Gmail account,
   2. Gmail app-specific password, and
   3. the recipient's email address.
      See Google's Account Help page to learn more about [app specific passwords](https://support.google.com/accounts/answer/185833?hl=en&sjid=12577493574589292708-NA)

**Steps to create an app specific password:**

1. Go to [Google Account](https://www.google.com/account/about/), one way to do this is to sign in your Gmail account, click on your profile picture located at the top right corner in Gmail and then select 'Manage your Google Account'.
2. Select Security.
3. Under "How you sign in to Google," select 2-Step Verification.
4. At the bottom of the page, select App passwords.
5. Enter a name that helps you remember where you’ll use the app password.
6. Select Generate.
7. To enter the app password, follow the instructions on your screen. The app password is the 16-character code that generates on your device.
8. Select Done.

#### Testing

Testing is the process of evaluating and verifying that code does what it is supposed to do. It is an essential part of the software development process. The project contains a pytest unit test. The test for this project is located in the root folder. It in a Python file called 'test_project.py'. It contains a number of tests that verify the functionality of the 'project.py' script.

To run a test, execute:

```sh
pytest test_project.py
```

#### License

This project is licensed under the MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

#### Ackowledgements

- [pyqrcode](https://pypi.org/project/PyQRCode/)
- [pyPNG](https://pypi.org/project/pypng/)
- [reportlab](https://pypi.org/project/reportlab/)
- [getpass4](https://pypi.org/project/getpass4/)
- [python-secrets](https://pypi.org/project/python-secrets/)
