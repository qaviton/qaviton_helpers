from qaviton_helpers import import_path, path

def test_import():
    pkg = import_path(path(__file__)("./utils/foopkg"))
    mdl = import_path(path(__file__)("./utils/foopkg/foomdl.py"))
    assert pkg.foomdl.value == 3
    assert mdl.value == 3
    m = __import__("package")
    m.manager.run()
