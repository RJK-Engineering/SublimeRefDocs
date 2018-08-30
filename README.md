# Sublime "Ref Docs" plugin

Open reference docs in a browser for the selected package name. If there is no selection and the cursor is within quoted text the quoted text will be selected.

## Install

Use Package Control to install package "Select Quoted".

Go to the Sublime Text Packages directory and git clone:

`git clone https://github.com/RJK-Engineering/SublimeRefDocs.git RefDocs`

## Key Binding

Basic config:

`{ "keys": ["f1"], "command": "ref_docs" }`

For Windows, `Default (Windows).sublime-keymap` is provided, create your own for other OS's.

## Options

If the browser doesn't open or if you want a different browser, use the "browser" argument:

`{ "keys": ["f1"], "command": "ref_docs", "args": { "browser": "c:/dev/chrome/GoogleChromePortable.exe" } }`

## To Do

* browser.open_new_tab option
* configurable package name -> url mapping
    * configurable package name string conversion ("/" => ".")

## See Also

* https://packagecontrol.io
* https://github.com/int3h/SublimeSelectQuoted
