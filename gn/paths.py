#!/usr/bin/env python
# Copyright 2016 The Fuchsia Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import platform

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FUCHSIA_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, os.pardir, os.pardir))
GN_PATH = os.path.join(FUCHSIA_ROOT, "buildtools", "gn")
MKBOOTFS_PATH = os.path.join(FUCHSIA_ROOT, "out", "build-magenta", "tools", "mkbootfs")
BUILDTOOLS_PATH = os.path.join(FUCHSIA_ROOT, "buildtools", '%s-%s' % (
    platform.system().lower().replace('darwin', 'mac'),
    {
        'x86_64': 'x64',
        'aarch64': 'arm64',
    }[platform.machine()],
))
DEBUG_OUT_DIR = os.path.join(FUCHSIA_ROOT, "out", "debug-x86-64")
RELEASE_OUT_DIR = os.path.join(FUCHSIA_ROOT, "out", "release-x86-64")
