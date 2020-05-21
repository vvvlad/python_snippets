

# instead of doing this ternary operator:
website = args['website'] if args['website'] else "https://medium.com/@jhsu98"
# can do this:
website = args['website'] or "https://medium.com/@jhsu98"
# The logical OR operator works by attempting to assign the first value. 
# In the event that the first value coerces to a boolean False—None, 
# empty variable, etc.—then the second value will be used.
