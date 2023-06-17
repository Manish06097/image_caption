import gradio as gr
import ast
from utils import ImageCaptionGenerator
generator = ImageCaptionGenerator()

def caption_generator(image):   
    caption = generator.generate_captions(image,5)
    captiongpt = generator.capgpt(caption,5)
    captiondict = ast.literal_eval(captiongpt)
    return tuple(captiondict.values())


title = "AI Image Captioning"
description = "Upload an image to generate captions."

app = gr.Interface(fn=caption_generator, inputs=gr.inputs.Image(label="Upload Image"), outputs=['text']*5, title=title, description=description)
app.launch()
