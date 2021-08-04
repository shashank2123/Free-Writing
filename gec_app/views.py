from django.shortcuts import render
import requests

# Create your views here.

def load_gec_page(request):
    text_value = ""
    corrections = ""
    if request.method == "POST":
        text_value = request.POST.get('incorrect_text')

        prefix = 'gec: '

        text_list = [ prefix + temp + '.' for temp in text_value.split('.') if temp.strip() != '']

        print(text_list)

        API_URL = "https://api-inference.huggingface.co/models/prithivida/grammar_error_correcter_v1"
        headers = {"Authorization": "Bearer api_ydyBXEkeTYneggYHgyXrGamriQfRTtAfxJ"}

        def query(payload):
	        response = requests.post(API_URL, headers=headers, json=payload)
	        return response.json()
        
        if text_list:
            output = query({   
                    "inputs": text_list,
                    "parameters":{
                        "max_length":512
                        }
                    })
            
            corrected_sent = [sent['generated_text'] for sent in output]

            corrections = " ".join(corrected_sent)

        text_value = text_value.replace(prefix,'')



    return( render(request,"gec_app/gec.html",{"text_value":text_value,"corrections":corrections}))
