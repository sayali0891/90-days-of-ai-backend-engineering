def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


"""
Output : 
Title: User Info
Positional arguments: ('Emil', 'Tobias')
Keyword arguments: {'age': 25, 'city': 'Oslo'}

https://www.w3schools.com/python/python_args_kwargs.asp

"""