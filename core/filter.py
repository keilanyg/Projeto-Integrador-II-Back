from django_filters import rest_framework as filters
from livros.models import Emprestimo
from datetime import timezone, timedelta
from dateutil.relativedelta import relativedelta 

class EmprestimoUsuarioFilter(filters.FilterSet):
    period = filters.ChoiceFilter(choices=[('day', 'Dia'), ('week', 'Semana'), ('month', 'Mês')], method='filter_by_period')

    def filter_by_period(self, queryset, name, value):
        user = self.request.user
        today = timezone.now().date()

        if value == 'day':
            return queryset.filter(usuario=user, data_emprestimo=today)
        elif value == 'week':
            week_start = today - timedelta(days=today.weekday())
            week_end = week_start + timedelta(days=6)
            return queryset.filter(usuario=user, data_emprestimo__range=[week_start, week_end])
        elif value == 'month':
            month_start = today.replace(day=1)
            month_end = (month_start + relativedelta(months=1)) - timedelta(days=1)
            return queryset.filter(usuario=user, data_emprestimo__range=[month_start, month_end])

        return queryset

    class Meta:
        model = Emprestimo
        fields = ['period']
