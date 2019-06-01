# Rrl-Viewer

Sublime Plugin to show RTL text on Popup.

Author: Nady Shalaby

Credit to: [CoreCave Ltd](https://www.corecave.com)

A Sublime Editor plugin that can display RTL (<b>R</b>ight <b>T</b>o <b>L</b>eft) content correctly.

Notice: to fix rtl problems from Sublime version 3.1 (3170) you need to change <i>"font_options": ["gdi"]</i>

## Features

<ul>
  <li>Should work great with Arabic, Hebrew, Syriac, Samaritan, Mandaic, Thaana, Mende Kikakui, N'Ko & Adlam.</li>
  <li>Settings file gives you control over window size, words per line and the devidor between several selections.</li>
  <li>Works with version 3080 and up.</li>
  <li>just need to adjust the key binding. (Currently, the plugin works with <code>Ctrl + F1</code> on Windows or OSX. If you want to change it, go to Preferences>>key bindings-user. and setup your custom key binding<code>	{"keys": ["shift+f1"], "command": "rtl_viewer" }</code>)</li>
</ul>

<img src="http://i.imgur.com/88c99aP.png" alt="rtl viewer">

## Setup

In the sublime Package Control (<code>Ctrl + P</code> and then type "install package"), search for 'Rtl Viewer'.

