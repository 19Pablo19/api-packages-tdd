from setuptools import setup, find_packages

setup(name = 'package',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    test_suite="tests"
    # install_requieres = [
    #     'flask'
    # ],
    # test_requiere = [
    #     ''
    # ]
    )
