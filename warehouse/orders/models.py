from django.db import models


class Order(models.Model):
    order_name = models.CharField(max_length=30, unique=True, verbose_name="Order name")

    class Status(models.TextChoices):
        NEW = 'New', 'New'
        PROCESS = 'In Process', 'In Process'
        STORED = 'Stored', 'Stored'
        COMPLETE = 'Complete', 'Complete'

    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.NEW,
    )

    def __str__(self) -> str:
        return f"{self.order_name} - {self.status}"
