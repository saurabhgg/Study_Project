from sys import argv

script_name,user_name=argv
print 'Hello %s I can see that you want to run %s' %(user_name,script_name)

question=raw_input('Can I ask you some questions before running the script ? ')

if question=='Yes':
    age= raw_input( 'What is your age %s '%user_name)

    gender= raw_input( 'What is your gender %s ' %user_name)

    married = raw_input( 'Are you marrier %s ? ' %user_name)

    print 'Hello %s it was nice knowing you.You are %s %s ' %(user_name,married,gender)

else:
    print """Sorry to hear that %s
but
    i 
    am
    cool
    with that """ %user_name
