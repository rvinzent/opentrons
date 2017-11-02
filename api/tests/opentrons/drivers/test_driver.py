import pytest


@pytest.fixture
def smoothie(monkeypatch):
    from opentrons.drivers.smoothie_drivers.v3_0_0.driver_3_0 import \
         SmoothieDriver_3_0_0 as SmoothieDriver

    monkeypatch.setenv('ENABLE_VIRTUAL_SMOOTHIE', 'true')
    driver = SmoothieDriver()
    driver.connect()
    yield driver
    driver.disconnect()
    monkeypatch.setenv('ENABLE_VIRTUAL_SMOOTHIE', 'false')


def position(x, y, z, a, b, c):
    return {axis: value for axis, value in zip('XYZABC', [x, y, z, a, b, c])}


def test_plunger_commands(smoothie, monkeypatch):
    from opentrons.drivers.smoothie_drivers.v3_0_0 import serial_communication
    command_log = []
    smoothie.simulating = False

    def write_with_log(command):
        command_log.append(command)
        return serial_communication.DRIVER_ACK

    monkeypatch.setattr(serial_communication, 'write_and_return',
                        write_with_log)

    smoothie.home()
    smoothie.move(x=0, y=1, z=2, a=3)
    smoothie.move(x=0, y=1, z=2, a=3, b=4, c=5)

    assert command_log == []


def test_functional(smoothie):
    from opentrons.drivers.smoothie_drivers.v3_0_0.driver_3_0 import HOMED_POSITION  # NOQA

    assert smoothie.position == position(0, 0, 0, 0, 0, 0)

    smoothie.move(x=0, y=1, z=2, a=3, b=4, c=5)
    assert smoothie.position == position(0, 1, 2, 3, 4, 5)

    smoothie.move(x=1, z=3, c=6)
    assert smoothie.position == position(1, 1, 3, 3, 4, 6)

    smoothie.home(axis='abc', disabled='')
    assert smoothie.position == position(
        1, 1, 3,
        HOMED_POSITION['A'],
        HOMED_POSITION['B'],
        HOMED_POSITION['C'])

    smoothie.home(disabled='')
    assert smoothie.position == HOMED_POSITION
