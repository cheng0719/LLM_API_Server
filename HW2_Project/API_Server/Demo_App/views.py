# from django.shortcuts import render

# views.py in language_api app

from django.http import JsonResponse
from asgiref.sync import sync_to_async
from django.shortcuts import render
import json
from .LLM_Model import process_prompt 

@sync_to_async
def process_prompt_async(prompt):
    return process_prompt(prompt)

async def prompt_view(request):
    if request.method == 'POST':
        try:
            # correct parsing of JSON
            data = json.loads(request.body)
            prompt = data['prompt']
            response = await process_prompt_async(prompt)
            return JsonResponse({'status': True, 'data': response})
        except KeyError as e:
            # return specific information about the missing parameter
            return JsonResponse({'status': False, 'message': 'Missing prompt in request'})
        except json.JSONDecodeError as e:
            # add this except block to catch JSON decoding errors
            return JsonResponse({'status': False, 'message': 'Invalid JSON input'})
        except Exception as e:
            # make sure to catch any other exceptions here
            return JsonResponse({'status': False, 'message': str(e)})
    else:
        return JsonResponse({'status': False, 'message': 'Only POST method is accepted'})



def index(request):
    return render(request, 'index.html')