from django.contrib import admin
from .models import User, Feedback, Video, TranscriptSegment
# Register your models here.
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Video)
admin.site.register(TranscriptSegment)