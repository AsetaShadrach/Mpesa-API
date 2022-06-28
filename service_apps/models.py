from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ServiceApps(models.Model):
    creator = models.CharField(max_length=50, null=True )
    app_id = models.CharField(max_length=50, primary_key=True)
    app_name = models.CharField(max_length=50, null=True)
    active = models.BooleanField(default=False)
    # The Json file should have
    # - current daily figures 
    # - progressive monthly figures
    # -- Note : the default for JSONField must be a callable
    service_details = models.JSONField(default=dict)
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
    change_description = models.CharField(max_length=150, null=True)

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
        