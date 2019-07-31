from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Board
from django.core.paginator import Paginator
from .forms import BoardForm
from user.models import Uniuser

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Uniuser.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']

            # newFile = Board(file = request.FILES['docfile'])
            # newFile.save()

            board.writer = user
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()
        files = Board.objects.all()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 10)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/board/list/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})