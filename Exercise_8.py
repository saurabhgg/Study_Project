formatter= ('%r %r %r %r')
abc='I could have wrote '
print formatter %('Hello','Friend',"Wassup" , "?")
print formatter %(formatter,formatter,formatter,formatter)
#Everything is coming in quotes because we have used %r not %s
print formatter %(abc, 'A full story','About the incidence that' , 'Happened last night but I am in no mood')