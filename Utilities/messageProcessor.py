from Utilities.model import Model
class MessageProcessor:
    '''
    Class to process message and get prediction
    '''
    model = None
    prompt = """
You are an expert email security analyst specializing in phishing detection. Your task is to analyze the provided email and determine whether it is legitimate or a phishing attempt.

### Input
# Email Body: {}

### Output Format
# Email Type: {}
# Confidence: {}
"""

    # Constructor
    def __init__(self, model_id, device_map):
        self.model = Model(model_id, self.prompt, device_map)

    # Process Message
    def processMessage(self, message):
        response = self.model.makeInference(message)
        label = self.getLabelFromResponse(response)
        return label

    
    def getLabelFromResponse(self, response):
        '''
        Processes the model response to get predicted label
        '''
        croppedResponse = response[-30: -1 ] # Response last 30 characters contain label
        if "phishing" in croppedResponse.lower():
            return "phishing"
        
        # If not phishing, it is safe
        return "Safe"