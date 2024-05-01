import google.generativeai as genai

# !pip install -U -q google.generativeai # Install the Python SDK

"""## Set up API key"""

"""## Set parameters

"""

"""## Run script

"""

# response = model.generate_content(
# text_scribe
# # ,
#     # Limit to 5 facts.
#     #generation_config = genai.GenerationConfig(stop_sequences=['\n6'])
# )
# print(response.text)
# class scribeState(rx.State):
    
def scribeGenerator():
    GOOGLE_API_KEY="AIzaSyAM2QVm-CFBibfLtq7H-Ed3yL6gi9qNA7A"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(
        "models/gemini-1.5-pro-latest",
        generation_config=genai.GenerationConfig(
            temperature=0.5,
        ),
        system_instruction="You're a professional doctor with 10 years plus expereince in patient care and you're very good at writing SOAP notes",
    )
    audio_file = genai.upload_file(path='./convo_audio.mp3')
    prompt2 = '''
    populate the following information in a python dictionary format, ["Symtoms", "HPI", "PE", "Constitutional", "differental_diagnosis", "Additional"]. 
    Instructions in how to populate HPI
    HPI: Pt is a (age) (M/F) presenting for **(Chief complaint here)**. This is where you would then put the specifics of their main complaint. The HPI format is very dependent on the type of visit it is and the specialty. ER visits and urgent visits are usually focused on ONE chief complaint and all of the associations/descriptions of this issue. If it is family medicine/internal medicine, you will likely have multiple paragraphs describing each issue. 
    '''
    print("calling scribeGenerator")
    response = model.generate_content([prompt2, audio_file]).text
    return response
