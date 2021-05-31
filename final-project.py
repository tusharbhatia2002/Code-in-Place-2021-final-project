'''
Welcome to the pre-screening test to check the eligibility of a candidate for job application.
the recruiter loads in a json file which contains the job requirements/parameters.
A series of questions is asked from the candidate for pre-screening/assessing the profile
'''

import json #importing json module
def main():
    candidate_details()
    eligibility_criteria()

#Reading json file which has job details mentond in it
with open('data.json') as f:
    qualifications = json.load(f)

#creating global variables to be used in following functions
A = 0
B = 0
C = 0
D = 0
E = 0
L = qualifications['mandatory_skills']
M = qualifications['bonus-skills']

#function to take details from the candidate
def candidate_details():

    print("Welcome candidate!")
    print('Answer the following pre-screening questions to asses your profile for eligibility for the position of web developer:')
    print("")
    ed = {1:'High school or equivalent', 2:'Bachelors degree',3:'Masters degree'}
    work = {1:'Less than 1 year',2:'1-3 years',3:'More than 3 years'}
    engl = {1:'A2',2:'B1',3:'B2',4:'C1',5:'C2'}
    education = int(input("Select the option number of your highest educational qualification: \n1.High school or equivalent\n2.Bachelors degree or equivalent\n3.masters degree or equivalent\nAnswer: "))
    while education not in [1,2,3]:
        education = int(input("invalid input,please enter 1, 2 or 3 "))
    if ed[education] in qualifications["educations"]:
        global A
        A = 1
    work_ex = int(input("Select the option number of your Work experience(in years)\n1.Less than 1 year\n2.1-3 years\n3.More than 3 years\nAnswer: "))
    while work_ex not in [1,2,3]:
        work_ex = int(input("invalid input,please enter 1, 2 or 3 "))
    if work[work_ex] in qualifications['work-experience']:
        global B
        B = 1
    eng = int(input("Select the option number of your english proficiency level:\n1.A2\n2.B1\n3.B2\n4.C1\n5.C2\nAnswer: "))
    while eng not in [1, 2, 3,4,5]:
        eng = int(input("invalid input,please enter 1, 2, 3, 4 or 5 "))
    if engl[eng] in qualifications['english-proficiency-level']:
        global C
        C = 1
    for i in L:
        question = input('Are you proficient with '+ str(i) + " ? (Y/N)")
        if question.lower() == "y":
            global D
            D+=1
    while True:
         bonus =input("Please select and enter additional skills(if any) from the following list(Case Sensitive): \n"+ str(M))
         if bonus == "":
             break
         if bonus in M:
            global E
            E += 1

#calculating the result and assessing the eligibility
def eligibility_criteria():
    result = (A + B + C + D)
    if result < 7:
        print("")
        print("Sorry, you are not eligible to apply!")
        feedback()
    else:
        print("")
        print("You are eligible to apply.")
        if E > 0:
            print("You have "+ str(E) + " bonus skill(s).")

#providing with feedback
def feedback():
    if A == 0:
        print('Your educational qualification is low')
    if B == 0:
        print('You need to gain some more work experience!')
    if C ==  0:
        print('You need to improve your english proficiency!')
    if D < 4:
        print('You do not have minimum technical proficiency required for this role.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
