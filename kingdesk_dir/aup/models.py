from django.db import models

class Wishes(models.Model):
    employer_from = models.TextField('Отправитель', max_length=255, default='')
    wish = models.TextField('Пожелание', max_length=255, null=True, default='')
    employer_to = models.TextField('Получатель', max_length=255, default='')

    def __str__(self):
        return self.employer_to
    
    class Meta:
        verbose_name = 'Пожелание'
        verbose_name_plural = 'Пожелания'

class Employers(models.Model):
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    lastname = models.CharField('Отчество', max_length=100, null=True, default='-')
    username = models.CharField('Логин', max_length=100, default='-')
    gender_id = models.ForeignKey('Genders', on_delete=models.CASCADE, null=True, default=None)
    phone = models.CharField('Phone', max_length=100, null=True, default=None)
    password = models.CharField('Пароль', max_length=100)
    photo = models.ImageField(blank=True, upload_to='images', default=None, null=True)
    post_id = models.ForeignKey('Posts', on_delete=models.CASCADE)
    division_id = models.ForeignKey('Divisions', on_delete=models.CASCADE)

    def __str__(self):
        return self.surname
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Posts(models.Model):
    post_name = models.CharField('Наименование должности', max_length=50)
    post_code = models.CharField('Код должности', max_length=20, default=None)

    def __str__(self):
        return self.post_name
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Divisions(models.Model):
    division_name = models.CharField('Наименование подразделения', max_length=100)
    region = models.CharField('Регион', max_length=100)
    city = models.CharField('Город', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    start_work = models.TimeField('Время начала работы')
    end_work = models.TimeField('Время конца работы')
    is_stop = models.BooleanField('Стоп пожелайки', default=False)

    def __str__(self):
        return self.division_name
    
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

class Current_tasks(models.Model):
    task = models.TextField('Задача', max_length=255, null=True, default='')
    shedule_id = models.ForeignKey('Current_shedules', on_delete=models.CASCADE)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Текущая задача'
        verbose_name_plural = 'Текущие задачи'

class Future_tasks(models.Model):
    task = models.TextField('Задача', max_length=255, null=True, default='')
    shedule_id = models.ForeignKey('Future_shedules', on_delete=models.CASCADE)

    def __int__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Будущая задача'
        verbose_name_plural = 'Будущие задачи'

class Current_shedules(models.Model):
    week_day_id = models.ForeignKey('Week_days', on_delete=models.CASCADE)
    date = models.DateField('Дата')
    employer_id = models.ForeignKey('Employers', on_delete=models.CASCADE)
    start_work = models.TimeField('Время начала смены')
    end_work = models.TimeField('Время окончания смены')
    is_weekend = models.BooleanField('Выходной', default=False)

    def __str__(self):
        return (self.employer_id.surname + ' - ' + self.week_day_id.day_name)
    
    class Meta:
        verbose_name = 'Текущее расписание'
        verbose_name_plural = 'Текущие расписания'
    
class Future_shedules(models.Model):
    week_day_id = models.ForeignKey('Week_days', on_delete=models.CASCADE)
    date = models.DateField('Дата')
    employer_id = models.ForeignKey('Employers', on_delete=models.CASCADE)
    start_work = models.TimeField('Время начала смены')
    end_work = models.TimeField('Время окончания смены')
    comment = models.TextField('Комментарий', max_length=255, null=True, default='')
    is_weekend = models.BooleanField('Выходной', default=False)

    def __str__(self):
        return (self.employer_id.surname + ' - ' + self.week_day_id.day_name)
    
    class Meta:
        verbose_name = 'Будущее расписание'
        verbose_name_plural = 'Будущие расписания'

class Future_shedules_New_Year(models.Model):
    week_day_id = models.ForeignKey('Week_days', on_delete=models.CASCADE)
    date = models.DateField('Дата')
    employer_id = models.ForeignKey('Employers', on_delete=models.CASCADE)
    start_work = models.TimeField('Время начала смены')
    end_work = models.TimeField('Время окончания смены')
    comment = models.TextField('Комментарий', max_length=255, null=True, default='')
    is_weekend = models.BooleanField('Выходной', default=False)

    def __str__(self):
        return (self.employer_id.surname + ' - ' + self.week_day_id.day_name)
    
    class Meta:
        verbose_name = 'Будущее расписание Новый год'
        verbose_name_plural = 'Будущие расписания Новый год'

class Week_days(models.Model):
    day_name = models.CharField('Наименование дня недели', max_length=20)
    alternate_name = models.CharField('Сокращенное наименование дня недели', max_length=2, null=True)

    def __str__(self):
        return self.day_name
    
    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

class Months(models.Model):
    month_name = models.CharField('Наименование месяца', max_length=20)
    alternate_name = models.CharField('Сокращенное наименование месяца', max_length=2, null=True)

    def __str__(self):
        return self.month_name
    
    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'

class Genders(models.Model):
    gender_name = models.CharField('Пол', max_length=10)

    def __str__(self):
        return self.gender_name
    
    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Полы'
