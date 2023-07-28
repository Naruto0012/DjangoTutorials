def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            context = {
                'form':form,
                'error_message': 'Invalid registration details. Please try again.'
            }
            return render(request, 'signup.html', context)
    else:
        form=UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/login')
