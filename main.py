from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

model = GPT2LMHeadModel.from_pretrained('./model/checkpoint-40000')

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')


def generate_poem(emotion, prompt, length=200):
    prompt = emotion + ' ' + prompt

    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        pad_token_id=tokenizer.eos_token_id,
        max_length=length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.92,
        temperature=.85,
        do_sample=True,
        top_k=125,
        early_stopping=True
    )

    text = tokenizer.decode(output[0], skip_special_tokens=True)

    text = text[len(emotion):]

    # text = text.replace('   ', '\n')

    return text


emotion = input("Enter the emotion: ")
prompt = input("Enter the prompt: ")

print(generate_poem(emotion, prompt))
