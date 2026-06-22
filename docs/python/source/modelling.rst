Modelling
=========

HiGHS has a rudimentry modelling language that allows models to be built and run using `highspy`. 

Below is an example of building a mathematical LP. The functions used are documented in detail below

.. math::

   \begin{aligned}
    max \quad & 10 x_1 + 25 x_2\\
    s.t. \quad &   x_1 +  2 x_2 \leq  80\\
                &  x_1 +  4 x_2 \leq 120\\
                &  x_1,     x_2 \geq   0\\
    \end{aligned}

.. code-block:: python
        
    # model and solve the LP
    import highspy

    h = highspy.Highs()
    h.silent()

    x1 = h.addVariable()
    x2 = h.addVariable()

    h.addConstr(x1 + 2*x2 <=  80)
    h.addConstr(x1 + 4*x2 <= 120)

    h.maximize(10*x1 + 25*x2)

    print(f"x1 = {h.val(x1)}")
    print(f"x2 = {h.val(x2)}")

Expected output:

.. code-block:: console

    x1 = 40
    x2 = 20


:meth:`highspy.Highs.addVariable`
---------------------------------

Adds a variable to the model. By default it is continuous,
non-negative, with zero objective coefficient, and has no name
associated with it.

.. code-block:: python

    addVariable(lb = 0, ub = kHighsInf, obj = 0, type=HighsVarType.kContinuous, name = None)

:meth:`highspy.Highs.addConstr`
-------------------------------

Adds a constraint to the model. It must be defined in terms of a
linear function, with `*` used when there are non-unit
coefficients. By default it has a lower bound of -infinity, an upper
bound of +infinity, and no name associated with it.

.. code-block:: python

    addConstr(cons, name = None)

:meth:`highspy.Highs.maximize`
------------------------------

Calls HiGHS to maximize the objective. By default it uses the
objective coefficients defined when the variables were added to the
model. However, a linear function can be passed as an argument.

.. code-block:: python

    maximize(obj=None)

:meth:`highspy.Highs.minimize`
------------------------------

Calls HiGHS to minimize the objective. By default it uses the
objective coefficients defined when the variables were added to the
model. However, a linear function can be passed as an argument.

.. code-block:: python

    minimize(obj=None)

:meth:`highspy.Highs.val`
-------------------------

Extracts the current value of a particular variable

.. code-block:: python

    val(var)


:meth:`highspy.Highs.vals`
--------------------------

Extracts the current values of a particular set of variables

.. code-block:: python

    vals(vars)

