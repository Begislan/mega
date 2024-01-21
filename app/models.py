from django.db import models
class Abonent(models.Model):
    name_abonent = models.CharField(max_length=250, verbose_name="Абонент")
    number = models.IntegerField()
    tarif = models.CharField(max_length=250, verbose_name="тарифный план")
    balance = models.IntegerField(default=0, verbose_name="обший баланс")
    min = models.IntegerField(default=0, verbose_name="обший минута")
    sms = models.IntegerField(default=0, verbose_name="обший смс")
    in_min = models.IntegerField(default=0, verbose_name="минуты внутри сети")
    vne_min = models.IntegerField(default=0, verbose_name="минуты вне сети")
    in_sms = models.IntegerField(default=0, verbose_name="смс")
    internet = models.IntegerField(default=0, verbose_name="интернет")

    

    class Meta:
        verbose_name = ("Абоненты")
        verbose_name_plural = ("Абоненты")

    def __str__(self):
        return f"{self.name_abonent} | {self.number}"

   
class News(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    full = models.TextField()
    img = models.ImageField()

    class Meta:
        verbose_name = ("Новости")
        verbose_name_plural = ("Новости")

    def __str__(self):
        return self.title
