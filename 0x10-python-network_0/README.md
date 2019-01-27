<h1>0x10. Python - Network #0</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What a URL is</li>
<li>What HTTP is</li>
<li>How to read a URL</li>
<li>The scheme for a HTTP URL</li>
<li>What a domain name is</li>
<li>What a sub-domain is</li>
<li>How to define a port number in a URL</li>
<li>What a query string is</li>
<li>What an HTTP request is</li>
<li>What an HTTP response is</li>
<li>What HTTP headers are</li>
<li>What the HTTP message body is</li>
<li>What an HTTP request method is</li>
<li>What an HTTP response status code is</li>
<li>What an HTTP Cookie is</li>
<li>How to make a request with cURL</li>
<li>What happens when you type google.com in your browser (Application level)</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. cURL body size
  </h3>
  <p>Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response</p>
<ul>
<li>The size must be displayed in bytes</li>
<li>You have to use <code>curl</code></li>
</ul>
<p>Please test your script in the container provided, using the web server running on port 5000</p>
        <p>File: <code>0-body_size.sh</code></p>
  <h3>
    1. cURL to the end
  </h3>
  <p>Write a Bash script that takes in a URL, sends a <code>GET</code> request to the URL, and displays the body of the response</p>
<ul>
<li>Display only body of a <code>200</code> status code response</li>
<li>You have to use <code>curl</code></li>
</ul>
<p>Please test your script in the container provided, using the web server running on port 5000</p>
        <p>File: <code>1-body.sh</code></p>
  <h3>
    2. cURL Method
  </h3>
  <p>Write a Bash script that sends a <code>DELETE</code> request to the URL passed as the first argument and displays the body of the response</p>
<ul>
<li>You have to use <code>curl</code></li>
</ul>
<p>Please test your script in the container provided, using the web server running on port 5000</p>
        <p>File: <code>2-delete.sh</code></p>
  <h3>
    3. cURL only methods
  </h3>
  <p>Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.</p>
<ul>
<li>You have to use <code>curl</code></li>
</ul>
<p>Please test your script in the container provided, using the web server running on port 5000</p>
        <p>File: <code>3-methods.sh</code></p>
  <h3>
    4. cURL headers
  </h3>
  <p>Write a Bash script that takes in a URL as an argument, sends a <code>GET</code> request to the URL, and displays the body of the response</p>
<ul>
<li>A header variable <code>X-HolbertonSchool-User-Id</code> must be sent with the value <code>98</code></li>
<li>You have to use <code>curl</code></li>
</ul>
<p>Please test your script in the container provided, using the web server running on port 5000</p>
        <p>File: <code>4-header.sh</code></p>
  <h3>
    5. cURL POST parameters
  </h3>
  <p>Write a Bash script that takes in a URL, sends a <code>POST</code> request to the passed URL, and displays the body of the response</p>
<ul>
<li>A variable <code>email</code> must be sent with the value <code>hr@holbertonschool.com</code></li>
<li>A variable <code>subject</code> must be sent with the value <code>I will always be here for PLD</code></li>
<li>You have to use <code>curl</code></li>
</ul>
<p>Please test your script in the container provided, using the web server running on port 5000</p>
        <p>File: <code>5-post_params.sh</code></p>
  <h3>
    6. Find a peak
  </h3>
  <p><strong>Technical interview preparation</strong>: </p>
<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>
<p>Write a function that finds a peak in a list of unsorted integers.</p>
<ul>
<li>Prototype: <code>def find_peak(list_of_integers):</code></li>
<li>You are not allowed to import any module</li>
<li>Your algorithm must have the lowest complexity </li>
<li><code>6-peak.py</code> must contain the function</li>
<li><code>6-peak.txt</code> must contain the complexity of your algorithm: <code>O(log(n))</code>, <code>O(n)</code>, <code>O(nlog(n))</code> or <code>O(n2)</code></li>
</ul>
        <p>File: <code>6-peak.py, 6-peak.txt</code></p>
