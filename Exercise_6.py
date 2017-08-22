people_type=2
x='There are %d types of people in the world' %(people_type)
binary='binary'
not_binary="doesn't"

y='Those who undertands %s and those who %s' %(binary,not_binary)
print x
print y
# We get the raw format of variable x by embeding it by using %r instead %s.Basically %r is used when we want to do debugging
print "I said : %r" %x
#We are getting y variable inside quotes by having '%s' instead of %s
print "I also said : '%s'" %y

funny_joke=False
joke="Isn't it hillarious %r? "
#We are passing the variable in 2nd step instead of first one.
print joke %funny_joke
