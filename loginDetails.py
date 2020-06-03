# this is a file that will be imported.



#username = "1181302651"
#password = "mOHAN1#2$3_"



class LoginDetails():
	# this are static variables
	ocmsURL = "https://cms.mmu.edu.my/psp/csprd/EMPLOYEE/HRMS/h/?tab=DEFAULT&cmd=login&errorCode=106&languageCd=ENG"
	username = 'Empty'
	password = 'Empty'

	def __init__ (self):
		print("loading credentials")

	@staticmethod
	def login_id_pass():
		LoginDetails.username = input('Username : ') # dont use () at the end of class as that is for instance varible , or object
		LoginDetails.password = input('Password : ')






if __name__ == "loginDetails":
	'''
	   does this work ?
	'''


