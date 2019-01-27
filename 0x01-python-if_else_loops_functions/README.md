<h1>0x01. Python - if/else, loops, functions</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>Why indentation is so important in Python</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use the <code>while</code> and <code>for</code> loops</li>
<li>How is Python&rsquo;s <code>for</code> different from <code>C</code>&lsquo;s?</li>
<li>How to use the <code>break</code> and <code>continues</code> statements</li>
<li>How to use <code>else</code> clauses on loops</li>
<li>What does the <code>pass</code> statement do, and when to use it</li>
<li>How to use <code>range</code></li>
<li>What is a function and how do you use functions</li>
<li>What does return a function that does not use any <code>return</code> statement</li>
<li>Scope of variables</li>
<li>What&rsquo;s a traceback</li>
<li>What are the arithmetic operators and how to use them</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Positive anything is better than negative nothing
  </h3>
  <p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.</p>
<ul>
<li>You can find the source code here</li>
<li>The variable <code>number</code> will store a different value every time you will run this program</li>
<li>You don&rsquo;t have to understand what <code>import</code>, <code>random. randint</code> do. Please do not touch this code</li>
<li>The output of the program should be:
<ul>
<li>The number, followed by
<ul>
<li>if the number is greater than 0: <code>is positive</code></li>
<li>if the number is 0: <code>is zero</code></li>
<li>if the number is less than 0: <code>is negative</code></li>
</ul></li>
<li>followed by a new line</li>
</ul></li>
</ul>
        <p>File: <code>0-positive_or_negative.py</code></p>
  <h3>
    1. The last digit
  </h3>
  <p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>.</p>
<ul>
<li>You can find the source code here</li>
<li>The variable <code>number</code> will store a different value every time you will run this program</li>
<li>You don&rsquo;t have to understand what <code>import</code>, <code>random.randint</code> do. <strong>Please do not touch this code</strong>. This line should not change: <code>number = random.randint(-10000, 10000)</code></li>
<li>The output of the program should be:
<ul>
<li>The string <code>Last digit of</code>, followed by</li>
<li>the number, followed by</li>
<li>the string <code>is</code>, followed by
<ul>
<li>if the number is greater than 5: the string <code>and is greater than 5</code></li>
<li>if the number is 0: the string <code>and is 0</code></li>
<li>if the number is less than 6 and not 0: the string <code>and is less than 6 and not 0</code></li>
</ul></li>
<li>followed by a new line</li>
</ul></li>
</ul>
        <p>File: <code>1-last_digit.py</code></p>
  <h3>
    2. I sometimes suffer from insomnia. And when I can&#39;t fall asleep, I play what I call the alphabet game
  </h3>
  <p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>
<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>2-print_alphabet.py</code></p>
  <h3>
    3. When I was having that alphabet soup, I never thought that it would pay off
  </h3>
  <p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>
<ul>
<li>Print all the letters except <code>q</code> and <code>e</code></li>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>3-print_alphabt.py</code></p>
  <h3>
    4. Hexadecimal printing
  </h3>
  <p>Write a program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example)</p>
<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>4-print_hexa.py</code></p>
  <h3>
    5. 00...99
  </h3>
  <p>Write a program that prints numbers from <code>0</code> to <code>99</code>.</p>
<ul>
<li>Numbers must be separated by <code>,</code>, followed by a space</li>
<li>Numbers should be printed in ascending order, with two digits</li>
<li>The last number should be followed by a new line</li>
<li>You can only use no more than 2 <code>print</code> functions with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>5-print_comb2.py</code></p>
  <h3>
    6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
  </h3>
  <p>Write a program that prints all possible different combinations of two digits.</p>
<ul>
<li>Numbers must be separated by <code>,</code>, followed by a space</li>
<li>The two digits must be different</li>
<li><code>01</code> and <code>10</code> are considered the same combination of the two digits <code>0</code> and <code>1</code></li>
<li>Print only the smallest combination of two digits</li>
<li>Numbers should be printed in ascending order, with two digits</li>
<li>The last number should be followed by a new line</li>
<li>You can only use no more than 3 <code>print</code> functions with string format</li>
<li>You can only use no more than 2 loops in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>6-print_comb3.py</code></p>
  <h3>
    7. islower
  </h3>
  <p>Write a function that checks for lowercase character. </p>
<ul>
<li>Prototype: <code>def islower(c):</code></li>
<li>Returns <code>True</code> if <code>c</code> is lowercase</li>
<li>Returns <code>False</code> otherwise</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li>
<li>Tips: ord()</li>
</ul>
<p>You don&rsquo;t need to understand <code>__import__</code></p>
        <p>File: <code>7-islower.py</code></p>
  <h3>
    8. To uppercase
  </h3>
  <p>Write a function that prints a string in uppercase followed by a new line.</p>
<ul>
<li>Prototype: <code>def uppercase(str):</code></li>
<li>You can only use no more than 2 <code>print</code> functions with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li>
<li>Tips: ord()</li>
</ul>
<p>You don&rsquo;t need to understand <code>__import__</code></p>
        <p>File: <code>8-uppercase.py</code></p>
  <h3>
    9. There are only 3 colors, 10 digits, and 7 notes; it&#39;s what we do with them that&#39;s important
  </h3>
  <p>Write a function that prints the last digit of a number.</p>
<ul>
<li>Prototype: <code>def print_last_digit(number):</code></li>
<li>Returns the value of the last digit</li>
<li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand <code>__import__</code></p>
        <p>File: <code>9-print_last_digit.py</code></p>
  <h3>
    10. a + b
  </h3>
  <p>Write a function that adds two integers and returns the result.</p>
<ul>
<li>Prototype: <code>def add(a, b):</code></li>
<li>Returns the value of <code>a + b</code></li>
<li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand <code>__import__</code></p>
        <p>File: <code>10-add.py</code></p>
  <h3>
    11. a ^ b
  </h3>
  <p>Write a function that computes <code>a</code> to the power of <code>b</code> and return the value.</p>
<ul>
<li>Prototype: <code>def pow(a, b):</code></li>
<li>Returns the value of <code>a ^ b</code></li>
<li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand <code>__import__</code></p>
        <p>File: <code>11-pow.py</code></p>
  <h3>
    12. Fizz Buzz
  </h3>
  <p>Write a function that prints the numbers from 1 to 100 separated by a space. </p>
<ul>
<li>For multiples of three print <code>Fizz</code> instead of the number and for multiples of five print <code>Buzz</code>. </li>
<li>For numbers which are multiples of both three and five print <code>FizzBuzz</code>.</li>
<li>Prototype: <code>def fizzbuzz():</code></li>
<li>Each element should be followed by a space</li>
<li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand <code>__import__</code></p>
        <p>File: <code>12-fizzbuzz.py</code></p>
  <h3>
    13. Insert in sorted linked list
  </h3>
  <p><strong>Technical interview preparation</strong>: </p>
<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>
<p>Write a function in C that inserts a number into a sorted singly linked list.</p>
<ul>
<li>Prototype: <code>listint_t *insert_node(listint_t **head, int number);</code></li>
<li>Return: the address of the new node, or <code>NULL</code> if it failed</li>
</ul>
        <p>File: <code>13-insert_number.c, lists.h</code></p>
  <h3>
    14. Smile in the mirror
  </h3>
  <p>Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (<code>z</code> in lowercase and <code>Y</code> in uppercase) , not followed by a new line.</p>
<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>100-print_tebahpla.py</code></p>
  <h3>
    15. Remove at position
  </h3>
  <p>Write a function that creates a copy of the string, removing the character at the position <code>n</code> (not the Python way, the &ldquo;C array index&rdquo;).</p>
<ul>
<li>Prototype: <code>def remove_char_at(str, n):</code></li>
<li>You are not allowed to import any module</li>
</ul>
<p>You don&rsquo;t need to understand <code>__import__</code></p>
        <p>File: <code>101-remove_char_at.py</code></p>
  <h3>
    16. ByteCode -&gt; Python #2
  </h3>
  <p>Write the Python function <code>def magic_calculation(a, b, c):</code> that does exactly the same as the following Python bytecode:</p>
<p>tips - ByteCode</p>
        <p>File: <code>102-magic_calculation.py</code></p>
