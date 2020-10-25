from django.contrib import admin

# Register your models here.
from .models import SkillModel,PersonalModel

from .models import PortfolioModel

from .models import BlogModel




admin.site.register(SkillModel)

admin.site.register(PersonalModel)

admin.site.register(PortfolioModel)
admin.site.register(BlogModel)
