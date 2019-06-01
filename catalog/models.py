from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Car(models.Model):

    CAR_TYPES = (
        (1, 'Passenger_car'),
        (2, 'Cargo'),
        (3, 'Bus'),
    )

    title = models.CharField(max_length=50)
    description = models.TextField()
    tipe = models.IntegerField(choices=CAR_TYPES)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'{self.title} from {self.pub_date}'
        return '{self.title} from {self.pub_date}'.format(self=self)

    #~ def __str__(self):
        #~ """
        #~ String for representing the Model object.
        #~ """
        #~ return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('car-detail', args=[str(self.id)])
