# Sublime "Ref Docs" plugin

Open reference documentation in a browser for the selected name, e.g. a package or a class name. If there is no selection and the cursor is within quoted text the quoted text will be selected.

Home page: https://github.com/RJK-Engineering/SublimeRefDocs

## Install

Go to the Sublime Text Packages directory and git clone:

`git clone https://github.com/RJK-Engineering/SublimeRefDocs.git RefDocs`

To enable automatic selection, install package "Select Quoted" (https://github.com/int3h/SublimeSelectQuoted).

## Key Binding

Basic config:

`{ "keys": ["f1"], "command": "ref_docs" }`

For Windows, [`Default (Windows).sublime-keymap`](Default%20(Windows).sublime-keymap) is provided, create your own for other OS's.

## Options

If the browser doesn't open or if you want a different browser, use the "browser" argument:

`{ "keys": ["f1"], "command": "ref_docs", "args": { "browser": "c:/dev/chrome/GoogleChromePortable.exe" } }`

## Settings

Name to url mapping is configured in [`RefDocs.sublime-settings`](RefDocs.sublime-settings).

## See Also

* https://packagecontrol.io
* https://github.com/int3h/SublimeSelectQuoted
