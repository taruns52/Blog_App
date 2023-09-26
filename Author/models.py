from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return "media/uploads/user_{0}/{1}".format(instance.username, filename)


class MyAuthor(AbstractUser):
    bio = models.CharField(
        max_length=100,
        verbose_name="Add Bio to let Users know about you",
        default="I'm passionate about using my financial expertise to help people reach their financial goals.",
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Add Your Office Address",
        default="Aranyani, Shop No. Sf 204, 2Nd Floor, Vr Surat, Rundh Village, Dumas Road, Magdalla, Surat, Gujarat",
    )
    phone_no = models.CharField(
        max_length=10, verbose_name="Phone Number", default="9632587410"
    )
    profile_pic = models.ImageField(
        upload_to=user_directory_path,
        verbose_name="Profile Photo",
        default="uploads/default.pic.jpeg",
    )

    def __str__(self):
        return self.username

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
