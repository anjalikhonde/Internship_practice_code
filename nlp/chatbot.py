import nltk
from nltk.tokenize import word_tokenize

# Download the necessary NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

print("==============================================")
print("AI CUSTOMER SUPPORT CHATBOT")
print("==============================================")

while True:
    user = input("\nYou: ").lower()
    tokens = word_tokenize(user)

    if "hello" in tokens or "hi" in tokens:
        print("Bot: Hello! Welcome to ABC Company.")

    elif "price" in tokens:
        print("Bot: Product prices start from Rs.999.")

    elif "delivery" in tokens:
        print("Bot: Delivery takes 3-5 business days.")

    elif "refund" in tokens:
        print("Bot: Refund will be processed within 7 days.")

    elif "order" in tokens:
        print("Bot: Please enter your Order ID on our website.")

    elif "contact" in tokens:
        print("Bot: Call us at 1000-100-100.")

    elif "bye" in tokens:
        print("Bot: Thank you! Visit Again.")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")