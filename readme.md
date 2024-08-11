# Gemini Styles

Gemini Styles is a Python script that uses the Gemini AI API to generate content in a specific writing style based on an input text file. The script takes a style sample from a text file and a user-provided prompt, then generates new content that matches the style of the input text.

## Features

- Read writing style from a text file
- Accept user prompts for content generation
- Utilize Gemini AI API to generate content in the specified style
- Simple command-line interface for easy use

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system
- A Gemini AI API key (sign up at [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. Clone this repository or download the script.

2. Install the required Python library:

   ```
   pip install google-generativeai
   ```

3. Replace `'YOUR_API_KEY_HERE'` in the script with your actual Gemini AI API key.

## Usage

1. Run the script:

   ```
   python main.py
   ```

2. When prompted, enter the path to your style text file. This file should contain a sample of the writing style you want to emulate.

3. Enter your content prompt when asked. This is the topic or idea for which you want to generate content.

4. The script will generate content based on your prompt in the style of the input text file and display it in the console.

## Example

```
$ python gemini_style_writer.py
Enter the path to your style text file: sample_style.txt
Enter your content prompt: Write a post about the importance of time management

Generated Content:
[The generated content will appear here]
```

## Security Note

This script includes the API key directly in the code for simplicity. For better security practices, especially in production environments, consider using environment variables or a secure key management system to handle API keys.

## Contributing

Contributions to the Gemini Style Writer project are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please open an issue in this repository.

Happy writing!
