from django.views import View
from django.http import JsonResponse, FileResponse, HttpResponse
import json
from PIL import Image, ImageFilter
import io
import base64
from MIRNet import low_light

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class GetImage(View):
    def post(self, request):
        data = json.loads(request.body)
        data['image'] = data['image'].replace('data:image/png;base64,', '')

        img = Image.open(io.BytesIO(base64.decodebytes(bytes(data['image'], "utf-8"))))
        img = img.convert('RGB')
        # img.save('original.png')

        # updated_img = img.rotate(180)
        updated_img = low_light.enhance(img)
        updated_img.save('updated.png')
        with open('updated.png', 'rb') as f:
            b64_string = base64.b64encode(f.read())


        return HttpResponse(b64_string)
        # return HttpResponse(base64.b64encode(bytes(img)))