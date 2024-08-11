import google.generativeai as genai


GEMINI_API_KEY = ''
genai.configure(api_key=GEMINI_API_KEY)

def read_style_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_content(style_text, prompt):
    model = genai.GenerativeModel('gemini-pro')
    system_prompt = f"""
    You are a content writer with a unique writing style. 
    Your task is to write content based on the following prompt, 
    but in the style of the given text. Here's the style text:
    {style_text}
    Now, write content for the following prompt in the same style:
    """
    
    response = model.generate_content(system_prompt + prompt)
    return response.text

def main():
    style_file_path = input("Enter the path to your style text file: ")
    style_text = read_style_file(style_file_path)
    user_prompt = input("Enter your content prompt: ")
    generated_content = generate_content(style_text, user_prompt)
    print("\nGenerated Content:")
    print(generated_content)

if __name__ == "__main__":
    main()
