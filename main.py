import os
import argparse
from dotenv import load_dotenv
from google import genai 
from google.genai import types

def main():
    load_dotenv()
    api_key=os.environ.get("GEMINI_API_KEY")

    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt",type=str,help="User Prompt")
    parser.add_argument("--verbose",action="store_true",help="Enable verbose output")
    args=parser.parse_args() # This method runs the parser and stores the xtracted data in a argsparse.Namespace object

    messages : list[types.Content] = [types.Content(role="user",parts=[types.Part(text=args.user_prompt)])]

    client= genai.Client(api_key=api_key)
    response = client.models.generate_content( # returns a GenerateContentResponse object
        model="gemini-2.5-flash",
        contents= messages
    ) 
    if args.verbose:
        print(f"Prompt Token : {response.usage_metadata.prompt_token_count} \n Response Token :{response.usage_metadata.candidates_token_count}")
    return response.text
    
if __name__ == '__main__' :
    result =main()
    print(result)


