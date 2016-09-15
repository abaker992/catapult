# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Dispatches requests to request handler classes."""

import webapp2

from bisect import run


_URL_MAPPING = [
    ('/new', new.NewHandler),
    ('/run', run.RunHandler),
]

APP = webapp2.WSGIApplication(_URL_MAPPING, debug=False)
