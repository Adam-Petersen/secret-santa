
import smtplib
import json
from cryptography.fernet import Fernet
from person import *
from graph import * 
from helpers import *

with open("cfg.json", "r") as cfg_file:
  cfg_str = cfg_file.read()
with open("key.txt", "rb") as key_file:
  key = key_file.read()

cfg = json.loads(cfg_str)
people = init_people(cfg["people"])
G = Graph(people)
success = G.assign_targets(G.people[0])

if not success:
  raise "Algorithm failed"
if not validate(people):
  raise "Validation failed"

send_emails = input("Assignments created. Start sending emails? Y/N: ")
if not send_emails.lower() == "y" and not send_emails.lower() == "yes":
  print("Exiting...")
  quit()

f = Fernet(key)
gmail_user = f.decrypt(cfg["sender_address"].encode()).decode()
gmail_password = f.decrypt(cfg["sender_password"].encode()).decode()

for person in people:
  to = person.email
  subject = cfg["email_subject"]
  body = cfg["email_body"].replace("{person}", person.name).replace("{target}", person.target.name)
  email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (gmail_user, to, subject, body)

  try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, email_text)
    server.close()

    print('Email sent to ' + person.name + '!')
  except Exception as ex:  
    print('Something went wrong...')
    print(str(ex))

  