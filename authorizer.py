import smtplib
import pickle
import random
import string
from email.mime.text import MIMEText

class Authorizer:
  BOT_MAIL = 'tjdgnsqn133@gmail.com'
  BOT_PASSWORD = open('bot_password.txt', 'r').readline()

  def __init__(self, email):
    self.email = email

  def send_mail(self):
    code = self.generate_code()
    self.save_the_code(code)
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(self.BOT_MAIL, self.BOT_PASSWORD)
    msg = MIMEText(code)
    msg['Subject'] = 'SERIKU 의 인증 코드입니다.'
    smtp.sendmail(self.BOT_MAIL, self.email, msg.as_string())
    smtp.quit()

  def generate_code(self):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(6))

  def save_the_code(self, code):
    codes = pickle.load(self.codes_file('rb'))
    codes[self.email] = code
    pickle.dump(codes, self.codes_file('wb'))

  def codes_file(self, mode):
    return open('codes.txt', mode)

  def authorize(self, code):
    codes = pickle.load(self.codes_file('rb'))
    result = codes.get(self.email) == code
    pickle.dump(codes, self.codes_file('wb'))
    return result

a = Authorizer('tjdgnsqn133@gmail.com')
# print(a.send_mail())
# print(a.authorize('NZJ31A'))
