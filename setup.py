import os
from setuptools import setup

setup(
    version="2.1.0",
    name="dcm-sip-builder-api",
    description="api for sip-builder-containers",
    author="LZV.nrw",
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
