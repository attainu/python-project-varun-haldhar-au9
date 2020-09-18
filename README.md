As we all know, the Bitcoin price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, you can run this script to stay updated.

# Bitcoin Price Notification

This is the Bitcoin Price Notification Python Script Package, this script will help you to get notified for the regular updates of bitcoin price on Telegram and IFTTT app notifications. This script will notify you whenever the Bitcoin price goes lower then threshold(You can adjust this according to your needs).



**Table of Content:**

1. [ Description. ](#desc)
2. [Prerequisite](#pre)
3. [Installation](#ins)
4. [Usage](#usg)
5. [Project Status](#pro)
6. [Contribute](#con)
7. [License](#lic)

<a name="desc"></a>

## Description

As we all know, Bitcoin price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, let’s make a Python app to do the work for you.

- For this project we are going to use the popular automation website IFTTT.
- We’re going to create two IFTTT applets:
  - One for emergency notification when Bitcoin price falls under a certain threshold; and
  - another for regular [Telegram](https://t.me/bitcoin_price_notification) updates on the Bitcoin price.
- These will be triggered by our python app which will consume the data from the Coinmaretcap.com.
- An IFTTT applet is composed of two parts: a trigger and an action.
  - The trigger will be a webhook service provided by IFTTT. You can think of webhooks as “user-defined HTTP callbacks”.
  - Our Python app will make an HTTP request to the webhook URL which will trigger an action.


<a name="pre"></a>
## Prerequisite

Must have one of the following app installed and/or must join or follow one of the following accounts

- Install the IFTTT App to receive the notifications
- Download Telegram App and join the [Telegram channel](https://t.me/bitcoin_price_notification).

<a name="ins"></a>
## Installation

1. Clone this repository
2. Create your virtual environment
3. Install all requirements
4. Run the bot  `bitcoin-price-notification.py`

<a name="usg"></a>
## Usage

This script gives the price of one BTC in INR. To receive notification on IFTTT, you must have installed the IFTTT mobile app. To receive notification on Telegram, you must have Telegram installed on your device and should have joined [this channel](https://t.me/bitcoin_price_notification) .

**Run the script to get instant Bitcoin Price Notification.**

`bitcoin-price-notification.py`

<a name="pro"></a>
## Project status

This script is ready to use you can simply clone the repo and use it, but the script is still under development and in upcoming days you can see more features, very unique designs, with easy to use, and understandable UI.

<a name="con"></a>
## Contribute

**Contributions are always welcome!**

Please ensure your pull request adheres to the following guidelines:

- Alphabetize your entry.
- Suggested READMEs should be beautiful or stand out in some way.
- Make an individual pull request for each suggestion.
- Keep descriptions short and simple, but descriptive.
- Start the description with a capital and end with a full stop/period.
- Check your spelling and grammar.
- Make sure your text editor is set to remove trailing whitespace.
- Use the `#readme` anchor for GitHub READMEs to link them directly

Thank you for your suggestions!

<a name="lic"></a>
## License

[MIT](https://choosealicense.com/licenses/mit/)