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
print("-- open() --")

print("---= Methods =---")

print("--= Reading =--")
print("-- read() --")
print("-- readline() --")
print("-- readlines() --")
print("-- xreadlines() --")
print("-- next() --")

print("--= Writing =--")
print("-- write() --")
print("-- writelines() --")
print("-- flush() --")

print("--= File Position =--")
print("-- tell() --")
print("-- seek() --")

print("--= Other =--")
print("-- close() --")
print("-- fileno() --")
print("-- truncate() --")
print("-- isatty() --")

print("---= Properties =---")
print("-- name() --")
print("-- mode() --")
print("-- encoding() --")
print("-- closed() --")
print("-- errors() --")
print("-- newlines() --")
print("-- softspace() --")
