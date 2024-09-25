# Generative AI Blog Generator 🤖

This is a Streamlit web application that generates blogs based on a given topic, target audience, and specified word count using the LLaMA 2 model.

## Features

- Generate a blog post by specifying a topic.
- Customize the length of the blog by inputting the number of words.
- Select the target audience: Researchers, Data Scientists, or Common People.
- Uses LLaMA 2 model (`IranziInnocent/llama-2-7b-chat.ggmlv3.q8_0`) to generate the text.

## How it Works

1. Enter a topic in the input box.
2. Specify the desired number of words for the blog.
3. Choose the target audience from a dropdown (Researchers, Data Scientist, or Common People).
4. Click the "Generate" button to create the blog.
5. The generated blog will be displayed on the screen.

## Installation
1. **Install required dependencies**:
    Make sure you have Python installed. Then, install the necessary libraries:
    ```bash
    pip install streamlit
    pip install langchain_community
    pip install ctransformers
    ```

2. **Run the Streamlit app**:
    Start the Streamlit server with the following command:
    ```bash
    streamlit run app.py
    ```

## Requirements

- Python 3.x
- `streamlit`
- `langchain_community`
- `ctransformers`

## Model Details

The app utilizes the LLaMA 2 model (`IranziInnocent/llama-2-7b-chat.ggmlv3.q8_0`), which is available on Hugging Face. Ensure you have the necessary access or local storage for the model if running offline.

## Usage

Once the app is running:

1. Open your browser and go to the URL provided in the terminal (usually `http://localhost:8501`).
2. Enter your topic in the input box.
3. Specify the number of words you want in the blog.
4. Choose your target audience from the dropdown menu.
5. Click "Generate" to create your blog.
6. The generated blog will appear below the input fields.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you would like to improve the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Developed By

IRANZI INNOCENT
