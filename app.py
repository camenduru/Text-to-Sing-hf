import gradio as gr
import re
import requests
import time
import tempfile

token = "XQMy5NHKujX8nXr8YCGktED3f7DEdvzm"
        


def separate_syllables(string):
    #numbers = [ 4, 4, 8, 5 ]
    numbers = [ 8, 9, 8, 9 ]
    # Split the string into a list of characters
    parts = string.split(" ")
    string = "".join(parts)
    print("the new string: "+ string)
    chars = list(string)

    # Create a list to store the syllables
    syllables = []

    # Iterate over the numbers
    for num in numbers:
        # Get the next num characters from the string
        syllable = "".join(chars[:num])
        print("Appending " + "".join(chars[:num]))
        # Add the syllable to the list
        syllables.append(syllable)
        # Remove the syllable from the list of characters
        chars = chars[num:]

    # If there are any remaining characters, add them as a new line
    if chars:
        syllables.append("-")
        for num in numbers:
            # Get the next num characters from the remaining characters
            syllable = "".join(chars[:num])
            # Add the syllable to the list
            syllables.append(syllable)
            # Remove the syllable from the list of characters
            chars = chars[num:]

    # Return the list of syllables joined by spaces
    if("-" in syllables): 
        results = [[]]
        lines = 0
        for i ,v in enumerate(syllables):
            if v == '-':
                lines=lines+1
            else: 
                if(len(results) == 1):
                    results.append([])
                results[lines].append(v)

        return list(map(lambda words: " ".join(words), results))
    else:
        return " ".join(syllables)


def flattenLines(lyrics):
    newValues = []
    for i,val in enumerate(lyrics): 
        if(type(lyrics[i]) == list):
            newValues.append(lyrics[i][0])
            newValues.append(lyrics[i][1])
        else:
            newValues.append(lyrics[i])

    return newValues

def getPayload(index):
    match index:
        case 0:
            return {
                "voiceModel":"CFV_2",
                "voiceModelStyle":"mezzo",
                "language":"en",
                "scoreFileRemotePath":"themes/DeckTheHalls/score/TTS_XMAS_DeckTheHalls_Melody_C_200bpm_4x4_ABCD.json",
                "scoreDataFileRemotePath":"themes/DeckTheHalls/score/TTS_XMAS_DeckTheHalls_Score_Data_ABCD.json",
                "dspFileRemotePath":"themes/DeckTheHalls/dsp/XML/TTS_XMAS_DeckTheHalls_DSP_C_200bpm_ABCD.xml",
                "dspEffect":"",
                "lyrics": [],
                "backgroundSounds":False,
                "artistName":"Cecilia",
                "songName":"Deck The Halls",
                "singerImageRemotePath":"singers/Singer-Cecilia-VideoImageBackground.png",
                "backgroundImageRemotePath":"themes/DeckTheHalls/images/Song-DeckTheHalls-VideoImageBackground02.png"
            }
        case 1:
            return {
                "voiceModel":"CFV_2",
                "voiceModelStyle":"mezzo",
                "language":"en",
                "scoreDataFileRemotePath": "themes/MoveYourBody/score/MoveYourBody_Score_Data_ABCD.json",
                "scoreFileRemotePath": "themes/MoveYourBody/score/MoveYourBody_Melody_ABCD.json",
                "singerImageRemotePath": "singers/Singer-Cecilia-VideoImageBackground.png",
                "dspFileRemotePath": "themes/MoveYourBody/dsp/XML/MoveYourBody_DSP_ABCD.xml",
                "dspEffect":"",
                "lyrics": [],
                "backgroundSounds":False,
                "artistName":"Cecilia",
                "songName":"Move Your Body",
                "backgroundImageRemotePath":"themes/DeckTheHalls/images/Song-DeckTheHalls-VideoImageBackground02.png"
            }
 
        case 2:
            return {
                "voiceModel": "Randy_v3o",
                "voiceModelStyle": "randy",
                "language": "en",
                "scoreFileRemotePath": "themes/DarkTrap/score/DarkTrap_Melody_ABCDEFGH.json", #"themes/DeckTheHalls/score/TTS_XMAS_DeckTheHalls_Melody_C_200bpm_4x4_ABCD.json",
                "scoreDataFileRemotePath": "themes/DarkTrap/score/DarkTrap_Score_Data_ABCDEFGH.json", #"themes/DeckTheHalls/score/TTS_XMAS_DeckTheHalls_Score_Data_ABCD.json",
                "dspFileRemotePath": "themes/DarkTrap/dsp/XML/DarkTrap_DSP_ABCDEFGH.xml", #"themes/DeckTheHalls/dsp/XML/TTS_XMAS_DeckTheHalls_DSP_C_200bpm_ABCD.xml",
                "dspEffect": "",
                "lyrics": [],
                "backgroundSounds": False,
                "artistName": "Jerry",
                "songName": "Dark Trap", #"Deck The Halls",
                "singerImageRemotePath": "singers/Singer-Jerry-VideoImageBackground.png",
                "backgroundImageRemotePath": "themes/DeckTheHalls/images/Song-DeckTheHalls-VideoImageBackground01.png"
            }

        case 3:
            return {
                "artistName": "Jerry",
                "backgroundImageRemotePath": "themes/HappyBirthday/images/Song-HappyBirthday-VideoImageBackground01.png",
                "backgroundSounds": False,
                "dspEffect": "",    
                "dspFileRemotePath": "themes/HappyBirthday/dsp/XML/HappyBirthday_DSP_ABCD.xml",
                "language": "en",
                "lyrics": [],
                "scoreDataFileRemotePath": "themes/HappyBirthday/score/HappyBirthday_Score_Data_ABCD.json",
                "scoreFileRemotePath": "themes/HappyBirthday/score/HappyBirthday_Melody_ABCD.json", 
                "singerImageRemotePath": "singers/Singer-Jerry-VideoImageBackground.png",
                "songName": "Happy Birthday",   
                "voiceModel": "CFV_2",
                "voiceModelStyle": "baritone"
            }
 
        case 4:
            return {
                "voiceModel": "Randy_v3o",
                "voiceModelStyle": "randy",
                "language": "en",
                "scoreFileRemotePath": "themes/Levitate/score/Levitate_Melody_ABCD.json", #"themes/DeckTheHalls/score/TTS_XMAS_DeckTheHalls_Melody_C_200bpm_4x4_ABCD.json",
                "scoreDataFileRemotePath": "themes/Levitate/score/Levitate_Score_Data_ABCD.json", #"themes/DeckTheHalls/score/TTS_XMAS_DeckTheHalls_Score_Data_ABCD.json",
                "dspFileRemotePath": "themes/Levitate/dsp/XML/Levitate_DSP_ABCD.xml", #"themes/DeckTheHalls/dsp/XML/TTS_XMAS_DeckTheHalls_DSP_C_200bpm_ABCD.xml",
                "dspEffect": "",
                "lyrics": [],
                "backgroundSounds": False,
                "artistName": "Jerry",
                "songName": "Levitate", #"Deck The Halls",
                "singerImageRemotePath": "singers/Singer-Ed-VideoImageBackground.png",
                "backgroundImageRemotePath": "themes/Levitate/images/Song-Levitate-VideoImageBackground02.png"
            }
 


def greet(index, lyrics):
    url = "https://staging-gateway-api.voicemod.net/v2/cloud/partners/ttsing"
    verification_url = "https://staging-gateway-api.voicemod.net/v2/cloud/partners/ttsing/"

    print("Calling api with "+ lyrics)

    lines = lyrics.split("\n")
    #newLines = flattenLines(list(map(separate_syllables, lines)))

    payload = getPayload(index)
    payload["lyrics"] = lines


    headers = {
        'x-api-key': token
    }


    print(payload)
    print("Before the call")
    response = requests.request("POST", url, headers=headers, json=payload)
    print("After the call...")
    jsonResp = response.json()
    print(response.text)
    jobID = jsonResp['jobId']
    verification_url += jsonResp['jobId']
    while(True):
        response = requests.request('GET', verification_url, headers=headers)
        print(response.text)
        print(jobID)
        jsonResp = response.json()
        if(jsonResp['status'] == 'failed'):
            return ""

        if('transformedAudioUrl' in jsonResp and jsonResp['transformedAudioUrl'] is not None):
            return gr.make_waveform(download_file(jsonResp['transformedAudioUrl']))
            #return download_file(jsonResp['urlVideoWithBackground'])
        print("Still processing...")
        time.sleep(1)




def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(response.content)
            tmp_file.flush()
            return tmp_file.name
    else:
        print("Error: Unable to download file")


with gr.Blocks() as demo:
    #def handleChange():
    #    line3.update(visible=False)

    gr.Markdown("""
        ## Voicemod's Text-to-Song API
        To use this API follow the instructions:
        1. First, select the melody you want from the dropdown
        2. Then write the lyrics for it

        ### Disclaimer
        Each melody has specific requirements for the lyrics (number of notes per verse and duration of each note).

        Use the examples provided to understand how they work and write valid lyrics to get best results

        Also, the length of the song is fixed, if you go over the line numbers the extra lyrics will be ignored.
        """)

    music_options = ["Deck the Halls by Cecilia", 
                     "Move your Body by Cecilia",
                     "Dark Trap by Jerry",
                     "Happy Birthday by Jerry",
                     "Levitate by Ed"]

    with gr.Row():                
        with gr.Column():
            with gr.Row():
                dd = gr.Dropdown(choices=music_options, type="index", label="Select the melody...")
                lines = gr.Textbox(lines=10, placeholder="Write your lyrics here...", label="Lyrics")

            with gr.Row():
                btn = gr.Button("Run")
        with gr.Column():
            video = gr.Video(label="Generated output")
            video.style(height=300)
        


    gr.Markdown("""
    ## Example lyrics

    To make your life easier, while testing the API, you can use and modify the following lyrics for each song:
    """)
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
                ### Dark Trap by Jerry

                > this is just a test  
                > don't worry about what I say  
                > the lyrics want to  go crazy  
                > when pushed too hard  
                > take it easy and relax  
                > this is moving too fast  
                > I can help you be  
                > a better singer  
            """)
        with gr.Column():
            gr.Markdown("""
                ### Happy Birthday by Jerry

                > happy birthday to you   
                > happy birthday to you!   
                > happy birthday dear Laura  
                > happy birthday to you!  
            """)
        with gr.Column():
            gr.Markdown("""
                ### Deck the Halls by Cecilia

                > Deck the halls with boughs of holly  
                > Fa la la la la, la la la la   
                > 'Tis the season to be jolly  
                > Fa la la la la, la la la la   

            """)
        with gr.Column():
            gr.Markdown("""
                ### Levitate by Ed 

                > this is just a test  
                > don’t worry about what I say  
                > the lyrics want to go crazy  
                > when pushed too hard  
            """)
        with gr.Column():
            gr.Markdown("""
                ### Move Your Body by Cecilia

                > this is just a test  
                > don’t worry now  
                > the lyrics will come the less you think about them  
                > just feel the melody  
            """)
     
 
 
    gr.Markdown("""
        ## Want to use this API for your project?

        If you'd like to use this API for your own project, request access through our [form here](https://voicemod.typeform.com/to/KqeNN6bO?typeform-source=huggingface)
    """)
   

    btn.click(fn=greet, 
              inputs=[
                    dd,
                    lines
              ],
                outputs=video)

demo.queue().launch(share=True)
