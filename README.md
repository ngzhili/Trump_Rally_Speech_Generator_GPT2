
# Trump Rally Speech Generator

Fine Tuned GPT-2 Text Generation Model on Donald Trump's Rally Speeches for US Presidential Elections.

Hugging Face GPT-2 Transformer Model: https://huggingface.co/gpt2

Dataset for Trump Rally Speeches: https://www.kaggle.com/christianlillelund/donald-trumps-rallies

## Pre-processing
Dataset concatenated to form a single .txt file for model training.
GPT-2 Weights fine-tuned using google-colab free GPU for 300 epoch.

## Inference on streamlit

#### 1) Prediction parameters: 
- Temperature = 0.7
- Max Characters Generated = 100
- Top Probability (top P) = 0.9
![Inference 1](https://github.com/ngzhili/Trump_Rally_Speech_Generator_GPT2/blob/main/inference.JPG)

#### 2) Prediction parameters: 
- Temperature = 1.0
- Max Characters Generated = 331
- Top Probability (top P) = 0.9
![Inference 2](https://github.com/ngzhili/Trump_Rally_Speech_Generator_GPT2/blob/main/inference2.JPG)

## aitextgen_streamlit
Streamlit-based Web App for Ai Text Generation based on GPT-2 Models from HuggingFace Model Hub using Python library aitextgen.
Not able to host demo on Huroku via Streamlit due to slug size >500mb after installing dependencies and fine-tuned GPT-2 weights.


