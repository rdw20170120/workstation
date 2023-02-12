# My source-generation library

* Based on Tavis Rudd's throw\_out\_your\_templates code
* Write "templates" in a real programming language (Python)
* Avoids problematic templating "languages"
* Generates files (source code) in various languages
  * Bash
  * Markdown
  * Python

## Testing
Based on my overall testing approach,
I must factor my functionality
into separate source files
like this:

* functionality worth testing right away
  * "material" = functions using "elements" to generate code portions
* functionality tested best by the code-generation output
  * classes for rendering
  * "framing" = functions that merely compose "materials"
  * functions for rendering to a file
* functionality unlikely to be worth testing directly
  * underlying template functionality
  * "element" = classes representing code-generation items

