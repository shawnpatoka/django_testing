from django.shortcuts import render
from .models import botwTest

def home_view(request):
    return render(request,'home.html')

def home_output_view(request):
    if request.method == 'POST':
        post=botwTest()
        post.tile_1_location = request.POST.get('tile_1_location')
        post.tile_1_headline = request.POST.get('tile_1_headline')
        post.tile_2_location = request.POST.get('tile_2_location')
        post.tile_2_headline = request.POST.get('tile_2_headline')
        post.tile_3_location = request.POST.get('tile_3_location')
        post.tile_3_headline = request.POST.get('tile_3_headline')
        post.tile_4_location = request.POST.get('tile_4_location')
        post.tile_4_headline = request.POST.get('tile_4_headline')
        post.tile_5_location = request.POST.get('tile_5_location')
        post.tile_5_headline = request.POST.get('tile_5_headline')
        post.tile_6_location = request.POST.get('tile_6_location')
        post.tile_6_headline = request.POST.get('tile_6_headline')
        post.save()

        

        context = {
            'stuff': {
                'location': post.tile_1_location,
                'headline': post.tile_1_headline,
            }
        }


        return render(request, 'output.html', context)  

    else:
        return render(request,'output.html')
    
