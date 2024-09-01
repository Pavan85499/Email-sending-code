# (simple Mail transfer protocol) -- for email sending use lib - smtplib
import smtplib   

#add diff protocols based on requirmet ex- https/ftp/udp/tcp..... for msg snding
# import httplib2
# import ftplib


server = smtplib.SMTP('smtp.gmail.com',587)

# creating server to start transport layer security (tls)
server.starttls()

# sendind from
server.login('ABCD123@gmail.com', '6546_gfhrthr')

# sending To
server.sendmail('ABCD!@gmail.com','Pavan121@gmail.com','Mail sent')

# just displaying message for success
print('Mail sent')