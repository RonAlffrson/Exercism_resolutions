"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time: int) -> int:
    #Calculate the bake time remaining.
    """:param elapsed_bake_time: int - elapsed cooking time.
       :return: int - total time elapsed (in minutes) preparing and cooking.

    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

PREPARATION_TIME = 0
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    :param number_of_layers:
    :return:
    """
    return number_of_layers * 2



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

       :param number_of_layers: int - the number of layers in the lasagna.
       :param elapsed_bake_time: int - elapsed cooking time.
       :return: int - total time elapsed (in minutes) preparing and cooking.

       This function takes two integers representing the number of lasagna layers and the
       time already spent baking and calculates the total elapsed minutes spent cooking the
       lasagna.
       """
    return (number_of_layers * 2) + elapsed_bake_time