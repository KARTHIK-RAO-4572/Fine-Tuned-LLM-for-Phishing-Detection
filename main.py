'''
Streamlit Application
'''

import streamlit as st
import logging
from Utilities.messageProcessor import MessageProcessor # File with logic for inference
from UI.uiElements import UIElements

# Logger Configuration
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


# Fetch HTML Code
titleElement = UIElements.title
phishingCardElement = UIElements.phishingCard
safeCardElement = UIElements.safeCard
developmentTeamInfoElement = UIElements.developmentTeamInfo

# Set Elements in UI

# title
st.html(titleElement)

# Side bar
with st.sidebar:
    st.image("https://github.com/KARTHIK-RAO-4572/GitHub-Images/blob/main/AU_AI_Logo.png?raw=true",width="stretch")
    st.html(developmentTeamInfoElement)

# Text area
st.session_state['message']  = st.text_area(label = "Text Area label",placeholder="Paste your message here",label_visibility="hidden")

device = 'cpu' # Change to GPU when avauilable

messageProcessor = MessageProcessor("Karthik-Rao-4572/Demo",device)

# Button to show result
if st.button('Predict'):
    if not st.session_state['message']:
        logging.error("Tried to predict with empty message")
        st.error('Message cannot be empty')
    else:
        columns = st.columns(3)
        with st.spinner("Making prediction"):
          result = "Safe"
          logging.info("Started Process...")
          result = messageProcessor.processMessage(st.session_state['message'])
          logging.info("Result Received is : \n" + result)
        if(result=="Phishing"):
            columns[1].html(phishingCardElement)
        elif(result=="Safe"):
            columns[1].html(safeCardElement)


