# OTP-verification-using-python
This repository contains the source code for generating OTP to email using python.


1.Generate OTP:

A random 6-digit OTP is generated using the random module.

2.User Input:

The user is prompted to enter his/her name and email ID.

3.Email Verification:

The entered email ID is verified to ensure it follows a basic email format.
The verification includes checking if the email domain is either "gmail", "hotmail", "yahoo", or "outlook", and if it has a valid top-level domain (".com", ".in", ".org", ".edu", ".co.in").
If the email is invalid, the user is prompted to enter a correct email ID.

4.Generate and Send OTP to Email:

A new OTP is generated.
A new email is composed with the generated OTP and sent to the user.

5.OTP Verification:

The user is prompted to enter the OTP received in their email.
If the entered OTP matches the generated OTP, the verification is successful.
If the OTP is incorrect, the user is prompted to enter it again, and the process is repeated until the correct OTP is entered.

6.Resend OTP:

If the user wants to resend the OTP, they can choose to do so. This involves generating a new OTP and sending a new email.

8.Final OTP Verification:

After the user successfully verifies the OTP, the script prints "OTP verified".
If the OTP is still incorrect after retries, the script prompts the user to enter a new email ID or resend the OTP to the same email.
