'''
Contains logic for model related activities
'''

import logging
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline

# Logger Config
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


class Model:
    '''
    Class that handles Model related activities
    '''
    prompt = None
    model_id = None
    model = None
    tokenizer = None
    text_generator = None


    # Constructor
    def __init__(self, model_id:str, prompt:str, device_map = 'cpu'):
        if(model_id is None or len(model_id) == 0):
            self.model_id = "Karthik-Rao-4572/Demo" # Dummy Model for Testing
        else:
            self.model_id = model_id

        self.prompt = prompt

        # BitsandBytes Configuration
        # self.bnbConfig = BitsAndBytesConfig(
        # load_in_4bit= True,
        # bnb_4bit_use_double_quant= True,
        # bnb_4bit_quant_type= "nf4",
        # bnb_4bit_compute_dtype= torch.bfloat16)
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            device_map = device_map, # What to use CPU or GPU
            # quantization_config = self.bnbConfig # Use if quantization is possible
            )
        
        self.text_generator = pipeline(
            task = "text-generation",
            model = self.model,
            tokenizer = self.tokenizer,
            max_new_tokens = 300)
        
    
    # Method to Get Response
    def makeInference(self, text):
        # Format the text in prompt format
        formattedPrompt = self.prompt.format(text, "", "")
        logging.info("Generating Response . . .")
        response = self.text_generator(formattedPrompt)
        logging.info("Response is generated")
        generated_text = response[0]['generated_text']
        return generated_text

        
        
