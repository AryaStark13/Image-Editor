from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from PIL import Image
import io
import base64
from MIRNet import low_light

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class GetImage(View):
    def __init__(self):
        self.model = None
        self.did_load = False

    def get(self, request):
        self.did_load = low_light.load_model()
        return HttpResponse(self.did_load)

    def post(self, request):
        data = json.loads(request.body)
        data['image'] = data['image'].replace('data:image/png;base64,', '')

        img = Image.open(io.BytesIO(base64.decodebytes(bytes(data['image'], "utf-8"))))
        img = img.convert('RGB')

        updated_img, total_time = low_light.enhance(img)
        updated_img.save('updated.png')

        with open('updated.png', 'rb') as f:
            b64_string = base64.b64encode(f.read())
            b64_string = str(b64_string, 'utf-8')

        # print(str(b64_string))
        return JsonResponse({'image': b64_string, 'loading_time': total_time})