import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen

st.title("Donald Trump Rally Speech Generator")

# Without any parameters, aitextgen() will download, cache, and load the 124M GPT-2 "small" model
# instantiate the model / download
#ai = aitextgen()
ai = aitextgen(model_folder="gpt2_weights_trump_rally_speech")

# Using the "with" syntax
with st.form(key='my_form'):
    prompt_text = st.text_input(label = "Enter your prompt text...",value = "Every family in Minnesota needs to know about sleepy Joe")
    temp = st.slider('Select Temperature/Perplexity',min_value = 0.1, max_value = 1.0, step = 0.1, value =0.7)
    max_length = st.slider('Select Max Length of Characters Generated',min_value = 1, max_value = 1024, step = 10, value =100)
    top_p = st.slider('Select Top Probability (top P)',min_value = 0.0, max_value = 1.0, step = 0.1, value =0.9)
    submit_button = st.form_submit_button(label='Generate Text!')


# gen = st.button('Generate Text!')
# create a prompt text for the text generation 
#prompt_text = "Python is awesome"
#prompt_text = st.text_input(label = "Enter your prompt text...",value = "Every family in Minnesota needs to know about sleepy Joe")
#prompt_text = "Donald Trump is"


#st.write(x)

#gpt_text = ai.generate_one(prompt=prompt_text,max_length = 100)


#print(gen)
if submit_button:
    with st.spinner("AI Trump is thinking of what to say........"):
        # text generation
        #placeholder1 = st.image("thinking_trump.jpg")
        placeholder1 = st.image("donald-trump-thinking.gif", width = 700)
        gpt_text = ai.generate_one(prompt=prompt_text,
                max_length = max_length,
                temperature=temp,
                no_repeat_ngram_size = 2,
                top_p=top_p)
    placeholder1.empty()    
    st.success("AI Trump has successfully generated the text below")
    st.balloons()
    # print ai generated text
    print(gpt_text)
    #placeholder2 = st.image("speaking_trump.jpg")
    placeholder2 = st.image("speaking-trump.gif",width = 700)
    st.markdown(gpt_text)
    

# Runs Application
#streamlit run textgen2.py