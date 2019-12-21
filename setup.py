import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='report-generator',
     version='0.2',
     author="Shashank Sharma",
     author_email="shashank.sharma98@gmail.com",
     description="To generate reports",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT',
     install_requires=["fpdf"],
     include_package_data=True,
     url="https://github.com/isohack/report_generator",
     packages=['report_generator'],
     package_dir={'report_generator': 'report_generator'},
)