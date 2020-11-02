import smtplib
import ssl

EMAIL = 'email@gmail.com'
PASSWORD = 'your-email-password-here'
PHONE_NUMBER = '4085555555'  # Your 10-digit phone number
CARRIER = 'Google Fi'  # Enter one of the carriers below

ADDRESS_BY_CARRIER = {
  'AT&T': '@txt.att.net',
  'T-Mobile': '@tmomail.net',
  'Verizon': '@vtext.com',
  'Sprint': '@messaging.sprintpcs.com',
  'Google Fi': '@msg.fi.google.com',
}

def _get_address(carrier):
  if carrier not in ADDRESS_BY_CARRIER:
    raise RuntimeError(
      f'Unknown carrier "{carrier}". Please choose one of: {ADDRESS_BY_CARRIER.keys()}')
  return ADDRESS_BY_CARRIER[carrier]

def _get_args(email):
  if 'gmail' in email:
    return { 'host': 'smtp.gmail.com', 'port': 465, 'context': ssl.create_default_context() }
  if 'yahoo' in email:
    return { 'host': 'smtp.mail.yahoo.com', 'port': 587 }
  if 'hotmail' in email:
    return { 'host': 'smtp.live.com', 'port': 587 }
  raise RuntimeError(f'Unknown SMTP args for email "{email}"')

def send_text(message):
  with smtplib.SMTP_SSL(**_get_args(EMAIL)) as server:
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, PHONE_NUMBER + _get_address(CARRIER), message)
