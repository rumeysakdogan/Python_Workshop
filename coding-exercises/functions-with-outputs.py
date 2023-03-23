# Functions with Outputs
# Docstrings

def format_name(f_name, l_name):
  """
  Take a first and last name and format it 
  to return the title case version of the name
  """
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formatted_name = f"{f_name} {l_name}".title()
  return formatted_name

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))