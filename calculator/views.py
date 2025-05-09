from django.shortcuts import render

def home(request):
    result = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
            elif operation == 'modulo':
                result = num1 % num2 if num2 != 0 else "Cannot modulo by zero"
            elif operation == 'percentage':
                result = (num1 * num2) / 100
            else:
                result = "Invalid operation"
        except Exception as e:
            result = f"Error: {e}"

    return render(request, 'calculator/home.html', {'result': result})
