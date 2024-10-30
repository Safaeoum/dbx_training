from training_objets_trouves.utils.emails import get_initials


def test_get_initials():
    assert get_initials("john.doe@example.com") == "jd"
    assert get_initials("alice.bob.charlie@example.com") == "abc"
    assert get_initials("john.@example.com") == "j"
    assert get_initials("") == ""
    assert get_initials("@example.com") == ""
    assert get_initials("john2.doe3@example.com") == "jd"
