from random import sample


def shuffle_model(model, numbers=None):
    """
    Shuffle model elements.
    :param model:
    :param numbers:
    :return:
    """
    numbers_object = numbers if numbers else model.objects.count()
    sample_id = sample(range(1, numbers_object + 1), numbers_object)

    return [model.objects.get(pk=pk) for pk in sample_id]
