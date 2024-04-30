# PASSWORD GENERATOR WITH QR CODE


#### Video Demo: https://youtu.be/2p_tIesIkI0

#### Description:

This Python program provides a solution for generating secure random passwords of any desired length. Along with generating the password, the program creates scannable QR code that corresponds to the generated password. For convenience, the password and QR code can be saved as a PDF file, making it easy to store and share. Moreover, the program offers a feature that allows users to seamlessly send the generated password and QR code PDF via email, using the sender's (the person who generated the password) Gmail account.

The program will create a strong and secure password, the longer the password, the more secure it will be. You can use the generated password for any app that requires a password. A good example would be the guest password to your wi-fi. This can be posted in the guest area or in your home for easy access to guests.

The code comes equipped with a handy constructor method called `send_mail` within the `Mailer` class. With this method, you can effortlessly send the generated QR code in PDF to any recipient's email address. Simply provide the sender's Gmail address, the sender's Gmail app-specific password, the receiver's email address, and the QR code PDF file as arguments. The `smtplib` library takes care of the mailing process behind the scenes. Now you can share those awesome QR codes with your friends, colleagues, or anyone else who needs a dose of high-tech awesomeness in their inbox!

In addition to the above, these four functions are the core of the program and serve as its backbone. Let's take a closer look at each function and see how it contributes to the program's overall functionality:

1. `Main` function: This function is the brain of the program. It controls the overall flow of the program and handles user interaction. It prompts the user for input, generates passwords, creates QR codes, and saves them as PDFs. Additionally, it prints information to keep the user informed throughout the process.

2. `Generate_password` function: This function generates strong and secure passwords of any desired length. Security is a top priority for the program, and this function ensures that all passwords generated are secure and difficult to crack.

3. `Generate_qr` function: This function is responsible for creating QR codes. It uses the pyqrcode library to generate a QR code that encapsulates the generated password. This function is essential for the program's functionality, as it allows users to easily share their passwords with others.

4. `Save_as_pdf` function: This function plays a vital role in the process by ensuring that the QR code is saved as a PDF file. This feature provides users with multiple options for sharing and storing their passwords, including printing, sharing, or storing the PDF file for safekeeping.
Overall, the program's four functions work seamlessly together to provide users with secure and easily accessible passwords. They also offer a user-friendly interface and provide clear feedback throughout the process.

P.S.
Although password input is masked, it would be wise to use Gmail's app-specific password as password input.

Steps:
1. Go to [Google Account](https://www.google.com/account/about/) or from your Gmail account, click your profile pic (top right) and click 'Manage your Google Account'
   a) If you chose google account, click "Privacy tools" tab.

2. Select Security

3. Under "How you sign in to Google" section, click "2-Step Verification". It must be "On" or turned On to proceed.
    Optional steps if turned off.
    a) If turned off, click the blue "Get started" button to start the process.
    b) Enter your phone number and choose how to get the codes. You can either
        i) Get the codes through text msg or by phone call.
        ii) Use a security key
        iii) Get a Google prompt on your phone whereby you hit "Yes" to sign in or "No" to reject. Note that you must be signed in to the Google Account on a phone for this option.
    c) click next and depending on the choice above, you will get a prompt. follow the steps to complete.
    d) If code, security key or phone prompt was successful, last step will ask you click "Turn on" and redirected to the security page.

4. At the bottom of the page, click App passwords.

5. Under "Select app" options, click "Other (Custom name)"

6. Type a name of your choosing e.g "Python QR Generator" and click "Generate" button.

This is the app-password you will enter when prompted in the terminal. Its only shown once you might want to write it down for testing. Trash it if it's not needed anymore.


#### Prerequisites

Make sure the following dependencies are installed for python 3.x:

- python-secrets 23.4.2
- PyQRCode 1.2.1
- pypng 0.20220715.0
- reportlab 4.0.4
- getpass4 0.0.14.1

#### Dependency install

To install the above libraries, you can opt to install one at a time, or multiple separated by a space (no commas).
use the code below depending on your `pip` setup.

```sh
pip3 install [package]
```
or
```sh
pip install [package]
```

#### Usage

To use this project, follow these steps:

1. Run the project.py script in your terminal.

2. When prompted, enter the desired length for your password.

3. Choose whether or not you want to change the default file name for the QR code. If you choose not to change it, the default name "password_qr" will be used. If you choose to change it, you will be prompted to type a file name of your choosing.

4. The generated password will be displayed on the terminal. Copy and save it for future use.

5. The QR code will be saved in the root (project) folder as a PDF file and a PNG file.

6. You can also choose to send the QR code PDF via email. If you choose to do this, you will be prompted to enter your Gmail account, Gmail app-specific password, and the recipient's email address.

see Google's Account Help on [app specific passwords](https://support.google.com/accounts/answer/185833?hl=en&sjid=12577493574589292708-NA)


#### Testing

Testing is the process of evaluating and verifying that code does what it is supposed to do. It is an essential part of the software development process. Included in the project is a unit pytest.

pytest is a unit testing framework, which means it provides a set of tools and features that make it easier to write and run tests in Python. Testing is an important part of the software development process. It helps to ensure that the code is of high quality. By writing tests, developers can catch bugs early in the development process. This can save time and money
The test for this project is located in the root folder. It is a Python file called `test_project.py`. It contains a number of tests that verify the functionality of the `project.py` script.

To run a test, type:

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