from datetime import datetime, date


def year(request):
    """Добавляет переменную с текущим годом."""
    dt = datetime.now().year
    return {
        'year': dt
    }
