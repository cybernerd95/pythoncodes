import pymysql
import matplotlib.pyplot as plt


def Patient_Management():
    while True:
        print('## Patient Management Programm  ##')
        print ('1. Add a new patient details')
        print ('2. Search a patient details')
        print ('3. Update a patient details')
        print ('4. Delete patient details ')
        print ('5. Display all patient details')
        print ('6. Show graph  details')
        print ('7. Exit ')
        choice=int(input('Enter your choice'))

        if choice==1:
            print('Add new patient details')
            insertnewpatientdetails()
        elif choice==2:
            print('Search patent details ')
            searchpatient()
        elif choice==3:
            print('Update patient details')
            updatepatient()
        elif choice==4:
            print('Delete patient details')
            deletepatient()
        elif choice==5:
            print('Displaying all patient details')
            displaypatientdetails()
        elif choice==6:
            print("Showing graph")
            patientgraph()
        elif choice==7:
            break
        else:
            print('Inavaid Choice entered please enter a valid choice form the given above')
def insertnewpatientdetails():
    A = pymysql.connect(host="localhost",user="root",password="manager",database="hospital")
    AC=A.cursor()
    print('Adding new patient details ')
    pid=int(input("Enter patient ID: "))
    pname=str(input("Enter patient name"))
    page=int(input("Enter patient age"))
    pgender=str(input("Enter patient gender"))
    pheight=int(input("Enter patient height"))
    pweight=int(input("Enter patient weight"))
    pbloodgp=str(input("Enter patient Blood Group"))
    pphno=int(input("Enter patient Phone number"))
    pemail=str(input("Enter patient email"))
    paddress=str(input("Enter patient address"))
    pDOB=str(input("Enter patient Date of Birth(YY/DD/MM)"))
    pdiagnosis=str(input("Enter patient Diagnosis"))
    Sql_command_1 = 'insert into patient_details values('+str(pid)+',"'+pname+'",'+str(page)+',"'+pgender+'",'+str(pheight)+','+str(pweight)+',"'+pbloodgp+'",'+str(pphno)+',"'+pemail+'","'+paddress+'","'+pDOB+'","'+pdiagnosis+'",)'
    AC.execute(Sql_command_1)
    print('Patient details have been updated sucessfully')

def searchpatient():
	A = pymysql.connect(host="localhost",user="root",password="manager",database="hospital")
	SC=A.cursor()#SC= scearch cursor 
	print('Searching patient details')
	PI=int(input('Enter patient ID to search'))
	Sql_command_2='select*from patient_details where pid= '+str(PI)+''
	SC.execute(Sql_command_2)
	row=SC.rowcount
	if(row>0):
		data=SC.fetchmany(1)
		for i in data:
			print('pid=',i[0])
			print('pname=',i[1])
			print('pDOB=',i[10])
			print('page=',i[2])
			print('pgender=',i[3])
			print('pheight=',i[4])
			print('pweight=',i[5])
			print('pbloodgp=',i[6])
			print('pdiagnosis=',i[11])
			print('pphno=',i[7])
			print('pemail=',i[8])
			print('paddress=',i[9])
		else:
			print('Patient ID not found ')
		A.commit()
def updatepatient():
	A = pymysql.connect(host="localhost",user="root",password="manager",database="hospital")
	UC = A.crusor()
	print('Updating patiend details')
	PI=int(intput('Enter patients ID for updating'))
	Sql_command_3='select*from patient_details where pid='+srt(PI)+''
	UC.execute(Sql_command_3)
	row=UC.rowcount
	if(row>0):
		data=UC.fetchmany(1)
		for i in data:
			print('pid=',i[0])
			print('pname=',i[1])
			print('pDOB=',i[10])
			print('page=',i[2])
			print('pgender=',i[3])
			print('pheight=',i[4])
			print('pweight=',i[5])
			print('pbloodgp=',i[6])
			print('pdiagnosis=',i[11])
			print('pphno=',i[7])
			print('pemail=',i[8])
			print('paddress=',i[9])
		npid=int(input('enter patients new ID ='))
		npname=int(input('enter patients new name ='))
		npage=int(input('enter patients new age  ='))	
		npgender=int(input('enter patients new gender ='))
		npheight=int(input('enter patients new height ='))
		npweight=int(input('enter patients new weight ='))
		npbloodg=int(input('enter patients new blood Group ='))
		npphno=int(input('enter patients new Phone number ='))
		npemail=int(input('enter patients new Email ='))
		npaddress=int(input('enter patients new address ='))
		npDOB=int(input('enter patients new Date of Birth ='))
		npdiagnosis=int(input('enter patients new Diagnosis ='))
		Sql_command_4='update patient_details set pid=('+str(npid)+',pname="'+npname+'",page='+str(npage)+',pgender="'+npgender+'",pheight='+str(npheight)+',pweight='+str(npweight)+',pbloodgp="'+npbloodgp+'",pphno='+str(npphno)+',pemail="'+npemail+'",paddress="'+npaddress+'",pDOB="'+npDOB+'",pdiagnosis="'+pdiagnosis+'",'
		UC.execute(Sql_command_4)
		print('Patientid',PI,'Details updated')
	else:
		print('patient ID ',PI,'not found')
		A.commit()

def deletepatient():
                A=pymysql.connect(host="localhost",user="root",password="manager",database="hospital")
                DC=A.cursor()
                PI=int(input('Enter patientID to delete patient details'))
                Sql_command_4='select*from patient_details where pid='+str(PI)+''
                DC.execute(Sql_command_4)
                rowDC.rowcount
                if(row>0):
                                data=DC.fetchmany(1)
                                print('The details of the patient are ')
                                for i in data:
                                                print('pid=',i,[0])
                                                print('pname=',i[1])
                                                print('pDOB=',i[10])
                                                print('page=',i[2])
                                                print('pgender=',i[3])
                                                print('pheight=',i[4])
                                                print('pweight=',i[5])
                                                print('pbloodgp=',i[6])
                                                print('pdiagnosis=',i[11])
                                                print('pphno=',i[7])
                                                print('pemail=',i[8])
                                                print('paddress=',i[9])
                                                d=int(input('are you sure you want to delete the following patient details ? to confirm pls press 1 '))
                                                if(d==1):
                                                                Sql_command_5='delete from patient_details where pid='+str(PI)+''
                                                                DC.execute(Sql_command_5)
                                                                print('Patient details deleted ')
                                                                A.commit()
                                                else:
                                                                print('Patient id ',PI,'not found ')

def displaypatientdetails():
	A = pymysql.connect(host="localhost",user="root",password="manager",database="hospital")
	Dic=A.cursor()
	Sql_command_6='select*from patient_details'
	Dic.execute(Sql_command_6)
	for i in Dic.fetchall():
		print('pid=',i,[0])
		print('pname=',i[1])
		print('pDOB=',i[10])
		print('page=',i[2])
		print('pgender=',i[3])
		print('pheight=',i[4])
		print('pweight=',i[5])
		print('pbloodgp=',i[6])
		print('pdiagnosis=',i[11])
		print('pphno=',i[7])
		print('pemail=',i[8])
		print('paddress=',i[9])
		print()
	print(Dic.rowcount,'records displayed')
	A.commit()

def showgraph():
	A = pymysql.connect(host="localhost",user="root",password="manager",database="hospital")
	SG=A.cursor()
	Sql_command_7='select page from patient_details'
	bins=[0,10,20,30,40,50,60,70,80,90,100]
	SG.execute(Sql_command_7)
	age=SG.fetchall()
	plt.hist(age,bins,rwidth =4)
	plt.xlabel('page')
	plt.ylabel('number of patients in that age ')
	plt.title('Patient age graph')
	plt.show()
	A.commit()

Choice=int(input('Enter 1 to select patient management '))
if Choice==1:
                print('Thank you for selecting patient management ')
                Patient_Management()
else :
                pass


