from setuptools import setup

setup(
    name='ceaos_sensors',
    version='0.0.1',
    packages=['ceaos_sensors'],
    install_requires=[
        'pigpio',
        'zmq',
        'Adafruit_DHT'
    ],
)
