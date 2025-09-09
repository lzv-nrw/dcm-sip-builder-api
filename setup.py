import os
from setuptools import setup

setup(
    version="3.0.0",
    name="dcm-sip-builder-api",
    description="specification of the DCM SIP Builder API",
    author="LZV.nrw",
    license="MIT",
    install_requires=[
    ],
    packages=[
        "dcm_sip_builder_api"
    ],
    package_data={
        "dcm_sip_builder_api": [
            "dcm_sip_builder_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
