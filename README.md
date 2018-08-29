# Sublime "Ref Docs" plugin

Open reference docs for the selected package name. If the cursor is within quoted text the quoted text will be selected.

## Install

Go to the Sublime Text Packages directory and git clone:

`git clone https://github.com/RJK-Engineering/SublimeRefDocs.git RefDocs`

## Key Binding

Basic config: `{ "keys": ["f1"], "command": "ref_docs" }`

For Windows, `Default (Windows).sublime-keymap` is provided, create your own for other OS's.

## Options

If the browser doesn't open or if you want a different browser, use the "browser" argument:
`{ "keys": ["f1"], "command": "ref_docs", "args": { "browser": "c:/dev/chrome/GoogleChromePortable.exe" } }`

## To Do

* browser.open_new_tab option
* configurable package name -> url mapping
    * configurable package name string conversion ("/" => ".")

## See Also

https://github.com/int3h/SublimeSelectQuoted
