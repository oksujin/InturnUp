from django.shortcuts import render
from community.forms import *

# 우리가 만들 함수 구현

"""
request를 인자로 하는 write 함수 
사용자의  요청이 request에 담긴다
"""

def write(request):
    """
    form 버튼 누르면 post 발생
    request된 POST들을 모두 form에 넣어준다.
    만약 form이 유효하면 db에 저장(form.save())
    유효하지 않다면 화면에서 보여주기만 함
    """
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save() #form을 db에 저장하는 부분
    else:
        form = Form() #form을 생성

    # 마지막 변수 html에 form을 보내주는 변수
    return render(request, 'write.html', {'form':form})
    """
    request를 rendering하는 과정
    templete를 쓰겠다고 지정한 상황
    write에서 html로 보내는 작업
    write.html파일 필요해서 생성해줌

    community에서 오른쪽버튼 new folder : templates
    templates에서 오른쪽버튼 new file : write.html
    """

def list(request):
    """
    Article이라는 db table에 있는 모든 column을 가져오게 된다.
    list를 가지고 오는 명령어
    """
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num) #num id를 넘겨서 object 하나를 가져온다
    return render(request, 'view.html', {'article':article})
  