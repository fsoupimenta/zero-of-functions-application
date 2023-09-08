# Zero of Functions Application 📈
This program is an application of the main methods of numerical calculation for finding the approximation of the roots of a function, where you can follow the variations of the values in a table according to each method, as well as the final approximation found according to the error and the number of iterations required.

## Roots of Functions
Let $f$ be a continuous function on the interval $[a, b]$, such that $f(a)$ and $f(b)$ have opposite signs. By the [Intermediate Value Theorem](https://byjus.com/maths/intermediate-value-theorem/), there exists a number $c$ between $a$ and $b$ such that $f(c) = 0$, that is, $f$ has at least one root between $a$ and $b$. 

Next, we'll look at the main numerical methods for finding an approximation to the root $c$.

### [Bisection method](https://byjus.com/maths/bisection-method/) 
The bisection method consists of dividing the interval $[a, b]$ in half, thus obtaining the number $c1 = \frac{a + b}{2}$.
Calculate the value $f(c1)$. 

If $f(c1)$ and $f(a)$ have opposite signs, take $c2 = \frac{a + c1}{2}$, and if $f(c1)$ and $f(b)$ which have opposite signs, we take $c2 = \frac{c1 + b}{2}$.
After calculating the value of $f(c2)$ and checking whether it is positive or negative, we divide again the previous interval in half, obtaining the point $c3$. 

Repeating this process produces a sequence of numbers $c1, c2, c3, c4, c5, . . . -→ c$ that `converges` to the root $c$.

### [Secant method](https://byjus.com/maths/secant-method/)
Lorem ipsum

### [Newton method](https://learn.saylor.org/mod/book/view.php?id=37482&chapterid=21131)
Lorem ipsum

## Tecnologies 🔧
- [Python](https://www.python.org)
- [PyQt6](https://pypi.org/project/PyQt6/)
- [SymPy](https://www.sympy.org/en/index.html)

## Usage 💻
Lorem ipsum
