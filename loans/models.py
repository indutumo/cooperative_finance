from django.db import models
from members.models import Member
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

STATUS_CHOICE = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    )

ACCOUNT_STATUS_CHOICE = (
       	    ('Deactivated', 'Deactivated'),
            ('Activated', 'Activated'),
            )


class LoanAccount(models.Model):
    owner = models.OneToOneField(Member, on_delete=models.CASCADE)
    total_principal = models.PositiveIntegerField()
    status = models.CharField(choices=ACCOUNT_STATUS_CHOICE, default='Deactivated', max_length=11)

    def __str__(self):
        return self.owner.first_name

class LoanIssue(models.Model):
    account = models.ForeignKey(LoanAccount, on_delete=models.CASCADE)
    loan_num = models.CharField(unique=True, max_length=255)
    principal = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_CHOICE, default='Pending', max_length=15)

    def __str__(self):
        return self.account.owner.first_name

class LoanPayment(models.Model):
    loan_num = models.ForeignKey(LoanIssue, on_delete=models.CASCADE)
    principal = models.PositiveIntegerField()

    def __str__(self):
        return self.loan_num.account.owner.first_name

class LoanDelete(models.Model):
    tran_type = models.CharField(max_length=10)
    principal = models.PositiveIntegerField()
    loan_num = models.CharField(max_length=256)
    account = models.CharField(max_length=256)

    def __str__(self):
        return self.account

@receiver(post_save, sender=Member)
def create_account(sender, **kwargs):
    if kwargs['created']:
        LoanAccount.objects.create(owner=kwargs['instance'],total_principal=0)


