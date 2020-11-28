import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Post(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # referral_code = models.UUIDField(default=uuid.uuid4,  editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


def increment_invoice_number():
    """
    last_invoice = TestPost.objects.all().order_by('id').last()
    if not last_invoice:
        return 'MAG0001'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('MAG')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = 'MAG' + str(new_invoice_int)
    return new_invoice_no
    """
    # GET Current Date
    today = datetime.date.today()

    # Format the date like (20-11-28 YY-MM-DD)
    today_string = today.strftime('%y%m%d')

    # For the very first time invoice_number is YY-MM-DD-001
    next_invoice_number = '001'

    # Get Last Invoice Number of Current Year, Month and Day (20-11-28 YY-MM-DD)
    last_invoice = TestPost.objects.filter(invoice_no__startswith=today_string).order_by('invoice_no').last()

    if last_invoice:
        # Cut 6 digit from the left and converted to int (201128:xxx)
        last_invoice_number = int(last_invoice.invoice_no[6:])

        # Increment one with last three digit
        next_invoice_number = '{0:03d}'.format(last_invoice_number + 1)

    # Return custom invoice number
    return today_string + next_invoice_number


class TestPost(models.Model):
    invoice_no = models.CharField(max_length=9,
                                  default=increment_invoice_number,
                                  null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
