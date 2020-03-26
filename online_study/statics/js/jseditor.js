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



function alertFunction (){
	alert('Hi! Buddy this is alert box ');
}

