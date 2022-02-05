"""
@ File: __init__.py
@ Author: CatNeverCodes
@ Created: 2022-02-05
"""


__version__ = "0.1.1"

import os
import json
import time
import requests

from typing import Union, Optional

from . utils import timer, load_config

config = load_config()
default_message = "Nothing To Speak."
dingtalk_webhook = config["dingtalk"]["webhook"]
dingtalk_mobiles = config["dingtalk"]["mobiles"]

from . messager import send_dingtalk

__all__ = ["timer", "send_dingtalk"]