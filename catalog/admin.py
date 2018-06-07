from django.contrib import admin
from .models import  ITOperation, ITManagement, ITGovernance,CorpGovernance

admin.site.register(ITOperation)
admin.site.register(ITManagement)
admin.site.register(ITGovernance)
admin.site.register(CorpGovernance)
