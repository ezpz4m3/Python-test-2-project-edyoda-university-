
class quiz_project:
	topics=[]
	questions={}
	options={}
	answers={}
	difficulty_level={}
	responses={}
	student_data=[]
	total=0
	scores={}

	def __init__(self):
		self.menu()

	def menu(self):
		print("Please enter your role:\n1:Admin\n2:Student\n3.Exit\n>>")
		n=int(input())
		if n==1:
			self.Admin()
		elif n==2:
			if quiz_project.questions!={}:
				self.Student()
			else:
				print("\n!!!Quiz has not been generated yet!!!\n")
				self.menu()
		elif n==3:
			return None
		else:
			print("Choose a valid option\n")
			self.menu()

	def Admin(self):
		username=input("Please enter the username: ")
		password=input("Please enter the password: ")
		if username=='admin@super' and password=='admin@12345':
			self.Adminmenu()
		else:
			print("Enter valid username\n")
			self.Admin()

	def Adminmenu(self):
		print("\n1.Add questions\n2.Display questions\n3.Delete quiz\n4.Scoreboard\n5.Exit\n>>")
		n=int(input())
		if n==1:
			self.Addques()
		elif n==2:
			self.display()
		elif n==3:
			self.clear_quiz()
		elif n==4:
			self.scoreboard()
		elif n==5:
			self.menu()
		else:
			print("Enter valid choice\n")
			self.Adminmenu()

	def clear_quiz(self):
		quiz_project.topics=[]
		quiz_project.questions={}
		quiz_project.options={}
		quiz_project.answers={}
		quiz_project.difficulty_level={}
		quiz_project.responses={}
		quiz_project.student_data=[]
		quiz_project.total=0
		print("The quiz has been deleted")
		self.Adminmenu()

	def scoreboard(self):
		print("Name".ljust(20),"Email".ljust(20),"Percentage")
		for i in quiz_project.student_data:
			print((i[0]).ljust(20),(i[1]).ljust(20),quiz_project.scores[i[0]])
		self.Adminmenu()


	def Addques(self):
		a=input("Pleae enter the question:\n")
		x=input("The question topic: ")
		c=int(input("Choose the difficulty level\n1-Easy  2-Medium  3-Hard\nChoose (1,2,3) >> "))
		while(c>3):
			c=int(input("Choose the difficulty level\n1-Easy  2-Medium  3-Hard\nChoose (1,2,3) >> "))
		b=x.lower()
		if b not in quiz_project.topics:
			quiz_project.topics.append(b)
			quiz_project.questions[b]=[]
			quiz_project.options[b]=[]
			quiz_project.answers[b]=[]
			quiz_project.difficulty_level[b]=[]

		quiz_project.questions[b].append(a)

		if c==1:
			quiz_project.difficulty_level[b].append(5)
			quiz_project.total+=5
		elif c==2:
			quiz_project.difficulty_level[b].append(10)
			quiz_project.total+=10
		elif c==3:
			quiz_project.difficulty_level[b].append(20)
			quiz_project.total+=20

		arr=[]
		print("The options are:")
		for i in range (1,5):
			print(i,":",end='')
			arr.append(input())
		quiz_project.options[b].append(arr)

		print("The correct answer options are:\n>>")
		quiz_project.answers[b].append(int(input()))

		if input("Would you like to add more questions? Yes(Y)/No(N)") in 'Yy':
			self.Addques()
		else:
			self.Adminmenu()

	def total_marks(self,name):
		if name in quiz_project.responses:
			sum1=0
			for i in quiz_project.topics:
				sum1+=sum(quiz_project.responses[name][i])
			return sum1
		else:
			print("!!!Name doesnt exist in the list!!!")

	def Student(self):
		self.stdname=input("Enter your name:")
		self.stdmail=input("Enter your email:")
		quiz_project.student_data.append([self.stdname,self.stdmail])
		quiz_project.responses[self.stdname]={}
		print("-------------The Test Is Starting--------------\nEasy question is for 5 marks\nMedium question is for 10 marks\nHard question is for 20 marks\n")
		if input("Press any  key to start>>")!='':
			for i in range (len(quiz_project.questions)):
				a=quiz_project.topics[i]
				quiz_project.responses[self.stdname][a]=[]
				print("____",a.upper(),"____")
				for j in range(len(quiz_project.questions[a])):
					print("\n",quiz_project.questions[a][j])
					for k in range(0,4):
						print(k+1,":",quiz_project.options[a][j][k])
					check=int(input("Enter the option:"))
					if check==quiz_project.answers[a][j]:
						quiz_project.responses[self.stdname][a].append(quiz_project.difficulty_level[a][j])
					else:
						quiz_project.responses[self.stdname][a].append(0)
		print("\n\nCORRECT ANSWERS ARE\n")
		for i in range (len(quiz_project.questions)):
			a=quiz_project.topics[i]
			print("\n____",a.upper(),"____\n")
			for j in range(len(quiz_project.questions[a])):
				print("\n",quiz_project.questions[a][j])
				for k in range(0,4):
					print(k+1,":",quiz_project.options[a][j][k])
				print("CORRECT ANSWER>>",quiz_project.answers[a][j],"\n")


		
		res=self.total_marks(self.stdname)
		print(self.stdname,"your score is",res,"/",quiz_project.total,"\n\n")
		quiz_project.scores[self.stdname]=res/quiz_project.total*100
		self.menu()

	def display(self):
		for i in range (len(quiz_project.questions)):
			a=quiz_project.topics[i]
			print("\n____",a.upper(),"____\n")
			for j in range(len(quiz_project.questions[a])):
				print("\n",quiz_project.questions[a][j])
				for k in range(0,4):
					print(k+1,":",quiz_project.options[a][j][k])
		self.Adminmenu()
		

start=quiz_project()