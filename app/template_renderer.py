from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

def render_notification(channel: str, recipient: str, message: str) -> str:
    template = env.get_template("notification_template.j2")
    return template.render(channel=channel, recipient=recipient, message=message)