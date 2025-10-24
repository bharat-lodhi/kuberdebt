from django.shortcuts import render, redirect
from adminapp.models import Blog,LoanConsultation
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"landing/index.html")


def blog_list(request):
    # Published blogs ko latest order me laate hain
    blogs = Blog.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'landing/blog_list.html', {'blogs': blogs})


from django.shortcuts import get_object_or_404

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, is_published=True)
    return render(request, 'landing/blog_detail.html', {'blog': blog})



def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        total_loan_amount = request.POST.get('total_loan_amount')
        loan_type = request.POST.get('loan_type')
        legal_notice = request.POST.get('legal_notice')
        preferred_timing = request.POST.get('preferred_timing')
        city = request.POST.get('city')
        problem_description = request.POST.get('problem_description')

        # Save to database
        LoanConsultation.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            total_loan_amount=total_loan_amount,
            loan_type=loan_type,
            legal_notice=legal_notice,
            preferred_timing=preferred_timing,
            city=city,
            problem_description=problem_description
        )

        messages.success(request, "Your consultation request has been submitted successfully!")
        return redirect('/contact/') 

    return render(request, 'landing/contact.html')

def services(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        total_loan_amount = request.POST.get('total_loan_amount')
        loan_type = request.POST.get('loan_type')
        legal_notice = request.POST.get('legal_notice')
        preferred_timing = request.POST.get('preferred_timing')
        city = request.POST.get('city')
        problem_description = request.POST.get('problem_description')

        # Save to database
        LoanConsultation.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            total_loan_amount=total_loan_amount,
            loan_type=loan_type,
            legal_notice=legal_notice,
            preferred_timing=preferred_timing,
            city=city,
            problem_description=problem_description
        )

        messages.success(request, "Your consultation request has been submitted successfully!")
        return redirect('/services/') 
    return render(request,"landing/services.html")