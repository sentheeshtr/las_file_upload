from django.shortcuts import render, redirect
from .forms import LasFileForm
from .models import LasFile
import laspy  # Install laspy with `pip install laspy`

def upload_file(request):
    if request.method == 'POST':
        form = LasFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_file')
    else:
        form = LasFileForm()
    return render(request, 'upload.html', {'form': form})

def view_file(request):
    las_files = LasFile.objects.all()
    if las_files:
        las_file = las_files.last()
        # Process the LAS file with laspy
        with laspy.open(las_file.file.path) as las:
            # Extract point cloud data (for example)
            points = las.points
            # You might want to extract X, Y, Z coordinates or other attributes
            x = points['x']
            y = points['y']
            z = points['z']
            # This is a simplistic example; adapt as needed
        return render(request, 'view_file.html', {'points': list(zip(x, y, z))})
    return render(request, 'view_file.html', {'error': 'No LAS file found.'})
