from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Tag, Scope, Article


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_count += 1
            else:
                is_main_count == 0
        if is_main_count > 1:
            raise ValidationError('Основным может быть только один раздел.')
        if is_main_count == 0:
            raise ValidationError('Укажите основной раздел.')
        return super().clean() 

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at', 'image']
    inlines = [ScopeInline]
    
@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    model = Scope
    list_display = ['id', 'tag', 'article', 'is_main']
    extra = 0
    