<h1>0x03. Python - Data Structures: Lists, Tuples</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What are lists and how to use them</li>
<li>What are the differences and similarities between strings and lists</li>
<li>What are the most common methods of lists and how to use them</li>
<li>How to use lists as stacks and queues</li>
<li>What are list comprehensions and how to use them</li>
<li>What are tuples and how to use them</li>
<li>When to use tuples versus lists</li>
<li>What is a sequence</li>
<li>What is tuple packing</li>
<li>What is sequence unpacking</li>
<li>What is the <code>del</code> statement and how to use it</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Print a list of integers
  </h3>
  <p>Write a function that prints all integers of a list.</p>
<ul>
<li>Prototype: <code>def print_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>
        <p>File: <code>0-print_list_integer.py</code></p>
  <h3>
    1. Secure access to an element in a list
  </h3>
  <p>Write a function that retrieves an element from a list like in C.</p>
<ul>
<li>Prototype: <code>def element_at(my_list, idx):</code></li>
<li>If <code>idx</code> is negative, the function should return <code>None</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return <code>None</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>
        <p>File: <code>1-element_at.py</code></p>
  <h3>
    2. Replace element
  </h3>
  <p>Write a function that replaces an element of a list at a specific position (like in C).</p>
<ul>
<li>Prototype: <code>def replace_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should not modify anything, and returns the original list</li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should not modify anything, and returns the original list</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>
        <p>File: <code>2-replace_in_list.py</code></p>
  <h3>
    3. Print a list of integers... in reverse!
  </h3>
  <p>Write a function that prints all integers of a list, in reverse order.</p>
<ul>
<li>Prototype: <code>def print_reversed_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>
        <p>File: <code>3-print_reversed_list_integer.py</code></p>
  <h3>
    4. Replace in a copy
  </h3>
  <p>Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).</p>
<ul>
<li>Prototype: <code>def new_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should return a copy of the original <code>list</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return a copy of the original <code>list</code></li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>
        <p>File: <code>4-new_in_list.py</code></p>
  <h3>
    5. Can you C me now?
  </h3>
  <p>Write a function that removes all characters <code>c</code> and <code>C</code> from a string.</p>
<ul>
<li>Prototype: <code>def no_c(my_string):</code></li>
<li>The function should return the new string</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.replace()</code></li>
</ul>
        <p>File: <code>5-no_c.py</code></p>
  <h3>
    6. Lists of lists = Matrix
  </h3>
  <p>Write a function that prints a matrix of integers.</p>
<ul>
<li>Prototype: <code>def print_matrix_integer(matrix=[[]]):</code></li>
<li>Format: see example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>
        <p>File: <code>6-print_matrix_integer.py</code></p>
  <h3>
    7. Tuples addition
  </h3>
  <p>Write a function that adds 2 tuples.</p>
<ul>
<li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code></li>
<li>Returns a tuple with 2 integers:
<ul>
<li>The first element should be the addition of the first element of each argument</li>
<li>The second element should be the addition of the second element of each argument</li>
</ul></li>
<li>You are not allowed to import any module</li>
<li>You can assume that the two tuples will only contain integers</li>
<li>If a tuple is smaller than 2, use the value <code>0</code> for each missing integer</li>
<li>If a tuple is bigger than 2, use only the first 2 integers</li>
</ul>
        <p>File: <code>7-add_tuple.py</code></p>
  <h3>
    8. More returns!
  </h3>
  <p>Write a function that returns a tuple with the length of a string and its first character.</p>
<ul>
<li>Prototype: <code>def multiple_returns(sentence):</code></li>
<li>If the sentence is empty, the first character should be equal to <code>None</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>8-multiple_returns.py</code></p>
  <h3>
    9. Find the max
  </h3>
  <p>Write a function that finds the biggest integer of a list. </p>
<ul>
<li>Prototype: <code>def max_integer(my_list=[]):</code></li>
<li>If the list is empty, return <code>None</code></li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use the builtin <code>max()</code></li>
</ul>
        <p>File: <code>9-max_integer.py</code></p>
  <h3>
    10. Only by 2
  </h3>
  <p>Write a function that finds all multiples of 2 in a list.</p>
<ul>
<li>Prototype: <code>def divisible_by_2(my_list=[]):</code></li>
<li>Return a new list with <code>True</code> or <code>False</code>, depending on whether the integer at the same position in the original list is a multiple of 2</li>
<li>The new list should have the same size as the original list</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>10-divisible_by_2.py</code></p>
  <h3>
    11. Delete at
  </h3>
  <p>Write a function that deletes the item at a specific position in a list.</p>
<ul>
<li>Prototype: <code>def delete_at(my_list=[], idx=0):</code></li>
<li>If <code>idx</code> is negative or out of range, nothing change (returns the same list)</li>
<li>You are not allowed to use <code>pop()</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>11-delete_at.py</code></p>
  <h3>
    12. Switch
  </h3>
  <p>Complete the source code in order to switch value of <code>a</code> and <code>b</code></p>
<ul>
<li>You can find the source code here</li>
<li>Your code should be inserted where the comment is (line 4)</li>
<li>Your program should be exactly 5 lines long</li>
</ul>
        <p>File: <code>12-switch.py</code></p>
  <h3>
    13. Linked list palindrome
  </h3>
  <p><strong>Technical interview preparation</strong>: </p>
<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>
<p>Write a function in C that checks if a singly linked list is a palindrome.</p>
<ul>
<li>Prototype: <code>int is_palindrome(listint_t **head);</code></li>
<li>Return: <code>0</code> if it is not a palindrome, <code>1</code> if it is a palindrome</li>
<li>An empty list is considered a palindrome</li>
</ul>
        <p>File: <code>13-is_palindrome.c, lists.h</code></p>
  <h3>
    14. CPython #0: Python lists
  </h3>
  <p>CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let&rsquo;s have fun with Python and C, and let&rsquo;s look at what makes Python so easy to use.</p>
Create a C function that prints some basic info about Python lists.</p>
<ul>
<li>Prototype: <code>void print_python_list_info(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Python version: 3.4</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c</code></li>
<li>OS: <code>Ubuntu 14.04 LTS</code></li>
<li>Start by reading:
<ul>
<li>listobject.h</li>
<li>object.h</li>
<li>Common Object Structures</li>
<li>List Objects</li>
</ul></li>
</ul>
        <p>File: <code>100-print_python_list_info.c</code></p>
