//cobalt,xcode,monokai,chrome,dawn,eclipse,gob,textmate,cloud,katzenmilch,kuroir
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/eclipse");
    editor.session.setMode("ace/mode/javascript");
    editor.setReadOnly(true);
    editor.setHighlightActiveLine(false);
    editor.setShowPrintMargin(false);
    editor.session.setUseWrapMode(true);
    editor.renderer.$cursorLayer.element.style.display = "none"
    editor.renderer.setShowGutter(false);
    document.getElementById('editor').style.fontSize='17px';