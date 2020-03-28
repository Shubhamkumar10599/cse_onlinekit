var editor1 = ace.edit("editor1");
    editor1.setTheme("ace/theme/eclipse");
    editor1.session.setMode("ace/mode/javascript");
    editor1.setReadOnly(true);
    editor1.setHighlightActiveLine(false);
    editor1.setShowPrintMargin(false);
    editor1.session.setUseWrapMode(true);
    editor1.renderer.$cursorLayer.element.style.display = "none"
    editor1.renderer.setShowGutter(false);
    document.getElementById('editor1').style.fontSize='17px'