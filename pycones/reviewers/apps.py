from django.apps import AppConfig


class ReviewersConfig(AppConfig):
    name = "reviewers"
    verbose_name = "Reviewers"

    def ready(self):
        import reviewers.signals.handlers
