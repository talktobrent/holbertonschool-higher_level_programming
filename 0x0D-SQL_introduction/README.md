<h1>0x0D. SQL - Introduction</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What&rsquo;s a database</li>
<li>What&rsquo;s a relational database</li>
<li>What does SQL stand for</li>
<li>What&rsquo;s MySQL</li>
<li>How to create a database in MySQL</li>
<li>What does <code>DDL</code> and <code>DML</code> stand for</li>
<li>How to <code>CREATE</code> or <code>ALTER</code> a table</li>
<li>How to <code>SELECT</code> data from a table</li>
<li>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</li>
<li>What are <code>subqueries</code></li>
<li>How to use MySQL functions</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. List databases
  </h3>
  <p>Write a script that lists all databases of your MySQL server.</p>
        <p>File: <code>0-list_databases.sql</code></p>
  <h3>
    1. Create a database
  </h3>
  <p>Write a script that creates the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>If the database <code>hbtn_0c_0</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>
        <p>File: <code>1-create_database_if_missing.sql</code></p>
  <h3>
    2. Delete a database
  </h3>
  <p>Write a script that deletes the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>If the database <code>hbtn_0c_0</code> doesn&rsquo;t exist, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>
        <p>File: <code>2-remove_database.sql</code></p>
  <h3>
    3. List tables
  </h3>
  <p>Write a script that lists all the tables of a database in your MySQL server.</p>
<ul>
<li>The database name will be passed as argument of <code>mysql</code> command (in the following example: <code>mysql</code> is the name of the database)</li>
</ul>
        <p>File: <code>3-list_tables.sql</code></p>
  <h3>
    4. First table
  </h3>
  <p>Write a script that creates a table called <code>first_table</code> in the current database in your MySQL server.</p>
<ul>
<li><code>first_table</code> description:
<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>first_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>
        <p>File: <code>4-first_table.sql</code></p>
  <h3>
    5. Full description
  </h3>
  <p>Write a script that prints the full description of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>You are not allowed to use the <code>DESCRIBE</code> or <code>EXPLAIN</code> statements</li>
</ul>
        <p>File: <code>5-full_table.sql</code></p>
  <h3>
    6. List all in table
  </h3>
  <p>Write a script that lists all rows of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>All fields should be printed</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>6-list_values.sql</code></p>
  <h3>
    7. First add
  </h3>
  <p>Write a script that inserts a new row in the table <code>first_table</code> (database <code>hbtn_0c_0</code>) in your MySQL server.</p>
<ul>
<li>New row:
<ul>
<li><code>id</code> = <code>89</code></li>
<li><code>name</code> = <code>Holberton School</code></li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>7-insert_value.sql</code></p>
  <h3>
    8. Count 89
  </h3>
  <p>Write a script that displays the number of records with <code>id = 89</code> in the table <code>first_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>8-count_89.sql</code></p>
  <h3>
    9. Full creation
  </h3>
  <p>Write a script that creates a table <code>second_table</code> in the database <code>hbtn_0c_0</code> in your MySQL server and add multiples rows.</p>
<ul>
<li><code>second_table</code> description:
<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
<li><code>score</code> INT</li>
</ul></li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
<li>If the table <code>second_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> and <code>SHOW</code> statements</li>
<li>Your script should create these records:
<ul>
<li><code>id</code> = 1, <code>name</code> = &ldquo;John&rdquo;, <code>score</code> = 10</li>
<li><code>id</code> = 2, <code>name</code> = &ldquo;Alex&rdquo;, <code>score</code> = 3</li>
<li><code>id</code> = 3, <code>name</code> = &ldquo;Bob&rdquo;, <code>score</code> = 14</li>
<li><code>id</code> = 4, <code>name</code> = &ldquo;George&rdquo;, <code>score</code> = 8</li>
</ul></li>
</ul>
        <p>File: <code>9-full_creation.sql</code></p>
  <h3>
    10. List by best
  </h3>
  <p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first) </li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>10-top_score.sql</code></p>
  <h3>
    11. Select the best
  </h3>
  <p>Write a script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first)</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>11-best_score.sql</code></p>
  <h3>
    12. Cheating is bad
  </h3>
  <p>Write a script that updates the score of Bob to <code>10</code> in the table <code>second_table</code>.</p>
<ul>
<li>You are not allowed to use Bob&rsquo;s id value, only the <code>name</code> field</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>12-no_cheating.sql</code></p>
  <h3>
    13. Score too low
  </h3>
  <p>Write a script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>13-change_class.sql</code></p>
  <h3>
    14. Average
  </h3>
  <p>Write a script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>The result column name should be <code>average</code></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
        <p>File: <code>14-average.sql</code></p>
  <h3>
    15. Number by score
  </h3>
  <p>Write a script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>The result should display:
<ul>
<li>the <code>score</code></li>
<li>the number of records for this <code>score</code> with the label <code>number</code></li>
</ul></li>
<li>The list should be sorted by the number of records (descending)</li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul>
        <p>File: <code>15-groups.sql</code></p>
  <h3>
    16. Say my name
  </h3>
  <p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<ul>
<li>Don&rsquo;t list rows without a <code>name</code> value</li>
<li>Results should display the score and the name (in this order)</li>
<li>Records should be listed by descending score </li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul>
<p>In this example, new data have been added to the table <code>second_table</code>.</p>
        <p>File: <code>16-no_link.sql</code></p>
