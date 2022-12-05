#Celcius to Fahrenheit
#Formular = c * 1.8 + 32.0

def cel_to_fahr(cel_val):
    """
    This function to convert celcius temp to fahrenheit temp.
    :param cel_val: float
    :return: float
    >>> cel_to_fahr(16)
    60.8
    >>> cel_to_fahr(23)
    73.4
    """
    fahr = cel_val * 1.8 + 32.0
    return fahr
   # return cel_val * 1.8 + 32.0


cel_val = 16
print(cel_to_fahr(cel_val))





#def my_name(name):
    #print("My name is %s" %name)
#my_name("Ridwanullah")
