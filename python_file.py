# File objects are implemented using C's <stdio.h> package and can be created with the built-in file() and open() func.
# File objects are also returned by some other built-in functions and methods.
# -- Such as os.popen() and os.fdopen() and the makefile() method of socket objects.
# Temporary files can be created using the tempfile module, and high-level file operations such as
# -- copying, moving, and deleting files and dictionaries can be achieved with the shutli module.

# When a file operation fails for an I/O related reason, the exception IOError is raised.
# -- This includes situations where the operation is not defined for some reason, like seek() on a
# tty device or writing a file opened for reading.

# Files are viewed as a sequential stream of bytes. A file is terminated with an end of file marker (EOF).
# -- When a file is opened a file object is associated with it.

# By default, there are three initialized when the script execution starts
# -- sys.stdin -- sys.stdout -- sys.stderr
# They correspond to the interpreter's standard input, output, and error streams.

print("---= Constructors =---")

print("-- file() --")
# Description: Returns a file object.
# Syntax: file(name[,model[,buffering]])
# -- name: Optional. Full filepath.

# -- mode: Optional. Possible values:
# r: opening for reading (default)
# w: open for writing, truncating the file first
# a: open for writing, appending to the end of the file if it exists
# b: binary mode
# t: text mode (default)
# +: open a disk file for updating (reading and writing)
# U: universal newlines mode (for backwards compatibility; should not be used in new code)

# -- buffering: Optional. Possible Values:
# 0: to switch buffering off (only allowed in binary mode)
# 1: to select line buffering (only usable in text mode)
# int > 1: to indicate the size of a fixed-size chunk buffer.

# Time Complexity:
# Remarks: When opening a file, it's preferable to use open() instead of invoking this constructor directly.
# -- File is more suited to type testing (for example, writing isinstance(f, file)).

# Example:
alice = open(r'alice_in_woderland.txt', 'r+')
print(alice.readline())
print("*************************")

print("-- open() --")
# Description: Opens a file returning a file object.
# Syntax: open(name[,mode[,buffering]])
# -- name: Optional. Full filepath.
# *************************
# -- mode: Optional. Possible Values:
# r: open for reading (default)
# w: open for writing, truncating the file first
# a: open for writing, appending to the end of the file if it exists
# b: binary mode
# t: text mode (default)
# +: open a disk file for updating (reading and writing)
# U: universal newlines mode (for backwards compatibility, should not be used in new code)

# The most commonly-used values of mode are
# r: reading. If mode is omitted. Default
# w: writing (truncating the file if it already exists)
# a: (Unix systems all writes append to the end of the file regardless of the seek position)

# The default is to use text mode, which may convert 'n' characters to a platform-specific representation
# -- on writing and back on reading.
# Thus, when opening a binary file, you should append 'b' to the mode value to open the file in binary mode,
# -- which will improve portability.
# Appending 'b' is useful even on systems that don't treat binary and text files differently.

# Modes 'r+', 'w+', and 'a+' open the file for updating (note that 'w+' truncates the file).
# Append 'b' to the mode to open the file in binary mode, on systems that differentiate between binary and text files;
# -- on systems that don't have this distinction, adding the 'b' has no effect.
# *************************
# -- buffering: Optional. Possible values:
# 0: to switch buffering off (only allowed in binary mode)
# 1: to select line buffering (only usable in text mode)
# int > 1: to indicate the size of a fixed-size chunk buffer

# The optional buffering argument specifies the file's desired buffer size:
# 0: Unbuffered
# 1: Buffered
# int > 1: Buffered, any other positive value means use a buffer of (approximately) that size (in bytes).
# A negative buffering means to use the system default, which is usually line buffered for tty devices and
# -- full buffered for other files. If omitted, the system default is used.
# *************************

# Time Complexity:

# Remarks: In addition to the standard fopen() values mode may be 'U' or 'rU'.
# Python is usually built with universal newlines support;
# 'U': opens the file as a text file, but lines may be terminated by any of the following:
# -- Unix end-of-line convention: 'n'
# -- Macintosh convention: 'r'
# -- Windows convention: 'rn'
# All of these external representations are seen as 'n' by the Python program.
# If Python is built without universal newlines support a mode with 'U' is the same as normal text mode.
# Note that file objects so opened also have an attribute called newlines which has a value of None.
# -- (If no newlines have yet been seen), -- 'n' -- 'r' -- 'rn', or a tuble containing all the newline types seen.
# Python enforces that the mode, after stripping 'U', begins with 'r', 'w', or 'a'.
# Python provides many file handling modules including
# -- fileinput --  os -- os.path -- tempfile -- shutil

# Example:
print(open('alice_in_woderland.txt'))

alice = open(r'alice_in_woderland.txt', 'r+')
print(alice.readline())
print("*************************")

print("---= Methods =---")
print("*************************")
print("--= Reading =--")


print("-- read() --")
# Description: Returns specified amount of bytes from the file.
# Syntax: file.read([size])
# -- size: Optional. Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes)>
# If the size argument is negative or omitted, reads all data until EOF is reached.

# Remarks: The bytes are returned as a string object.
# -- An empty string is returned when EOF is encountered immediately.
# (For certain files, like ttys, it makes sense to continue reading after an EOF is hit).

# Notes: This method may call the underlying C function fread() more than once in an effort
# -- to acquire as close to size bytes as possible.
# Also note that when in non-blocking mode, less data than was requested maybe returned, if no size parameter was given.
# This function is simply a wrapper for the underlying fread() C function, and will behave the same in corner cases,
# -- such as whether the EOF value is cached.

# Return Value: None.

# Example:
alice.read()

print("*************************")

print("-- readline() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# -- size: Optional. If the size argument is present and non-negative, it is a maximum byte count
# (including the trailing newline) and an incomplete line may be returned.
# When size is not 0, an empty string is returned only when EOF is encountered immediately.
# Return Value: str
# Remarks: A trailing newline character is kept in the string (but my be absent when a file ends w/ an incomplete line).
# Note: Unlike stdio's fgets() in C, the returned string contains null characters('0') if occurred in input.

# Example:
f = open(r'alice_in_woderland.txt')
print(f.readline(10))
print("*************************")

print("-- readlines() --")
# Description: Returns a list containing lines from the file.
# Syntax: file.readlines([sizehint])
# -- sizehint: Optional. If the sizehint argument is present, instead of reading up to EOF,
# whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.
# Return Value: list
# Remarks: Reads lines until EOF using readline() and returns a list containing the lines thus read.
# -- Objects implementing a file-like iterface may choose to ignore sizehint if it cannot be implemented or
# cannot be implemented efficiently

# Example:
f = open(r'alice_in_woderland.txt')
l = f.readlines()
print(l)
print("*************************")

print("-- xreadlines() --")
# Description: Returns an iterator over the lines of the file.
# Syntax: file.xreadlines()
# Return Value: file
# Remarks: This method returns the same thing as iter(file).
# Usage of this function is deprecated. File objects are iterators by default now.

# Example:
print("*************************")

print("-- next() --")
# Description: Returns a next line from the file.
# Syntax: file.next()
# Remarks: A file object is its own iterator, for example iter(f) returns f(unless f is closed)
# When a file is used as an iterator, typically in a for loop

# Example:
print("*************************")

print("--= Writing =--")
print("*************************")

print("-- write() --")
# Description: Writes a string to the file.
# Syntax: file.writes(str)
# -- str: A string you want to write to the file.
# Return Value: None.
# Remarks: There is no return value. Due to buffering, the string may not actually show up in the file
# -- until the flush() or close() method is called.

# Example:
f = open(r'alice_in_woderland.txt', 'a')
f.write('foo')
f.close()

f = open(r'alice_in_woderland.txt')
print(f.read())
print("*************************")

print("-- writelines() --")
# Description: Writes a sequence of strings to the file.
# Syntax: file.writelines(iterable)
# -- iterable: Any iterable object producing strings, typically a list of strings.
# Return Value: None.
# Remarks: There is no return value. The name is intended to match readlines(); writelines()
# -- Does not add line separators.
# Each iteration returns the same result as readline(), and iteration ends when the readline() method
# -- returns an empty string.
# File objects also offer a number of other interesting attributes. These are not required for file-like objects,
# -- but should be implemented if they make sense for the particular object.

# Example:
f = open(r'test.txt', 'w')
l = ['foo', 'bar']
f.writelines(l)
f.close()

f = open(r'test.txt')
print(f.read())
print("*************************")

print("-- flush() --")
# Description: Flushes the write buffers of the file.
# Syntax: file.flush()
# Return Value: None.
# Remarks: It works like stdio's fflush(). This maybe a no-op on some file-like objects.
# flush() does not necessarily write the file's data to disk.

# Example:
fw = open(r'test.txt', 'w')
fw.write('foobar')

fr = open(r'test.txt')
print(fr.readlines()) # wrote a line to fr file, will not write until close() method is called.

fw.flush() # flusing forces the buffer content into the file without closing it
print(fr.readlines())

fw.close()
print("*************************")

print("--= File Position =--")
print("*************************")

print("-- tell() --")
# Description: Returns the file's current position.
# Syntax: file.tell()
# Return Value: long
# Remarks: On Windows, tell() can return illegal values. Use binary ('rb') to circumvent this problem.

# Example:
f = open(r'test.txt')
print(f.tell())

f.seek(3)
print(f.tell())
print("*************************")

print("-- seek() --")
# Description: Sets the file's current position.
# Syntax: file.seek(offset[,whence])
# -- offset: Required. The offset from the beginning of the file.
# -- whence: Optional.
# Return Value: None.
# Remarks:

# Example:
print("*************************")

print("--= Other =--")
print("*************************")

print("-- close() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- fileno() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- truncate() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- isatty() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("---= Properties =---")
print("*************************")

print("-- name() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- mode() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- encoding() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- closed() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- errors() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- newlines() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")

print("-- softspace() --")
# Description: Reads one entire line from the file.
# Syntax: file.readline([size])
# Return Value: str
# Remarks:

# Example:
print("*************************")
