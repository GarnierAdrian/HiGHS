# [Modelling](@id model-py)

HiGHS has a rudimentry modelling language that allows models to be built and run using `highspy`. 

Below is an example of building a mathematical LP. The functions used are documented in detail below

```math
\begin{aligned}
max \quad & 10x+ 25y\\
s.t.\quad &  x + 2y \leq 80\\
          &  x + 4y \leq 120\\
          &  x,y \geq 0
\end{aligned}
```



```python
import highspy

h = highspy.Highs()
h.silent()

x = h.addVariable()
y = h.addVariable()

h.addConstr(x + 2*y <=  80)
h.addConstr(x + 4*y <= 120)

h.maximize(10*x + 25*y)

print(f"x = {h.val(x)}")
print(f"y = {h.val(y)}")
```
Output:
```
x =  40.0
y =  20.0
```

## Adding Variables

### addVariable

Adds a variable to the model. By default it is continuous,
non-negative, with zero objective coefficient, and has no name
associated with it. It returns a highs_var that can be use later
retrieve the results.

```python
addVariable(lb = 0, ub = kHighsInf, obj = 0, type=HighsVarType.kContinuous, name = None)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lb` | `float` | `0.0` | Lower bound |
| `ub` | `float` | `kHighsInf` | Upper bound |
| `obj` | `float` | `0.0` | Objective coefficient |
| `type` | `HighsVarType` | `kContinuous` | Variable type (continuous, integer, semi-continuous, semi-integer) |
| `name` | `str \| None` | `None` | Optional variable name |


There are additional aliases that encode the other variable types:

```python
addIntegral(lb=0, ub=inf, obj=0.0, name=None)
```

Convenience alias for `addVariable` with `type=HighsVarType.kInteger`.


```python
addBinary(obj=0.0, name=None)
```

Convenience alias for `addVariable` with `lb=0`, `ub=1`, `type=HighsVarType.kInteger`.


### addVariables 

Adds multiple variables in a single call. 

```python
addVariables(*nvars, lb=0, ub=inf, obj=0, type=kContinuous, name=None, name_prefix=None, out_array=True) → HighspyArray | dict`
```

Adds multiple variables in a single call. The first positional arguments define the shape/index set.

**Positional arguments (`*nvars`):**

- **Integer(s):** Defines array dimensions. `addVariables(5)` creates a 1-D array of 5 variables; `addVariables(3, 4)` creates a 3×4 array.
- **Mapping or sequence:** Creates a dictionary of variables keyed by the provided indices.

**Keyword arguments:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lb` | `float \| array \| mapping` | `0` | Lower bound(s) |
| `ub` | `float \| array \| mapping` | `kHighsInf` | Upper bound(s) |
| `obj` | `float \| array \| mapping` | `0` | Objective coefficient(s) |
| `type` | `HighsVarType \| array \| mapping` | `kContinuous` | Variable type(s) |
| `name` | `list[str]` | `None` | Explicit list of names |
| `name_prefix` | `str` | `None` | Prefix; names become `{name_prefix}{index}` |
| `out_array` | `bool` | `True` when all args are int | Return `HighspyArray` instead of dict |



## addConstr

Adds a constraint to the model. It must be defined in terms of a
linear function, with `*` used when there are non-unit
coefficients. By default it has a lower bound of -infinity, an upper
bound of +infinity, and no name associated with it.

```
addConstr(cons, name = None)
```

## maximize

Calls HiGHS to maximize the objective. By default it uses the
objective coefficients defined when the variables were added to the
model. However, a linear function can be passed as an argument.

```
maximize(obj=None)
```

## minimize

Calls HiGHS to minimize the objective. By default it uses the
objective coefficients defined when the variables were added to the
model. However, a linear function can be passed as an argument.

```
minimize(obj=None)
```

## val

Extracts the current value of a particular variable

```
val(var)
```

## vals

Extracts the current values of a particular set of variables

```
vals(vars)
```

## MIP Example




