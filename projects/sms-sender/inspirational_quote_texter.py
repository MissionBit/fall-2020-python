import requests
import time
import sms

def main():
  while True:
    print('Retrieving random quote...')
    r = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    if not r.ok:
      raise RuntimeError(f'Request to quotes API failed: {r.text}')
    quote = r.json()
    print(f'Received quote {quote} from API; sending text message...')
    sms.send_text('"{}"\n\n- {}'.format(quote['quoteText'], quote['quoteAuthor']))
    print('Sent text message.')
    time.sleep(60 * 60 * 24)  # Sleep for one day

if __name__ == '__main__':
  main()
