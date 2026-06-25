import os
import argparse
from dotenv import load_dotenv
from google import genai 
from google.genai import types

def main():
    load_dotenv()
    api_key=os.environ.get("GEMINI_API_KEY")

    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("User prompt",type=str,help="User Prompt")
    args=parser.parse_args() # Thid method runs the parser and stores the xtracted data in a argsparse.Namespace object

    messages= [types.Content(role="user",parts=types.Part(text=args.user_prompt))]

    client= genai.Client(api_key=api_key)
    content = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt
    )
    


if __name__ == "__main__":
    main()
