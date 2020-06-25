import zipfile, time

def bruteforce(file, list="lists\list100k.txt", list2="lists\list1m.txt"):
	zip = zipfile.ZipFile(file) #open the zipfile
	password = None
	counter = 0
	startTime = time.time() #check when we started so we can know how much time it took us
	with open(list, "rt") as f: #open the first 100,000 passwords
		listpass = [x.strip() for x in f.readlines()] #takes passwords from the list one by one while omitting the "\n"
		for password in listpass: #take the passwords one by one
			counter += 1
			try:
				zip.extractall(pwd=password.encode('cp850','replace')) #try to open the file with the given password
			except RuntimeError:
				continue #if fails, continue to the next run of the loop
			finishTime = time.time() - startTime #how much time it took us
			speed = counter/finishTime #how many tries we were doing per second
			print("Password Found")
			print("Password:",password)
			print("It took ",finishTime," seconds to crack the Password (",speed," attempts per second).",sep='')
			f.close()
			return

	with open(list2, "rt") as f: #open the last 900,000 passwords
		listpass = [x.strip() for x in f.readlines()]
		for password in listpass:
			counter += 1
			try:
				zip.extractall(pwd=password.encode('cp850','replace'))
			except RuntimeError:
				continue
			finishTime = time.time() - startTime
			speed = counter/finishTime
			print("Password Found")
			print("Password:",password)
			print("It took ",finishTime," seconds to crack the Password (",speed," attempts per second).",sep='')
			f.close()
			return
			
	print("Password Not Found")
	f.close()
	
if __name__ == "__main__": #don't run if imported
	path = input("zip path?\n")
	bruteforce(path)
	input("Press Enter to exit...")
	quit()
