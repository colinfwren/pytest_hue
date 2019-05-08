import pyhue


class HueReporter(object):
    def __init__(self, hue_ip, hue_username, hue_rooms):
        self.bridge = pyhue.Bridge(hue_ip, hue_username)
        self.rooms = \
            [room for room in self.bridge.groups if room.name in hue_rooms]
        self.tests = 0.0
        self.run_tests = 0.0
        self.passed_tests = 0.0
        self.failed_tests = 0.0
        self.skipped_tests = 0.0

    def set_tests(self, tests):
        self.tests = tests

    def initialise_test_run(self):
        for room in self.rooms:
            for light_id in room.lights:
                light = self.bridge.get_light(light_id)
                light.on = True
                light.bri = 0
                light.xy = pyhue.rgb2xy(255, 255, 255)

    def add_run_test(self):
        self.run_tests += 1
        for room in self.rooms:
            for light_id in room.lights:
                light = self.bridge.get_light(light_id)
                brightness = int(255 * (self.run_tests / self.tests))
                red = int(255 * (self.failed_tests / self.tests))
                green = int(255 * (self.passed_tests / self.tests))
                blue = int(255 * (self.skipped_tests / self.tests))
                hue = pyhue.rgb2xy(red, green, blue)
                light.bri = brightness
                light.xy = hue

    def add_passing_test(self):
        self.passed_tests += 1
        self.add_run_test()

    def add_failed_test(self):
        self.failed_tests += 1
        self.add_run_test()

    def add_skipped_test(self):
        self.skipped_tests += 1
        self.add_run_test()

    def pytest_collection_modifyitems(self, config, items):
        self.set_tests(len(items))
        self.initialise_test_run()

    def pytest_runtest_logreport(self, report):
        if report.when == 'call':
            if report.passed:
                self.add_passing_test()
            if report.skipped:
                self.add_skipped_test()
            if report.failed:
                self.add_failed_test()
