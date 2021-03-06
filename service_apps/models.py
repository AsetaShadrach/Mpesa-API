from django.db import models
from collections import OrderedDict
import uuid

class ServiceApp(models.Model):
    creator = models.CharField(max_length=50, default="Not Given" )
    app_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    app_name = models.CharField(max_length=50, unique=True, blank=False)
    active = models.BooleanField(default=False)
    # tr -> transaction
    # l --> last
    # d --> day(s)
    tr_count_l_d = models.IntegerField(default=0)
    tr_count_l_7d = models.IntegerField(default=0)
    tr_count_l_30d = models.IntegerField(default=0)
    tr_cum_sum_l_d = models.FloatField(default=0)
    tr_cum_sum_l_7d = models.FloatField(default=0)
    tr_cum_sum_l_30d = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # The Json file should have
    # - progressive monthly figures
    # -- Note : the default for JSONField must be a callable
    service_details = models.JSONField(default=OrderedDict)

    class Meta:
        db_table = 'service_apps'
        verbose_name_plural = 'service_apps'
        ordering = ['-created_at']

    
    def __str__(self):
        return str(f'''AppID :{self.app_id},
                        CreatedAt : {self.created_at},
                        Creator :{self.creator},
                        Active : {self.active}
                        ''')
        