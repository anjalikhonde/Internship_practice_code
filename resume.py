import pandas as pd

print("=======================================================")
print("AI RESUME SCREENING SYSTEM")
print("=======================================================")

name=input("Candidate Name:")

resume=input("Enter Skills:").lower()

required_skills=[
    "python",
    "machine learning",
    "sql",
    "communication"
]

score=0
matched=[]

for skill in required_skills:
    if skill in resume:
        score+=1

        matched.append(skill)

percentage=(score/len(required_skills))*100

print("candidate :",name)

print("matched skills:",matched)

print("score:",score)

print("percentage:",percentage,"%")

if percentage>=75:

    print("Result:shortlisted")

elif percentage>=50:

    print("Result:Need Technical Interview")

else:
    print("Results:Rejected")