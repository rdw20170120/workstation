# My source-generation library

* Based on Tavis Rudd's throw\_out\_your\_templates Python code
* Write "templates" in a real programming language (Python)
* Avoids problematic templating "languages"
* Generates files (source) in various languages
  * Bash
  * Markdown
  * Python

## Testing
Based on my overall testing approach,
I must factor my functionality
into separate source files
like this:
* functionality worth testing right away
  * "material" = functions using "elements" to generate source portions
* functionality tested best by the source-generation output
  * classes for rendering
  * "frame" = functions that merely compose "materials" and "frames"
  * "complete" frames = functions that merely compose "materials" and "frames" into a complete file
  * functions for rendering to a file
* functionality unlikely to be worth testing directly
  * underlying template functionality
  * "element" = classes representing source-generation items

Therefore,
I will divide up
the source-generation functionality
along these lines:
* separate module for each kind of source file to be generated
* module heirarchy that matches the relationships between kinds of source files
* separate modules for Bash scripts invoked before, during, and after BriteOnyx activation
  * "bash" = stand-alone scripts that do not use BriteOnyx functionality
  * "activating" = scripts invoked during the activation of BriteOnyx
  * "briteonyx" = scripts that depend upon BriteOnyx functionality being activated in the current project
* for each module:
  * "element.py" = classes representing low-level source-generation items
  * "material.py" = functions that generate testable source portions
  * "frame.py" = functions that merely compose "materials" and other "frames" (`return [...]`)
  * "render.py" = class & function for rendering a particular kind of file
  * "complete.py" = functions for rendering complete source files, sometimes with variants as appropriate
  * "test\_material.py" = test suite for "material.py"

