import torch
from torch.utils.data import Dataset, DataLoader
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
import pandas as pd

df = pd.read_csv('poems_with_emotions.csv')

df['text'] = df['Emotion'] + ' ' + df['Poem']

df['text'].to_csv('train.txt', header=False, index=False)

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")  # For macOS with M1 chip
model.to(device)


train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path='train.txt',
    block_size=128
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Define the training arguments
training_args = TrainingArguments(
    output_dir='./model',
    use_mps_device=True,
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=1,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

trainer.train()
