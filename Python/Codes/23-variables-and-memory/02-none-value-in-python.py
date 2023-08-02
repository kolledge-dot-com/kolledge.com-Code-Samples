# Mutable default argument issue :
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst



# Return value of a function :
def send_email(to, subject, body):
    # Code to send email goes here...
    return None



# Checking for the Python None value :
value = None
if value is None:
   print("value is None")
else:
   print("value is not None")