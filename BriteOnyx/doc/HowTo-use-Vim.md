HowTo use Vim

TODO: Need to switch to Spacemacs again...

### File browsing
`:Explore`
`:help netrw-browse-maps`

`-` = go up one directory
`D` = delete current file
`I` = toggle banner
`P` = browse current file in previously-used window
`c-l` = refresh listing
`c-tab` = expand/shrink window
`cd` = change to current directory
`cr` = open current directory or file
`d` = create a directory
`gn` = make current directory the top of tree
`i` = cycle through view types
`mF` = unmark file
`md` = apply diff marked files (up to 3)
`me` = add marked files to arg list
`mf` = mark current file
`mg` = apply vimgrep to marked files
`mu` = unmark all files
`o` = open current directory/file in new window

### File lists
Learn when to use which file lists

* argument list
* quickfix list
* buffer list

### Help
`c-]` = jump to current link
`c-t` = jump back

### Line numbering
ru = relative line numbering
nu = line numbering

### Search
Disable search highlighting = :noh

### Split
`c-w h` = switch split pane

### Substitute
TODO: How do I select text, then use it in a substitute as OLD or NEW?
Substitute :%s/FIND/REPLACE/g
Substitute in all buffers :bufdo %s/FIND/REPLACE/ge | update

