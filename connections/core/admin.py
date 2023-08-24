from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount         # 7)  11)  13)
# Register your models here.

admin.site.register(Profile)        # 7)
admin.site.register(Post)        # 11)
admin.site.register(LikePost)        # 13)

admin.site.register(FollowersCount)