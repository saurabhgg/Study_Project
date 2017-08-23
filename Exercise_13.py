from sys import argv
#From usage is better then direct import as it would save lot of code load during the run time
var1,var2,var3,var4=argv
age=raw_input("Please enter your age sir")
print 'Well you wanted to run file : %s ' %var1

print 'But the file is not present in %s location ' %var2

print 'Please go and have fun in %s ' %var3

print 'And come back after  %s ' %var4

print 'And you are %s ' %age

print '%s %s %s %s %s' %(var1,var2,var3,var4,age)