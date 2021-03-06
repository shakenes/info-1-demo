from Car import Car, NoDriverException, TooManyPassengersException
import pytest


def test_constructor():
    # these constructor calls should not work and we expect a ValueError
    with pytest.raises(ValueError):
        c = Car(-1)
    with pytest.raises(ValueError):
        c = Car(0)
    with pytest.raises(ValueError):
        c = Car(1.5)
    with pytest.raises(ValueError):
        c = Car("5")

    # This one should work
    c = Car(2)
    # check type of object
    assert isinstance(c, Car)


def test_add_passenger():
    c = Car(4)
    assert c.get_passengers() == []
    c.add_passenger("Hugo")
    assert c.get_passengers() == ["Hugo"]
    c.add_passenger("Alice")
    assert c.get_passengers() == ["Hugo", "Alice"]
    c.add_passenger("Alice2")
    c.add_passenger("Alice3")
    assert len(c.get_passengers()) == 4
    with pytest.raises(TooManyPassengersException):
        # Now there are more passengers than seats, so we expect an exception
        c.add_passenger("Alice4")
    assert len(c.get_passengers()) == 4

    # now lets tests invalid passenger names
    with pytest.raises(ValueError):
        c.add_passenger(0)

    with pytest.raises(ValueError):
        c.add_passenger({"Test": 1})

    with pytest.raises(ValueError):
        c.add_passenger(["Hugo"])

    # now lets test something stupid
    with pytest.raises(ValueError):
        c.add_passenger(Exception)


def test_accelerate():
    c = Car(4)
    with pytest.raises(NoDriverException):
        c.accelerate()
    assert c.get_speed() == 0
    c.add_passenger("Fahrerlein")
    c.accelerate()
    assert c.get_speed() == 1
    c.accelerate()
    assert c.get_speed() == 2


def test_brake():
    c = Car(4)
    c.add_passenger("Hugo")
    c.brake()
    assert c.get_speed() == 0
    c.accelerate()
    c.accelerate()
    c.brake()
    assert c.get_speed() == 1


def test_remove_passenger():
    c = Car(4)
    with pytest.raises(ValueError):  # list.remove raises a ValueError if value is not found in list
        c.remove_passenger("Herbert")
    c.add_passenger("Hugo")
    assert len(c.get_passengers()) == 1
    c.remove_passenger("Hugo")
    assert len(c.get_passengers()) == 0


def test_get_speed():
    c = Car(3)
    assert c.get_speed() == 0
    with pytest.raises(NoDriverException):
        c.accelerate()
    assert c.get_speed() == 0
    c.add_passenger("Olaf")
    c.accelerate()
    assert c.get_speed() == 1


def test_get_passengers():
    c = Car(3)
    assert c.get_passengers() == []
    c.add_passenger("Alice")
    assert c.get_passengers() == ["Alice"]
    c.add_passenger("Olaf")
    assert c.get_passengers() == ["Alice", "Olaf"]
