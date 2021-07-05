from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория клиентов"
        verbose_name_plural = "Категории клиентов"

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    full_name = models.CharField(max_length=255, unique=True, verbose_name="Ф.И.О.")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория клиента"
    )
    image = models.ImageField(upload_to="customer_image/", blank=True, null=True,verbose_name="Фото")
    document = models.FileField(upload_to="customer/", blank=True, null=True, verbose_name="документ")
    birthday = models.DateField(verbose_name="День рождение")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField("Активный", default=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.full_name}"


#Долг
class Debt(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Клиент",
        db_index=True
    )
    sum = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        null=True,
        verbose_name="Сумма долга"
    )
    borrow_date = models.DateTimeField(verbose_name="время выдачи долга", db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    repay_date = models.DateField(verbose_name="Ожидаемая дата оплаты")
    comment = models.CharField(verbose_name="Комментарий", blank=True, null=True, max_length=255)
    is_paid = models.BooleanField(verbose_name="Оплачено")
    is_active = models.BooleanField("Активный")

    class Meta:
        verbose_name = "Долг"
        verbose_name_plural = "Долги"

    def __str__(self):
        return f"{self.customer}-{self.sum}"


class Payment(models.Model):
    debt = models.ForeignKey(
        Debt,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Долг"
    )
    sum = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        null=True,
        verbose_name="Внесенная сумма"
    )
    payment_date = models.DateField(verbose_name="Дата оплаты")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"{self.debt}/ {self.sum}"