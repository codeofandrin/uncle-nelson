# Credits: discord.py (https://github.com/Rapptz/discord.py)

from docutils.parsers.rst import Directive
from docutils import nodes


class exception_hierarchy(nodes.General, nodes.Element):
    pass


def visit_exception_hierarchy_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='exception-hierarchy-content'))


def depart_exception_hierarchy_node(self, node):
    self.body.append('</div>\n')


class ExceptionHierarchyDirective(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()
        node = exception_hierarchy('\n'.join(self.content))
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app):
    app.add_node(exception_hierarchy, html=(visit_exception_hierarchy_node, depart_exception_hierarchy_node))
    app.add_directive('exception_hierarchy', ExceptionHierarchyDirective)
    return {'parallel_read_safe': True}
