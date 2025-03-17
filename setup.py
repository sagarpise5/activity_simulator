from setuptools import setup, find_packages

setup(
    name="activity_simulator",
    version="1.0",
    packages=find_packages(),
    install_requires=["evdev"],
    entry_points={
        "console_scripts": [
            "desklog-start=activity_simulator.simulator:start",
            "desklog-stop=activity_simulator.simulator:stop",
        ],
    },
    author="Sagar",
    description="A tool to simulate user activity (mouse, keyboard) to prevent idle tracking.",
)
