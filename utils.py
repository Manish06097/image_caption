import os
import torch
import openai
import requests
import numpy as np
from PIL import Image
from dotenv import dotenv_values
from transformers import BlipProcessor, BlipForConditionalGeneration

class ImageCaptionGenerator:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")
        
    
    def generate_captions(self, image_path, text="A photograph of"):
        raw_image = Image.fromarray(image_path.astype(np.uint8)).convert("RGB")
        inputs = self.processor(raw_image, text, return_tensors="pt").to("cuda")
        out = self.model.generate(**inputs,max_length= 100)
        captions = self.processor.decode(out[0], skip_special_tokens=True) 
        return captions
    
    def capgpt(self,image_description,num_captions):
        openai.api_key=dotenv_values(".env")['OPENAPI']
        
        prompt = f"""image_description:{image_description}, num_captions:{num_captions}, write a Captions that  should be catchy, exciting, innovative, captivating, creative and
engaging ,output should be in the form of json format {{ 
caption1:"",
caption2:"",
......

}}   """

        response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.2,
        max_tokens = 1000,
        messages = [
            {"role": "user", "content": prompt}
        ]
        )
        
        return response['choices'][0]['message']['content']
    
    




