from sys import argv

script_name,user_name,file_name=argv

print "We are going to erase %s file %s" %(file_name,user_name)
print "If you want us to stop then please press  (^C)"
print "If you want us to proceed then please press return"

user_ip=raw_input("?")

file2=open(file_name,'r')
print file2.read()


print "Opening the file -> %s" %file_name
file1=open(file_name,'w')

print "truncating the file %s" %file_name
file1.truncate()

print 'Let\'s write something into the file'
file1.write(raw_input('Shoot us with some random stuff that you want us to write'))
file1.write('\n')

file1.write(raw_input('Shoot us with some random stuff that you want us to write again'))
file1.write('\n')
file1.write(raw_input('Shoot us with some random stuff that you want us to write again'))

file1.close()
file2=open(file_name,'r')
print file2.read()
