from ._reporter import HueReporter


def pytest_addoption(parser):
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--hue-ip',
        dest='hue_ip',
        action='store',
        type=str,
        default=None,
        help='IP address for Phillips Hue reporting'
    )
    group.addoption(
        '--hue-username',
        dest='hue_username',
        action='store',
        type=str,
        default=None,
        help='Username for Phillips Hue reporting'
    )
    group.addoption(
        '--hue-rooms',
        dest='hue_rooms',
        action='store',
        type=str,
        nargs='+',
        default=[],
        help='Rooms to control with Phillips Hue reporting'
    )


def pytest_configure(config):
    hue_ip = config.option.hue_ip
    hue_username = config.option.hue_username
    hue_rooms = config.option.hue_rooms
    if hue_ip:
        config._hue_reporter = HueReporter(hue_ip, hue_username, hue_rooms)
        config.pluginmanager.register(config._hue_reporter)


def pytest_unconfigure(config):
    hue_reporter = getattr(config, '_hue_reporter', None)
    if hue_reporter:
        del config._hue_reporter
        config.pluginmanager.unregister(hue_reporter)
