# Low Price Product Alert

Low Price Alert app

Self messaging app to never miss the best deals for the product of your choice. 

I used a Razer Blade on Amazon as my product tester.

This application is installable locally in desktop.

## Built With

- Python

## Getting Started

To get a local copy up and running follow these simple example steps.

### Setup

- Open the console
- Download or git clone https://github.com/AllanAscencio/low_price_product_alert
- cd low_price_product_alert

Install requests:

Linux

```
  $ pip install requests 
```

In Linux, If you require root permission, use ‘sudo’. Alternatively, you can also use pipenv to install requests library, where pipenv is used to automatically manage the packages during the course of installation/uninstallation.

```
$ pip install pipenv
```

Windows

The Windows users need to navigate to the Python directory, and then install the request module as follows:

```
> python -m pip install requests
```

Mac
For MacOS, install Python through ‘Home Brew’. Thereafter, install pip and request module (which is the same as Linux installation process.)

### SMPTLIB

smptlib is part of python's standard library, so you do not have to install it. Therefor the only step you need to take before writing the code to use it, is to

```
  import smptlib
```

Then I used the following standard block of code to connect and send messages:

```
with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PW)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="youremail@gmail.com",
            msg=f"Price is below $2800 USD, you should buy NOW!\n{URL}"
        )

```
If you have issues and keep getting this error:
![image](https://user-images.githubusercontent.com/103056674/210819707-88eaf199-bb01-459d-b6be-98afe6f38760.png)

1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"

Below are steps specific to users sending email from Gmail and Yahoo addresses as outlined in the Birthday Wisher on Day 32.


2. Turn on 2-Step Verification for your email under the Security settings for your account. For example, Manage Your Google Account -> Security.

![image](https://user-images.githubusercontent.com/103056674/210819918-c0c1e85c-9ea0-461e-8e34-dbba3fc0e2d7.png)


3. Add an App Password under your email settings. Select "Other" from the drop-down settings and choose a password. Use this app password in your Python code.

![image](https://user-images.githubusercontent.com/103056674/210819948-e958b4af-1878-4db5-bb93-5ec0bcdb29cc.png)


4. Add a port number by changing your code to this:

```
smtplib.SMTP("smtp.gmail.com", port=587)
```

if you need further documentation for smptlib https://docs.python.org/3/library/smtplib.html

Author
👤 **Allan Ascencio**

- [Github](https://github.com/AllanAscencio)
- [Linkedin](https://www.linkedin.com/in/gianfranco-allan)


## Considerations

- Remember to change the URL in the code, to the specific URL of the item you want from the amazon wepage
- Remember to change the price amount you want the alert to be activated

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## Show your support

Give a ⭐️ if you like this project!

## 📝 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.
