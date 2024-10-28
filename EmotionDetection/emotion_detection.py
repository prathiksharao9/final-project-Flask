"""function libraries"""
import json, requests
def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=input_json, headers=headers)

    if response.status_code == 400:
        error_res = {'anger' : None,'disgust' : None,'fear' : None,'joy' : None,'sadness' : None, 'dominant_emotion' : None}
        return error_res
    formatted_response = json.loads(response.text)
    extracted_res = formatted_response['emotionPredictions'][0]['emotion'] 
    extracted_res['dominant_emotion'] =  next(key for key, value in extracted_res.items() if value == max(extracted_res.values()))
    return extracted_res
