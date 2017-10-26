from utils.choices import ChoiceEnum


class Choices(ChoiceEnum):
    choice1 = 'choice1_value'
    choice2 = 'choice2_value'
    choice3 = 'choice3_value'


def test_enum_as_choices():
    choices = Choices.choices()
    choices_expected = (
        ('choice1', 'choice1_value'),
        ('choice2', 'choice2_value'),
        ('choice3', 'choice3_value'),
    )

    assert choices == choices_expected
