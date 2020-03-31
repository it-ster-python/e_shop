from django import forms
from blog import models


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = "__all__"
        exclude = ["add_time"]
        widgets = {
            "comment_article": forms.HiddenInput(),
            "comment_text": forms.Textarea(
                attrs={
                    "id": "message",
                    "class": "form-control"
                }
            )
        }

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data


# def clean(self):
#         if self.cleaned_data.get('login') in list_closed_login:
#             self.add_error('login', 'Данное имя пользователя закрыто для регистрации')
#             raise forms.ValidationError('Ошибка ввода')
#         try:
#             user = User.objects.get(login=self.cleaned_data.get('login'))
#         except User.DoesNotExist:
#             if not match(LOGIN, self.cleaned_data.get('login')):
#                 self.add_error('login', 'Допускаются только латинские символы и _')
#                 raise forms.ValidationError('Ошибка ввода')
#         else:
#             self.add_error('login', 'Имя пользователя {} уже занято'.format(user.login))
#             raise forms.ValidationError('Ошибка ввода')

#         if not match(NAME, self.cleaned_data.get('name')):
#             self.add_error('name', 'Допускаются только русские, латинские символы')
#             raise forms.ValidationError('Ошибка ввода')

#         if not match(NAME, self.cleaned_data.get('family')):
#             self.add_error('family', 'Допускаются только русские, латинские символы')
#             raise forms.ValidationError('Ошибка ввода')

#         if not match(EMAIL, self.cleaned_data.get('email')):
#             self.add_error('email', 'Email не соответствует шаблону')
#             raise forms.ValidationError('Ошибка ввода')

#         if not match(PHONE, self.cleaned_data.get('telephone')):
#             self.add_error('telephone', 'Номер не соответствует шаблону')
#             raise forms.ValidationError('Ошибка ввода')

#         try:
#             country = Country.objects.get(name_ru=self.cleaned_data.get('country'))
#         except Country.DoesNotExist:
#             self.add_error('country', 'Данной страны нет в базе данных')
#             raise forms.ValidationError('Ошибка ввода')
#         else:
#             pass

#         try:
#             region = Region.objects.get(
#                 country_id=country.id,
#                 name_ru=self.cleaned_data.get('region')
#             )
#         except Region.DoesNotExist:
#             self.add_error('region', 'Данного региона / области нет в базе данных')
#             raise forms.ValidationError('Ошибка ввода')
#         else:
#             pass

#         try:
#             district = District.objects.get(
#                 region_id=region.id,
#                 name_ru=self.cleaned_data.get('district')
#             )
#         except District.DoesNotExist:
#             self.add_error('district', 'Данного районного центра нет в базе данных')
#             raise forms.ValidationError('Ошибка ввода')
#         else:
#             pass

#         try:
#             City.objects.get(
#                 district_id=district.id,
#                 name_ru=self.cleaned_data.get('city')
#             )
#         except City.DoesNotExist:
#             self.add_error('city', 'Данного населенного пункта нет в базе данных')
#             raise forms.ValidationError('Ошибка ввода')
#         else:
#             pass

#         if not match(STREET, self.cleaned_data.get('street')):
#             self.add_error('street', 'Используются не поддерживаемые символы')
#             raise forms.ValidationError('Ошибка ввода')

#         if not match(PASSWORD, self.cleaned_data.get('password')):
#             self.add_error('password', 'Пароль от 8-и до 50-и символов')
#             raise forms.ValidationError('Ошибка ввода ')

#         if self.cleaned_data.get('password') != self.cleaned_data.get('password_repeat'):
#             self.add_error('password_repeat', 'Пароли не совподают')
#             raise forms.ValidationError('Ошибка ввода')
#         if not self.cleaned_data.get('agreement'):
#             self.add_error('agreement', 'Для регистрации необходимо принять условия использования')
#             raise forms.ValidationError('Ошибка ввода')

#         return self.cleaned_data