<h1>File Integrity Monitor</h1>
<p>A Python project that monitors the integrity of files.</p>

- This program monitors files within a directory, checking for any creation, deletion or modification of files.<br>
- This is achieved by the following:

<ol>
<li>Creating a baseline file, which calculates the hash of the files present in the directory & storing them into a file called <code>Baseline.txt.</code></li>
<li>Monitoring the directory by calculating and comparing the hash of the files present in that directory, to the hashes stored in <code>`Baseline.txt`.</code></li>
<li>Upon creation, deletion or modification of a file, a message is printed out listing the name of the file that has been created, deleted or modified.</li>
</ol>

I'm quite content with how this project turned out & helped me get back up to scratch with Python, as well as catering towards the Cyber Security aspect of software development.<br>

Whilst I was finishing off this project I was thinking about potential features that could be implemented in the future, these aren't required for the base program to work, however they would contribute towards the quality of life, modularity or futureproofing of the FIM: <br>

- Introducing modularity in the form of different hashing functions, so being able to switch from SHA512 to SHA256 or to MD5, of course each hashing function will have it's own security advantages & disadvantages.<br>
- QoL changes could include displaying the initial options again <b>after</b> creating the baseline, gracefully exiting the program, changing the colour of the text to highlight the file names or create an order of priority with colours and which action took place (e.g. File deleted = red).<br>
- Futureproofing can be achieved by simply keeping up with Cybersec news and developments, if a new hashing function is created, then ensure the project is updated to reflect support of the new function or implement a dynamic method which automatically adds support for new hashing functions.<br>
