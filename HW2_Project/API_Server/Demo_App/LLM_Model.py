from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
import torch

tokenizer = None
model = None

def load_model():
    global tokenizer, model

    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

def process_prompt(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    outputs = model.generate(input_ids)
    response = tokenizer.decode(outputs[0])
    prefix_length = len("<pad>")
    suffix_length = len("</s>")
    result = response[prefix_length:-suffix_length].strip()

    return result

