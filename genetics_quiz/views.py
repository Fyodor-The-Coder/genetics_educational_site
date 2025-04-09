import random
from django.shortcuts import render, redirect
from genetics_dictionary.models import Term

def start_quiz(request):
    return render(request, "start_quiz.html")

def begin_quiz(request):
    request.session['quiz'] = {
        'total': 5,
        'current': 1,
        'correct': 0,
        'used': []
    }
    return redirect('quiz')

def quiz(request):
    session = request.session.get('quiz')
    if not session:
        return redirect('start_quiz')

    if request.method == 'POST':
        if str(request.session.get('correct_id')) == request.POST.get('answer'):
            session['correct'] += 1
        session['current'] += 1
        request.session.modified = True

    if session['current'] > session['total']:
        return redirect('results')

    term = Term.objects.exclude(term_id__in=session['used']).order_by('?').first()
    definitions = list(
        Term.objects.exclude(term_id=term.term_id)
                   .order_by('?')[:3]
    ) + [term]
    random.shuffle(definitions)

    session['used'].append(term.term_id)
    request.session['correct_id'] = term.term_id
    request.session.modified = True

    return render(request, 'quiz.html', {
        'term': term.term_ru,
        'definitions': definitions,
        'progress': session
    })

def results(request):
    quiz_data = request.session.get('quiz', {})
    correct = quiz_data.get('correct', 0)
    total = quiz_data.get('total', 5)
    percentage = round((correct / total) * 100) if total > 0 else 0

    if 'quiz' in request.session:
        del request.session['quiz']
    return render(request, 'results.html', {
        'correct': correct,
        'total': total,
        'percentage': percentage
    })