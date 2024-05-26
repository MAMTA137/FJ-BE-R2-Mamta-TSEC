from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget, Transaction, IncomeSource, ExpenseCategory
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from django.core.files.storage import FileSystemStorage



@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    income = sum(t.amount for t in transactions if t.income_source)
    expenses = sum(t.amount for t in transactions if t.expense_category)
    context = {
        'transactions': transactions,
        'income': income,
        'expenses': expenses,
        'savings': income - expenses,
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_transaction(request):
    if request.method == 'POST':
        date = request.POST['date']
        amount = request.POST['amount']
        description = request.POST['description']
        income_source_id = request.POST.get('income_source')
        expense_category_id = request.POST.get('expense_category')
        receipt = request.FILES.get('receipt')

        income_source = IncomeSource.objects.get(id=income_source_id) if income_source_id else None
        expense_category = ExpenseCategory.objects.get(id=expense_category_id) if expense_category_id else None

        transaction = Transaction.objects.create(
            user=request.user,
            date=date,
            amount=amount,
            description=description,
            income_source=income_source,
            expense_category=expense_category,
            receipt=receipt
        )
        return redirect('dashboard')

    income_sources = IncomeSource.objects.filter(user=request.user)
    expense_categories = ExpenseCategory.objects.filter(user=request.user)
    return render(request, 'add_transaction.html', {
        'income_sources': income_sources,
        'expense_categories': expense_categories,
    })

@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.date = request.POST['date']
        transaction.amount = request.POST['amount']
        transaction.description = request.POST['description']
        transaction.income_source_id = request.POST.get('income_source')
        transaction.expense_category_id = request.POST.get('expense_category')
        transaction.save()
        return redirect('dashboard')
    
    income_sources = IncomeSource.objects.filter(user=request.user)
    expense_categories = ExpenseCategory.objects.filter(user=request.user)
    return render(request, 'edit_transaction.html', {'transaction': transaction, 'income_sources': income_sources, 'expense_categories': expense_categories})

@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('dashboard')
    return render(request, 'delete_transaction.html', {'transaction': transaction})


@login_required
def monthly_report(request):
    start_date = timezone.now().replace(day=1)
    end_date = start_date + timedelta(days=30)

    income = Transaction.objects.filter(
        user=request.user,
        date__range=[start_date, end_date],
        income_source__isnull=False
    ).aggregate(total_income=Sum('amount'))['total_income'] or 0

    expenses = Transaction.objects.filter(
        user=request.user,
        date__range=[start_date, end_date],
        expense_category__isnull=False
    ).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

    context = {
        'income': income,
        'expenses': expenses,
        'savings': income - expenses,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'monthly_report.html', context)
    

@login_required
def add_budget(request):
    if request.method == 'POST':
        category_id = request.POST['expense_category']
        amount = request.POST['amount']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        expense_category = ExpenseCategory.objects.get(id=category_id)
        Budget.objects.create(
            user=request.user,
            expense_category=expense_category,
            amount=amount,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('dashboard')

    expense_categories = ExpenseCategory.objects.filter(user=request.user)
    return render(request, 'add_budget.html', {'expense_categories': expense_categories})

@login_required
def budget_progress(request):
    budgets = Budget.objects.filter(user=request.user)
    progress = []
    for budget in budgets:
        spent = Transaction.objects.filter(
            user=request.user,
            expense_category=budget.expense_category,
            date__range=[budget.start_date, budget.end_date]
        ).aggregate(total_spent=Sum('amount'))['total_spent'] or 0

        progress.append({
            'category': budget.expense_category.name,
            'budgeted': budget.amount,
            'spent': spent,
            'remaining': budget.amount - spent
        })

    return render(request, 'budget_progress.html', {'progress': progress})
