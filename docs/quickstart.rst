.. currentmodule:: uncle_nelson

Quickstart
===========

This page gives you a brief introduction to the library.
If you don't have the library installed yet, check :doc:`install` first.


Minimal example
----------------

Let's make our first use of the library.

First, create a file called ``main.py`` and add following code (explanation below):

.. code-block:: python3

    from uncle_nelson import calculate_mix, DrugType, IngredientType

    def main():
        mix = calculate_mix(DrugType.meth, [IngredientType.cuke, IngredientType.banana])
        effects = ", ".join(e.value for e in mix.effects)

        print(f"Your custom mix has following effects: {effects}")

    if __name__ == "__main__":
        main()

It's a really basic example, but let's have a look what happens here:

1. First lines imports :func:`.calculate_mix`, :class:`.DrugType`, and :class:`.IngredientType` to calculate a mix.
2. Inside the ``main`` function we call :func:`.calculate_mix` with the :class:`.DrugType` and a list of :class:`.IngredientType` (Note: The order matters, because each ingredient is applied individually).
3. After that we get all the information of the mix, including the effects, price and cost.
4. Finally we execute our ``main`` function.

|

Now let's run the script.

On Linux/MacOS, use

.. code-block:: shell

    python3 main.py

On Windows, use

.. code-block:: shell

    py -3 main.py

This should output something like this ::

    Your custom mix has following effects: Thought-Provoking, Gingeritis
