from setuptools import setup

setup(
        name="rplp",
        version="0.1",
        py_modules=["rplp"],
        install_requires=["requests", "bs4"],
        entry_points={
            "console_scripts":[
                "rplp = rplp:main",
            ],
        }
)
