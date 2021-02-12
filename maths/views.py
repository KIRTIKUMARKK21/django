from django.http import HttpResponse
from django.shortcuts import render
def math(request):
    return render(request,"index1.html")
def Sum(request):
    f1=request.GET.get("f1",0)
    f2=request.GET.get("sd",0)
    s=request.GET.get("s")
    if s=="Sum":
        sum=int(f1)+int(f2)
        dic={"res":sum}
        return render(request,"index1.html",dic)
    d=request.GET.get("d")
    if d=="Diff":
        diff = int(f1) - int(f2)
        dic = {"res": diff}
        return render(request, "index1.html", dic)
    d=request.GET.get("m")

    if d == "Mult":
        mult = int(f1)*int(f2)
        dic = {"res": mult}
        return render(request, "index1.html", dic)
    d=request.GET.get("div")

    if d == "Divide":
        div = int(f1)/ int(f2)
        dic = {"res": div}
        return render(request, "index1.html", dic)
    d = request.GET.get("hcf")

    if d == "Hcf":
        def h(a, b):
            if (a > b):
                g, s = a, b
            else:
                g, s = b, a
            if s == 0:
                return (g)
            else:
                rem = g % s
                return h(s, rem)
        hcf=h(int(f1),int(f2))

        dic = {"res": hcf}
        return render(request, "index1.html", dic)

    d = request.GET.get("lcm")

    if d == "Lcm":
        def h(a, b):
            if (a > b):
                g, s = a, b
            else:
                g, s = b, a
            if s == 0:
                return (g)
            else:
                rem = g % s
                return h(s, rem)
        lcm=(int(f1)*int(f2))/h(int(f1),int(f2))

        dic = {"res": lcm}
        return render(request, "index1.html", dic)

    d = request.GET.get("clr")
    if d == "cl":

        return render(request, "index1.html")






