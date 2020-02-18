from PIL import Image
from django.shortcuts import render
from django.http import HttpResponseRedirect

from answersheet.forms import AnswerSheetUploadForm
from answersheet.models import AnswerSheet


def uploadFile(request):
    if request.method == 'POST':
        form = AnswerSheetUploadForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            image = form.cleaned_data['image']

            # your logic is here
            marks = 55

            AnswerSheet.objects.create(
                image=image,
                marks=marks
            )
            return render(request, 'result.html', {'marks': marks})

    else:
        form = AnswerSheetUploadForm()

    return render(request, 'upload.html', {'form': form})

