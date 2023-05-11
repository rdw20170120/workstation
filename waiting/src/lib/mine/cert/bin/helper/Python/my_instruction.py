import throw_out_your_templates

from my_couchbase import SERVICE_DATA_ID
from my_couchbase import SERVICE_INDEX_ID
from my_couchbase import SERVICE_QUERY_ID
from my_couchbase import SERVICE_SEARCH_ID
from my_couchbase import service_name


htmltags = throw_out_your_templates._GetAttrDict(throw_out_your_templates.htmltags)
visitor_map = throw_out_your_templates.xml_default_visitors_map.copy()

PAGE_DOC_4_6 = (
    "https://developer.couchbase.com/documentation/server/4.6/introduction/intro.html"
)
PAGE_EXAMPLE_COM = "http://example.com"

PAGE_Bash = "support/HowTo-Bash.html"
PAGE_CUT_AND_PASTE = "support/HowTo-cut_and_paste.html"
PAGE_FOCUS = "support/HowTo-manage_keyboard_focus.html"
PAGE_MACHINE = "support/machine_naming.html"
PAGE_OVERVIEW = "index.html"
PAGE_SESSION = "support/HowTo-exam_session.html"
PAGE_SSH = "support/HowTo-SSH.html"
PAGE_SUDO = "support/HowTo-sudo.html"
PAGE_UI = "support/HowTo-UI.html"
PAGE_UNDO = "support/Why-do_then_undo.html"


def _get_default_encoding():
    return throw_out_your_templates.get_default_encoding()


def _get_serializer():
    return throw_out_your_templates.Serializer(visitor_map, _get_default_encoding())


def _meta():
    return htmltags.meta(charset=_get_default_encoding())


@visitor_map.register(throw_out_your_templates.HTML5Doc)
def _visit_html5_doc(doc, walker):
    walker.walk(
        [
            throw_out_your_templates.safe_unicode("<!DOCTYPE html>"),
            throw_out_your_templates.html(lang="en")[doc.head, doc.body],
        ]
    )


def emphasis(content):
    return htmltags.span("emphasis")[content]


def link(css_class, target, content):
    if not target.startswith("http"):
        target = "./{0}".format(target)
    return htmltags.a(css_class, href=target)[content]


def literal(content):
    return htmltags.span("literal")[content]


def literal_list(content):
    list = sorted(content.split(","))
    return literal(", ".join(list))
    # TODO: RESEARCH: How do I make this work?
    # list = [literal(item) for item in list]
    # return ', '.join(list)
    # ISSUE: literal() returns an XML Element, which is not a string for joining


def service_list(content):
    """Return a string containing a comma-separated list of service names translated from the
    incoming string containing a comma-separated list of service identifiers.
    """
    list = content.split(",")
    list = sorted([service_name(s) for s in list])
    return ", ".join(list)


####################################################################################################


def configure_storage_directories(task, step, servers, directory_data, directory_index):
    task.add_step_header(step, "Configure storage directories")
    task.add(
        htmltags.p[
            "Configure the ",
            emphasis("data"),
            " storage directory to ",
            literal(directory_data),
            " on ",
            literal_list(servers),
            ".",
        ]
    )
    task.add(
        htmltags.p[
            "Configure the ",
            emphasis("index"),
            " storage directory to ",
            literal(directory_index),
            " on ",
            literal_list(servers),
            ".",
        ]
    )


def set_ram_quotas(task, step, servers, data_ram, index_ram):
    task.add_step_header(step, "Set RAM quotas")
    if int(data_ram) != 0:
        task.add(
            htmltags.p[
                "Set the per-node memory quota to ",
                literal(data_ram),
                " ",
                emphasis("MB RAM"),
                " for the ",
                emphasis(service_list(SERVICE_DATA_ID)),
                " on ",
                literal_list(servers),
                ".",
            ]
        )
    if int(index_ram) != 0:
        task.add(
            htmltags.p[
                "Set the per-node memory quota to ",
                literal(index_ram),
                " ",
                emphasis("MB RAM"),
                " for the ",
                emphasis(service_list(SERVICE_INDEX_ID)),
                " on ",
                literal_list(servers),
                ".",
            ]
        )


def setup_services(task, step, servers, services):
    task.add_step_header(step, "Setup services")
    task.add(
        htmltags.p[
            "Setup the ",
            emphasis(service_list(services)),
            " on ",
            literal_list(servers),
            ".",
        ]
    )
    task.add(
        htmltags.p[
            "Do ",
            emphasis("NOT"),
            " setup the ",
            emphasis(service_list(SERVICE_SEARCH_ID)),
            " on this node.",
        ]
    )


def use_any_means(task, servers, port_web_ui):
    task.add(
        htmltags.p[
            "You can use the client's web browser to access the Couchbase Server web GUI at port ",
            literal(port_web_ui),
            " on each of ",
            literal_list(servers),
            ".  You may also choose to use CLI tools or web services, or any combination.",
        ]
    )


####################################################################################################


def discuss_long_running(task):
    task.add(
        htmltags.p[
            emphasis("NOTE:"),
            """  This task involves one or more long-running processes.  You can certainly wait for such
processes to run, but that will use some of your limited examination time.  Instead, you may want to
continue with other exam tasks while such processes are running.  You may also want to attempt
running such processes in parallel, if that is suitable for the task at hand.""",
        ]
    )


def discuss_md5(task):
    task.add(
        htmltags.p[
            emphasis("NOTE:"),
            "  You may notice that there are one or more ",
            emphasis("*.md5"),
            """ files present.  Such files contain formatted text including a MD5 checksum of the
corresponding primary file (the file without the """,
            emphasis(".md5"),
            """ suffix).  Such files can be used to verify the integrity of the corresponding primary
file using an appropriate tool.  If you have any trouble working with the primary file, then
checking its integrity is an appropriate troubleshooting step.""",
        ]
    )


####################################################################################################
# TODO: RENAME: these with single underscore prefix to make them module-private


def get_output(content):
    return _get_serializer().serialize(content)


def print_output(output):
    print((output.encode(_get_default_encoding())))


####################################################################################################
# TODO: DELETE: these


def _style():
    return htmltags.style()[
        "body {font-family: serif; font-size: 100%;}\n",
        "h1.task {color: green; font-family: sans-serif; font-size: 2.00em;}\n",
        "h2.step {color: orange; font-family: sans-serif; font-size: 1.50em;}\n",
        "p {color: black; font-size: 1.00em;}\n",
        "span.literal {color: blue; font-family: monospace; font-weight: bold; font-size: 1.25em;}\n",
        "span.emphasis {color: purple; font-style: italic;}\n",
    ]


def _title(identifier, name):
    return htmltags.title("task")["Task {0}".format(identifier)]


def head(task_identifier, task_name):
    return htmltags.head[_meta(), _style(), _title(task_identifier, task_name)]


def step(identifier, name):
    return htmltags.h2("step")["Step {0} - {1}".format(identifier, name)]


def task(identifier, name):
    return htmltags.h1("task")["Task {0} - {1}".format(identifier, name)]


""" Disabled content
"""
