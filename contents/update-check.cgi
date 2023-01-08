#!/bin/tclsh
# call with
# - cmd=check_version&version=<version>
# - cmd=download&version=<version>

set checkVersionUrl "https://raw.githubusercontent.com/sg70/hm-homebridge-addon/main/contents/VERSION"
set downloadReleaseUrl "https://github.com/sg70/hm-homebridge-addon/releases/latest"

catch {
  set input $env(QUERY_STRING)
  set pairs [split $input &]
  foreach pair $pairs {
    if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
      set $varname $val
    }
  }
}

if { [info exists cmd ] && $cmd == "download"} {
    puts -nonewline "Content-Type: text/html; charset=utf-8\r\n\r\n"
    puts -nonewline "<!DOCTYPE html><html><head><meta http-equiv='refresh' content='0; url=$downloadReleaseUrl' /></head><body></body></html>"
} else {
    puts -nonewline "Content-Type: text/plain; charset=utf-8\r\n\r\n"
    catch {
        set newVersion [ exec /usr/bin/wget -qO- --no-check-certificate $checkVersionUrl ]
    }
    if { [info exists newVersion] } {
        puts $newVersion
    } else {
        puts "n/a"
    }
}
