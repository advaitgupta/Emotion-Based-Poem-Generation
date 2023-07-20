# Emotion-Based Poem Generation with GPT-2

The Emotion-Based Poem Generation project is an innovative application of the GPT-2 language model, designed to generate unique and emotionally resonant poems based on user-specified emotions. The core of this project is the GPT-2 model, a large-scale transformer-based language model known for its high-quality text generation capabilities. The model has been fine-tuned on a specially curated dataset of poems, each labeled with a specific emotion. This dataset was created by combining a large collection of poems with the NRC Emotion Lexicon, a comprehensive lexicon that associates words with eight basic emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and two sentiments (negative and positive). The fine-tuned model is capable of generating new poems that not only adhere to the stylistic and thematic characteristics of the training data but also reflect the emotional tone specified by the user. This is achieved by using the specified emotion as a prompt for the GPT-2 model, guiding the emotional tone of the generated poem. The project provides flexibility in terms of the length of the generated poems, allowing users to specify their preferred length.

## Table of Contents
1. [Features](#features)
2. [Dataset Preparation](#dataset-preparation)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dependencies](#dependencies)

## Dataset Preparation

- The dataset of poems was scraped from the Poetry Foundation website.
- The poems were cleaned by removing punctuation, converting to lowercase, and lemmatizing the words.
- The NRC Emotion Lexicon was used to label the poems with emotions. Each word in a poem was matched with the corresponding emotions in the lexicon.
- The emotion score for a poem was calculated as the sum of the scores of its words for each emotion. The emotion with the highest score was assigned as the label for the poem.
- The emotions supported by this project are: anger, anticipation, disgust, fear, joy, sadness, surprise, trust, and neutral.

## Features

- Utilizes the GPT-2 language model for text generation.
- Trained on a dataset of poems labeled with emotions from the NRC Emotion Lexicon.
- Generates a poem based on a specified emotion.
- The emotion is used as a prompt for the GPT-2 model, guiding the tone of the generated poem.
- The generated poems reflect the emotional tone specified by the user.
- The model can generate poems of varying lengths.

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/EmotionBasedPoemGeneration.git


2. Navigate to the cloned repository:
cd EmotionBasedPoemGeneration


3. Install the required dependencies


## Usage

1. Run the data_scraping.py file to prepare the dataset (skip this step if you already have the poems.csv file from repo).

2. Run the data_classification.py file to clean and label the data.

3. Run the training.py file to train the model.

4. Run the main script.

5. When prompted, enter the emotion you want the poem to reflect along with a starting prompt.

## Dependencies

This project is built using Python and relies on several libraries including:

- Transformers
- Pandas
- PyTorch
- NLTK 
- Sklearn
- Tqdm
