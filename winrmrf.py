#!/usr/bin/python3
from cmd import Cmd
import winrm as pywinrm
import argparse
from time import gmtime, strftime

parser = argparse.ArgumentParser(description="WinRM Shell")
parser.add_argument("host", metavar="", help="Host to connect to")
parser.add_argument("-u", "--username", metavar="", required="true", help="Username to authenticate as")
parser.add_argument("-p", "--password", metavar="", required="true", help="Password to authenticate with")
parser.add_argument("-d", "--domain", metavar="", help="The domain said creds will work on")
args = parser.parse_args()

def yellow(string):
	return '\033[1;33m%s\033[0m' % string

def banner():

	print()
	print(yellow(('█╗    ██╗██╗███╗   ██╗██████╗ ███╗   ███╗      ██████╗ ███████╗')))
	print(yellow(('█║    ██║██║████╗  ██║██╔══██╗████╗ ████║      ██╔══██╗██╔════╝')))
	print(yellow(('█║ █╗ ██║██║██╔██╗ ██║██████╔╝██╔████╔██║█████╗██████╔╝█████╗  ')))
	print(yellow(('█║███╗██║██║██║╚██╗██║██╔══██╗██║╚██╔╝██║╚════╝██╔══██╗██╔══╝  ')))
	print(yellow(('███╔███╔╝██║██║ ╚████║██║  ██║██║ ╚═╝ ██║      ██║  ██║██║     ')))
	print(yellow(('╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝     ')))
	print()

class Credentials:
	# Packages up the credentials nicely
	def __init__(self,username,password,domain):
		self.username = username
		self.password = password
		self.domain = domain
		if self.domain == None:
			self.domain = 'WORKGROUP'

class Connection:
	# Does all the connections
	def __init__(self,hostname,credentials):
		self.hostname = hostname
		self.username = credentials.username
		self.password = credentials.password
		self.domain = credentials.domain

	def session(self,args):
		conn = pywinrm.Session(self.hostname, auth=('{}\\{}'.format(self.domain, self.username), self.password), transport='ntlm', server_cert_validation='ignore')
		try:
			r = conn.run_cmd(args)
			print (r.std_out.decode('utf-8'))
			print (r.std_err.decode('utf-8'))
		except Exception as e:
			print()
			print(yellow(e))
			quit()

class Terminal(Cmd):
	start_time=strftime("%H:%M:%S", gmtime())
	prompt = '[%s] %s ' % (yellow(start_time),yellow('>>'))

	def shell(self,args):

		if args == 'quit' or args == 'exit':
			print("\nGoodbye.")
			quit()

		credentials = Credentials(username, password, domain)
		connection = Connection(hostname,credentials)
		connection.session(args)

	def default(self,args):
		self.shell(args)


banner()

hostname = args.host
username = args.username
password = args.password
domain = args.domain

print('Connecting to: '+yellow(hostname))
print('Using credentials: %s\%s:%s' % (yellow(domain),yellow(username),yellow(password)))

try:
	term = Terminal()
	term.cmdloop()
except KeyboardInterrupt:
	print('\n\rDetected CTRL+C!')
	quit()

