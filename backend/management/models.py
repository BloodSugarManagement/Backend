from django.db import models
from accounts.models import CustomUser
from config.utils import get_current_date
from management.services import warning_thresold


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
    before_morning = models.PositiveIntegerField(default=0, help_text="아침 식전")
    after_morning = models.PositiveIntegerField(default=0, help_text="아침 식후")
    before_lunch = models.PositiveIntegerField(default=0, help_text="점심 식전")
    after_lunch = models.PositiveIntegerField(default=0, help_text="점심 식후")
    before_evening = models.PositiveIntegerField(default=0, help_text="저녁 식전")
    after_evening = models.PositiveIntegerField(default=0, help_text="저녁 식후")
    feedback = models.ForeignKey(FeedbackManager, on_delete=models.CASCADE, help_text="메모", null=True)
    created_at = models.DateField(default=get_current_date, help_text="생성 일자")

    @property
    def is_empty_stomach_warning(self):
        return warning_thresold(self.empty_stomach, 70, 100)

    @property
    def is_before_morning_warning(self):
        return warning_thresold(self.before_morning, 90, 140)

    @property
    def is_after_morning_warning(self):
        return warning_thresold(self.after_morning, 90, 140)

    @property
    def is_before_lunch_warning(self):
        return warning_thresold(self.before_lunch, 90, 140)

    @property
    def is_after_lunch_warning(self):
        return warning_thresold(self.after_lunch, 90, 140)

    @property
    def is_before_evening_warning(self):
        return warning_thresold(self.before_evening, 90, 140)

    @property
    def is_after_evening_warning(self):
        return warning_thresold(self.after_evening, 90, 140)

    class Meta:
        verbose_name = "혈당 관리"
        verbose_name_plural = "혈당 관리"
