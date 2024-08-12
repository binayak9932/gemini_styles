from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

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

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    style_file_path = data.get('style_file_path')
    user_prompt = data.get('user_prompt')

    if not style_file_path or not user_prompt:
        return jsonify({'error': 'Both style_file_path and user_prompt are required.'}), 400

    try:
        style_text = read_style_file(style_file_path)
        generated_content = generate_content(style_text, user_prompt)
        return jsonify({'generated_content': generated_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
