from django.db import models
from accounts.models import CustomUser
from config.utils import get_current_date


class FeedbackManager(models.Model):
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text="작성자")
    content = models.TextField(default=None, null=True, help_text="메모 내용")
    created_at = models.DateField(default=get_current_date, help_text="생성 일자")

    class Meta:
        verbose_name = "메모"
        verbose_name_plural = "메모"


class BloodSugarManager(models.Model):
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text="작성자")
    empty_stomach = models.PositiveIntegerField(default=0, help_text="공복")
    morning = models.PositiveIntegerField(default=0, help_text="아침")
    lunch = models.PositiveIntegerField(default=0, help_text="점심")
    evening = models.PositiveIntegerField(default=0, help_text="저녁")
    feedback = models.ForeignKey(FeedbackManager, on_delete=models.CASCADE, help_text="메모", null=True)
    created_at = models.DateField(default=get_current_date, help_text="생성 일자")

    @property
    def is_empty_stomach_warning(self):
        return not (0 == self.empty_stomach or 70 <= self.empty_stomach <= 100)

    @property
    def is_morning_warning(self):
        return not (0 == self.morning or 90 <= self.morning <= 140)

    @property
    def is_lunch_warning(self):
        return not (0 == self.lunch or 90 <= self.lunch <= 140)

    @property
    def is_evening_warning(self):
        return not (0 == self.evening or 90 <= self.evening <= 140)

    class Meta:
        verbose_name = "혈당 관리"
        verbose_name_plural = "혈당 관리"
