from django.db import models


#Модель для смены контактных данных
#Электронной почты и телефона
class Contacts(models.Model):
    email = models.EmailField(max_length=254, verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    class Meta:
        verbose_name="Контактные данные компании (телефон и электронная почта)"
        verbose_name_plural="Контактные данные компании (телефон и электронная почта)"

    def __str__(self):
        return self.email


#Модель для смены изображения и названия
#Для отчета 1-ИЛ
class il_1(models.Model):
    about = models.CharField(max_length=400, verbose_name="Название отчета")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default="", verbose_name="Фотография для 1-ИЛ для арендаторов лесных участков")

    class Meta:
        verbose_name="Материалы ДЗ к отчету 1-ИЛ"
        verbose_name_plural="Материалы ДЗ к отчету 1-ИЛ"

    def __str__(self):
        return self.about

#Модель для смены изображения и названия
#Для отчета 1-ВЛ
class vl_1(models.Model):
    about = models.CharField(max_length=400, verbose_name="Название отчета")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фотография для 1-ВЛ для арендаторов лесных участков")

    class Meta:
        verbose_name="Материалы ДЗ к отчету 1-ВЛ"
        verbose_name_plural="Материалы ДЗ к отчету 1-ВЛ"


#Модель для смены изображения и названия
#Для отчета 1-ИЛ для граждан
class il_1_citizen(models.Model):
    about = models.CharField(max_length=400, verbose_name="Название отчета")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фотография для 1-ИЛ для граждан (заготовка древесины для собственных нужд)")

    class Meta:
        verbose_name="Материалы ДЗ к отчету 1-ИЛ для граждан"
        verbose_name_plural="Материалы ДЗ к отчету 1-ИЛ для граждан"


#Модель для смены стоимости работы
#при заказе до 300 штук
class price_300(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="Стоимость")

    class Meta:
        verbose_name="Цена при заказе до 300 штук материалов ДЗ"
        verbose_name_plural="Цена при заказе до 300 штук материалов ДЗ"

    def __str__(self):
        return str(self.price)


#Модель для смены стоимости работы
#при заказе от 301 штуки
class price_301(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="Стоимость")

    class Meta:
        verbose_name="Цена при заказе от 301 штуки материалов ДЗ"
        verbose_name_plural="Цена при заказе от 301 штуки материалов ДЗ"

    def __str__(self):
        return str(self.price)


#Модель для смены стоимости работы
#для граждан
class price_citizen(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="Стоимость")

    class Meta:
        verbose_name="Цена для граждан осуществляющих заготовку древесины для собственных нужд"
        verbose_name_plural="Цена для граждан осуществляющих заготовку древесины для собственных нужд"

    def __str__(self):
        return str(self.price)


#Модель для сохранения контактов заявки
#в базе арендованных
class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    email = models.EmailField(max_length=254, verbose_name="Электронная почта", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    dztype = models.CharField(max_length=150, default="",verbose_name="Тип материалов ДЗ")

    class Meta:
        verbose_name="Контактные данные заказчиков"
        verbose_name_plural="Контактные данные заказчиков"

    def __str__(self):
        return str(self.name)
