import operator
import string
import PyQt5
import json
global priority_reference
sorted_priorities = []

# def init():
# priority_reference = {
#                          "tire": 2,
#                          "tire losing air": 3,
#                          "tire losing pressure": 3,
#                          "tire leaking air": 3,
#                          "tire leaking": 3,
#                          "break light out": 10,
#                          "break light needs to be replaced": 10,
#                          "break light burnt out": 10
#                         }

priority_reference = {
    "tire": 2,
    "brake light": 5,
    "clutch": 7,
    "transmission": 10,
    "crankshaft": 12,
    "brake": 10,
    "brakes": 8,
    "oil": 4,
    "oil change": 4,
    "shock": 6,
    "shocks": 6,
                    }

# everything with with word 'tire' worth 3
# everything with the word 'crankshaft' worth 12
# everything with the word 'light' is worth a 4
# DOESN'T MATTER WHAT OTHER WORDS ARE IN THE STRING!!!
# RANDY SAYS USE REGEX TO TELL IF THE WORD IS IN OUR STRING!!!
# THIS IS GOOD ENOUGH!!

def build_priorities():
    print("building list of priority")
    issues = []
    building = 1
    while building:
        issue = input("Enter an issues to record: ")
        if issue == "done":
            building = False
        issues.append(issue)
    return issues


def prioritize(issueList):
    # print("Prioritizing list of issues")
    urgency = []
    p = {}
    # issues = build_priorities()  # issues contains string such as "Front tire is losing air"
    issues = issueList
    for issue in issues:
        issue.lower() # this might not make a difference
        priority_level = 0
        for key in priority_reference:
            if key in issue:
                value = priority_reference.get(key, 0)  # issue, 0)
                priority_level = priority_level + value
                p[issue] = priority_level
                urgency.append(priority_level)
        p[issue] = priority_level  # put an issue into the list even if it doesn't have a key in it!

    # for key in priority_reference:
    #     for issue in issues:  # for each string in the list of issues
    #         priority_level = 0
    #         if key in issue:
    #             # tokenize string 'key'
    #             # for/while loop thru 'key' tokens
    #             # check if priority_refrence.has_key(token[i]) by while or for looping through *DEFAULT GET VALUE IS ZERO SO DON'T NEED TO CHECK!
    #             # value = priority_reference.get(key, default=0)
    #             # check if key contains it by priority_reference.has_key(key, default=0) * DON'T NEED THIS B/C DEFAULT IS ZERO!
    #             # print(key.split())
    #
    #             # priority_level = 0
    #             value = priority_reference.get(key, 0)  # issue, 0)
    #             priority_level = priority_level + value
    #             p[issue] = priority_level
    #             urgency.append(priority_level)

    urgency.sort()
    # print(urgency)
    sorted_priorities = sorted(p.items(), key=operator.itemgetter(1))
    # print(sorted_priorities) # sorted_priorities is a LIST
    return sorted_priorities


        # if priority_reference.has_key(key):
        #    value = priority_reference.get(key, default=0)
        #    priority_level = priority_level + value
        #    urgency.append(priority_level)  # add new priority level to list of priorities

# def save_file():
    # file = open('issues.txt', 'r+')
    # file.write("Hey, did I get saved?")
    # json.dump(file, sorted_priorities)
    # O_CREAT
    # file.close()
