import nltk
from nltk.tokenize import word_tokenize

# Download the tokenizer (only the first time)
nltk.download('punkt')

print("========================================")
print("     AI MEDICAL REPORT ANALYZER")
print("========================================")

# Take input and convert it to lowercase
report = input("\nEnter Medical Report: ").lower()

# Convert the report into words
tokens = word_tokenize(report)

# Debug (You can remove these two lines later)
print("\nTokens:", tokens)

# Disease lists
critical = [
    "cancer",
    "heart",
    "attack",
    "covid",
    "stroke"
]

warning = [
    "fever",
    "diabetes",
    "cough",
    "cold",
    "bp"
]

critical_found = []
warning_found = []

# Check each word
for word in tokens:
    if word in critical:
        critical_found.append(word)
    elif word in warning:
        warning_found.append(word)

# Display Report
print("\nReport Summary")
print("----------------------------------------")
print("Critical :", critical_found)
print("Warning  :", warning_found)

# Decide Priority
if len(critical_found) > 0:
    print("\nPriority : HIGH")
    print("Doctor Consultation Required Immediately")

elif len(warning_found) > 0:
    print("\nPriority : MEDIUM")
    print("Medical Check-up Recommended")

else:
    print("\nPriority : LOW")
    print("No Serious Disease Detected")