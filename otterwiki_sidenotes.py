import re

from otterwiki.plugins import hookimpl, plugin_manager

class SideNotes:
    @hookimpl
    def renderer_markdown_preprocess(self, md: str) -> str:
        return re.sub('{{note ([^}]*)}}', '<label class="sidenote-number"></label><span class="alert-sidenote">\\1</span>', md, flags=re.IGNORECASE)

    @hookimpl
    def static_css(self) -> str:
        return '''
@import url('https://fonts.googleapis.com/css2?family=Baskervville');

body {
    counter-reset: sidenote-counter;
}

.content > .page {
    font-family: 'Baskervville', serif;
    font-weight: 400;
}

.alert-sidenote:before {
    content: counter(sidenote-counter) " ";
    font-size: 1rem;
    top: -0.5rem;
}

.sidenote-number {
    counter-increment: sidenote-counter;
}
.sidenote-number:after {
    content: counter(sidenote-counter);
    font-size: 1rem;
    top: -0.5rem;
    left: 0.1rem;
}

.alert-sidenote {
    float: right;
    clear: right;
    margin-right: -60%;
    width: 50%;
    margin-top: 0.3rem;
    margin-bottom: 0;
    font-size: 1.1rem;
    line-height: 1.3;
    vertical-align: baseline;
    position: relative;
}
'''

plugin_manager.register(SideNotes())
