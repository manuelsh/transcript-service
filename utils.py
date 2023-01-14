from io import BytesIO
import base64
import banana_dev as banana
from keys import api_key, model_key

# Expects an mp3 file named test.mp3 in directory

def transcribe(file):
    #mp3bytes = BytesIO(file)
    #mp3 = base64.b64encode(mp3bytes.getvalue()).decode("ISO-8859-1")
    mp3 = base64.b64encode(file).decode("ISO-8859-1")
    model_payload = {"mp3BytesString": mp3}
    out = banana.run(api_key, model_key, model_payload)
    return out['modelOutputs'][0]