import sys
import random

#Function that takes student id and name and returns id and student email   
def generate_email(id, name):
    # split the names into surnames and forenames
    surname, forename = name.split(',')
    # remove non-alphabetic characters from surnames
    surname = ''.join([x for x in surname if x.isalpha()]).lower()
    # extract initials of the names
    initials = '.'.join([n[0] for n in forename.split()]).lower()
    # generate 4 random digits
    digits = str(random.randint(1000, 9999))
    # return the email address
    return f'{id} {initials}.{surname}{digits}@poppleton.ac.uk' 

#Check for command-line argument
if len(sys.argv) < 2:
    print("Error: Missing command-line argument.")
    sys.exit()

try:
    #Open the input file
    f = open(sys.argv[1], "r")
    #Read the student data
    student_data = f.readlines()
    f.close()
    #Open the output file
    f1 = open("emails.txt", "w")
    #Generate the email addresses
    emails = [generate_email(line.split()[0], ' '.join(line.split()[1:])) for line in student_data]
    #Write the email addresses to the output file
    f1.write('\n'.join(emails))
    f1.close()

except FileNotFoundError:
    print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")