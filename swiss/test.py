import paramiko

class ssh:
	def __init__(self):
		self.ssh_output=None
		self.ssh_error=None
		self.client=None
		self.host=192.168.0.103
		self.username="wolfflow"
		self.password="hhelibe1234"
		seld.timeout=10.0
		self.pkey="/home/wolfflow/.ssh/id_rsa"
		self.port=22

	def connect(self):
		"login to the server via client"
		print("connecting")
		self.client=paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
		if(self.password==''):
			private_key=paramiko.RSAKey.from_private_key_file(self.pkey)
			self.clien.connect(hostname=self.hostname,port=self.port,username=self.username,pkey=private_key,allow_agent=False,look_for_keys=False)
		else:
			self.client.connect(hostname=self.hostname,port=self.port,username=self.username,password=self.password,allow_agent=False,look_for_keys=False)
		
