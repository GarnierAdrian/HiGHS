HiPO in Python
==============

The HiPO Interior Point Method (IPM) solver currently uses external dependencies
to provide enhanced performance for linear and quadratic programming problems. 
The required dependencies are packaged in the highspy-extras. The packaged dependencies 
have licensing terms different from HiGHS, such as Apache 2.0. Other algorithms 
may also rely on highspy-extras in the future.

HiPO can enhance performance on many large problem instances. It is not very well 
suited for smaller or easier LPs.

Installation
------------

Install directly:

.. code-block:: console

    (.venv) $ pip install highspy-extras


Or install via the highspy optional dependency:

.. code-block:: console

    (.venv) $ pip install highspy[extras]

At present, the optional dependency installs support needed for HiPO. Both highspy
and highspy-extras are available on PyPI and conda-forge.

Usage
-----

When highspy-extras is installed, HiGHS can use algorithms that depend on these 
external libraries. At present this primarily means the HiPO solver. Note that 
highspy-extras is automatically consumed by highspy and does not need to be imported 
manually. You can explicitly select HiPO:

.. code-block:: python

    import highspy

    # Create a HiGHS instance
    h = highspy.Highs()

    # Load your model
    h.readModel("model.mps")

    # Set solver to use HiPO
    h.setOptionValue("solver", "hipo")

    # Solve
    h.run()

For debugging library packaging issues, you can also query the ABI version 
reported directly by the shared library:

.. code-block:: python

    import highspy_extras

    print(highspy_extras.__version__)
    print(highspy_extras.get_library_version())