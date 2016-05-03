#!/usr/bin/env python
# encoding: UTF-8

import sys
from smtplib import SMTP_SSL as SMTP
from time import sleep
import config


# This is a sneak preview of the hell I have in store for you :)


def send_email(from_addr, to_addr, body_text):
		"""
		Send an Email
		"""

		msg_body = ""
		parts = ["From: %s" % config.from_addr,
				"To: %s" % config.to_addr,
				"MIME-Version: 1.0",
				"Content-type: text/html",
				"Subject: %s" % subject,
				"",
				body_text
				, "\r\n"]
		msg_body = "\r\n".join(parts)
		server = SMTP(config.host, 465)
		# server.set_debuglevel(1)
		server.ehlo()
		server.login(config.usrnme,config.pswd)
		server.sendmail(from_addr, to_addr, msg_body)
		server.quit()
		sleep(2)
		
body_text = 'Hey there! <br/><br/> Next time someone asks you to remove them from an email list<br/><br/> You will remember this moment <br/> Now remove %s from your email list!<br/><br/><br/> Regards,<br/><br/> Pissed off Developer<br/> [From: Address]' % config.from_addr

while True:	
	for i in range(len(config.victims)):
		subject 	= "Career Inquiry"
		#config.to_addr = config.victims[i]
		send_email(config.from_addr, [config.to_addr], body_text)
		print "Sent Message To " + config.victims[i]

			

