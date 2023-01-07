#!/bin/tclsh
# call with
# - cmd=check_version&version=<version>
# - cmd=download&version=<version>

set newversion "1.0.0"
puts -nonewline "Content-Type: text/plain; charset=utf-8\r\n\r\n"
puts $newversion
