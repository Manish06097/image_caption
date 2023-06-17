# AI Image Captioning

This project is an AI tool that generates captions based on the images provided by the user. It utilizes pre-trained models from the Hugging Face library to perform image caption generation and uses OpenAI's GPT-3.5 Turbo model for generating catchy and creative captions.

## Project Overview

The project consists of a Gradio-based application that provides a user-friendly interface for uploading images and receiving AI-generated captions for those images.

![image](https://github.com/Manish06097/image_caption/assets/73208573/07bb8293-a350-4a77-b9c2-951708d9115c)


## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python 3.7 or higher
- Gradio
- PyTorch
- Transformers
- OpenAI

You can install the required packages using the following command:
```
pip install -r requirements.txt
```


## How to Run

1. Clone the repository to your local machine.
2. Navigate to the project directory.

3. Set up the environment variables by creating a `.env` file in the project directory and adding the following line:
```
OPENAPI=<your_openai_api_key>
```

Replace `<your_openai_api_key>` with your actual OpenAI API key.

4. Start the Gradio application by running the following command:

5. Open your web browser and go to the provided URL (e.g., `http://localhost:7860`) to access the application.

6. Upload an image and click the "Generate Captions" button to receive AI-generated captions for the image.

## Code Concept

The code concept revolves around the Gradio library, which simplifies the creation of user interfaces for machine learning models.

The `app.py` file contains the application logic and interface configuration. It uses the `caption_generator` function to generate captions for the uploaded image.

The `caption_generator` function utilizes the `ImageCaptionGenerator` class from the `utils.py` module. This class encapsulates the functionality for generating image captions. It uses pre-trained models from the Hugging Face library to process images and generate captions.

The generated captions are then passed to OpenAI's GPT-3.5 Turbo model for further refinement and creativity. The final captions are returned and displayed in the Gradio interface.

Feel free to explore the code further and customize it according to your needs!


## Hugging Face BLIP Model
The project utilizes the BLIP model from Hugging Face, which is a state-of-the-art vision-language model for unified vision-language understanding and generation. The model has been pre-trained on a large dataset of image-caption pairs to learn the correlation between visual content and textual descriptions.

The BLIP model leverages the Vision Transformer (ViT) architecture, which has shown excellent performance in various vision tasks. It combines image processing and language understanding capabilities to provide accurate and contextually relevant captions for images.

![image](https://github.com/Manish06097/image_caption/assets/73208573/b7e866a5-6d26-41e3-a083-950b34128bfd)

## Available Checkpoints and Tasks
The project provides pre-trained and fine-tuned checkpoints for various tasks:
- Image Captioning (COCO)

These checkpoints can be used to evaluate the model's performance on specific tasks or further fine-tune the model for custom applications.

## Acknowledgements
The project acknowledges the resources and libraries that it builds upon, including ALBEF, Huggingface Transformers, and timm. These open-source contributions have been instrumental in the implementation and success of the BLIP model.

If you find this project useful for your research or application, consider citing the original paper presented at the International Conference on Machine Learning (ICML) in 2022.

Please refer to the project documentation and official resources for more detailed instructions, code examples, and updates related to the BLIP model and its integration in this project.




