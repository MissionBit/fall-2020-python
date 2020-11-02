# SMS Sender

## How to use

1. Copy [sms.py](sms.py) to your project
1. Update `EMAIL`, `PASSWORD`, `PHONE_NUMBER`, and `CARRIER`
1. To send a text:
   ```python
   import sms

   # your code here...

   sms.send_text('your message here')
   ```

## Caveats

1. If you use Gmail, you'll need to visit https://myaccount.google.com/lesssecureapps and turn on access for less secure apps
1. If your cell phone carrier isn't listed in the script, add the corresponding entry from this table: https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account

## How it works

Every cell phone carrier has a "gateway address" which can be used to send a text message (via email) to any cell phone number on that carrier's network. All this script does is log in to your email server and send an email to your phone number using your carrier's gateway address.

## Example project

[inspirational_quote_texter.py](inspirational_quote_texter.py): A script that texts you a random inspirational quote once a day.
