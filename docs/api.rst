.. currentmodule:: uncle_nelson

:tocdepth: 3

API Reference
==============

This section provides a detailed overview of the API of uncle-nelson.


Mix
-------

.. autofunction:: uncle_nelson.mix.calculate_mix

.. class:: Mix

    A namedtuple which represents a calculated mix.

    .. attribute:: drug

        The type of drug.

        :type: :class:`DrugType`

    .. attribute:: ingredients

        A list of added ingredients.

        :type: List[:class:`IngredientType`]

    .. attribute:: effects

        A list of effects the mixed drug has.

        :type: List[:class:`EffectType`]

    .. attribute:: price

        The (suggested) sell price of the mixed drug.

        :type: :class:`int`

    .. attribute:: cost

        The ingredients cost of the mixed drug.

        :type: :class:`int`


Enumerations
-------------
All enumerations inherit from :class:`enum.Enum`.

DrugType
~~~~~~~~~~~~~~

.. class:: DrugType

    Specifies the type of a drug.

    .. attribute:: og_kush

        OG Kush weed.

    .. attribute:: sour_diesel

        Sour Diesel weed.

    .. attribute:: green_crack

        Green Crack weed.

    .. attribute:: granddaddy_purple

        Granddaddy Purple weed.

    .. attribute:: methamphetamine

        Methamphetamine.

    .. attribute:: meth

        Alias of :attr:`methamphetamine`.

    .. attribute:: cocaine

        Cocaine.

IngredientType
~~~~~~~~~~~~~~

.. class:: IngredientType

    Specifies the type of ingredient.

    .. attribute:: cuke

        Cuke ingredient.

    .. attribute:: banana

        Banana ingredient.

    .. attribute:: paracetamol

        Paracetamol ingredient.

    .. attribute:: donut

        Donut ingredient.

    .. attribute:: viagra

        Viagra ingredient.

    .. attribute:: mouth_wash

        Mouth Wash ingredient.

    .. attribute:: flu_medicine

        Flu Medicine ingredient.

    .. attribute:: gasoline

        Gasoline ingredient.

    .. attribute:: energy_drink

        Energy Drink ingredient.

    .. attribute:: motor_oil

        Motor Oil ingredient.

    .. attribute:: mega_bean

        Mega Bean ingredient.

    .. attribute:: chili

        Chili ingredient.

    .. attribute:: battery

        Battery ingredient.

    .. attribute:: iodine

        Iodine ingredient.

    .. attribute:: addy

        Addy ingredient.

    .. attribute:: horse_semen

        Horse Semen ingredient.

EffectType
~~~~~~~~~~

.. class:: EffectType

    Specifies the type of effect.

    .. attribute:: anti_gravity

        Anti-Gravity effect.

    .. attribute:: athletic

        Athletic effect.

    .. attribute:: balding

        Balding effect.

    .. attribute:: bright_eyed

        Bright-Eyed effect.

    .. attribute:: calming

        Calming effect.

    .. attribute:: calorie_dense

        Calorie-Dense effect.

    .. attribute:: cyclopean

        Cyclopean effect.

    .. attribute:: disorienting

        Disorienting effect.

    .. attribute:: electrifying

        Electrifying effect.

    .. attribute:: energizing

        Energizing effect.

    .. attribute:: euphoric

        Euphoric effect.

    .. attribute:: explosive

        Explosive effect.

    .. attribute:: focused

        Focused effect.

    .. attribute:: foggy

        Foggy effect.

    .. attribute:: gingeritis

        Gingeritis effect.

    .. attribute:: glowing

        Glowing effect.

    .. attribute:: jennerising

        Jennerising effect.

    .. attribute:: laxative

        Laxative effect.

    .. attribute:: lethal

        Lethal effect.

    .. attribute:: long_faced

        Long-Faced effect.

    .. attribute:: munchies

        Munchies effect.

    .. attribute:: paranoia

        Paranoia effect.

    .. attribute:: refreshing

        Refreshing effect.

    .. attribute:: schizophrenic

        Schizophrenic effect.

    .. attribute:: sedating

        Sedating effect.

    .. attribute:: seizure_inducing

        Seizure-Inducing effect.

    .. attribute:: shrinking

        Shrinking effect.

    .. attribute:: slippery

        Slippery effect.

    .. attribute:: smelly

        Smelly effect.

    .. attribute:: sneaky

        Sneaky effect.

    .. attribute:: spicy

        Spicy effect.

    .. attribute:: thought_provoking

        Thought-Provoking effect.

    .. attribute:: toxic

        Toxic effect.

    .. attribute:: tropic_thunder

        Tropic Thunder effect.

    .. attribute:: zombifying

        Zombifying effect.