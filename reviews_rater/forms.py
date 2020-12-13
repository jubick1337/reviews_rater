from django.forms import Form, CharField, TextInput, ValidationError

from reviews_rater.model_holder import model


class MemoryModelForm(Form):
    review = CharField(
        label='',
        widget=TextInput(attrs={"placeholder": "Enter review"}))

    def clean_review(self, *args, **kwargs):
        review = self.cleaned_data.get('review')
        tokens = review.split(' ')
        if len(tokens) > model.max_len:
            raise ValidationError('Max review size is 128 tokens')
        return review
