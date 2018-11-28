from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, EmailField, CharField, Textarea, ModelForm, URLField, HiddenInput, IntegerField, ModelChoiceField, TypedChoiceField

from walker_panel.models import Task, City


class SignUpForm(UserCreationForm):
    username = EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Email')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class TaskForm(ModelForm):
    name = CharField(widget=HiddenInput(), required=False)
    id = IntegerField(widget=HiddenInput(), required=False)
    search_query = CharField(label='Поисковый запрос',
                             help_text='*по этому запросу мы будем искать сайт в Яндексе')
    target_url = URLField(label='Целевой сайт',
                          help_text=f'*на этом сайте мы будем проводить больше всего времени '
                                    f'и выполнять целевые действия')
    competitor_sites = CharField(label="Сайты конкурентов (в столбик)", widget=Textarea(attrs={}),
                                 help_text='*эти сайты мы будем быстро покидать')
    region = ModelChoiceField(queryset=City.objects.all(), empty_label='', label='Указать регион', initial='')
    delay = IntegerField(label='Задержка', help_text='Запускать не чаще, чем раз в n минут')
    launches_per_day = IntegerField(label='Количество запусков в день',
                                    help_text='Максимальное количество запусков в день (0 — без ограничений)')

    class Meta:
        model = Task
        fields = ['name', 'id', 'search_query', 'target_url', 'competitor_sites', 'region', 'delay', 'launches_per_day']


class ProxyForm(Form):
    proxies = CharField(label='Список прокси', help_text='Прокси в формате host:port:username:password',
                        widget=Textarea(attrs={'placeholder': 'host:port:username:password'}))

    class Meta:
        fields = ['proxies']
