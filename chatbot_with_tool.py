
import re
from calculator_tool import calculate
import google.generativeai as genai

API_KEY = "AIzaSyB3HoyHxbBbfmdEz58_02YAzP9RqCyi6DU"
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")

def llm_response(prompt: str) -> str:
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini Error: {e}"

def detect_math_task(user_input: str) -> bool:
    math_keywords = ["add", "plus", "+", "sum", 
                     "times", "multiply", "x", "*",
                     "minus", "subtract", "-", 
                     "divide", "/", 
                     "mod", "modulus", "%"]
    return any(keyword in user_input.lower() for keyword in math_keywords)

def main():
    print("🤖 Chatbot with Calculator Tool ")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        
        if detect_math_task(user_input):
            if any(word in user_input.lower() for word in ["capital", "who", "what", "where", "why"]):
                print("🤖 Sorry, I cannot handle multiple tasks at once yet.")
                continue
            result = calculate(user_input)
            print(f"🤖 Calculator says: {result}")
        else:
            response = llm_response(user_input)
            print(f"🤖 {response}")

if __name__ == "__main__":
    main()
