#!/usr/bin/env python
# Copyright 2016 The Fuchsia Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import json
import gn
import os
import paths
import sys


def main():
    parser = argparse.ArgumentParser(description="Generate Ninja files for Fuchsia")
    parser.add_argument("--args", dest="gn_args", help="additional args to pass to gn",
                        action="append")
    parser.add_argument("--modules", "-m", help="comma separted list of modules",
                        default="default")
    parser.add_argument("--release", "-r", help="generate release mode build files",
        action="store_true")
    parser.add_argument("--outdir", "-o", help="output directory", default="out/debug")
    parser.add_argument("--target_cpu", "-t", help="Target CPU", default="x86-64",
                        choices=['x86-64', 'aarch64'])
    parser.add_argument("--goma", help="use goma", metavar="GOMADIR",
                        nargs='?', const=True, default=False)
    (args, passthrough) = parser.parse_known_args()

    if args.release:
        args.outdir = "out/release"

    # TODO: Do not clobber user specified output dir
    args.outdir += "-" + args.target_cpu

    outdir_path = os.path.join(paths.FUCHSIA_ROOT, args.outdir)

    gn_command = ["gen", outdir_path, "--check"]

    cpu_map = {"x86-64":"x64", "aarch64":"arm64"}
    gn_args = "--args=target_cpu=\"" + cpu_map[args.target_cpu]  + "\""
    gn_args += " modules=\"" + args.modules + "\""

    if args.release:
        gn_args += " is_debug=false"
    if args.goma:
        gn_args += " use_goma=true"
        if type(args.goma) is str:
            path = os.path.abspath(args.goma)
            if not os.path.exists(path):
                parser.error('invalid goma path: %s' % path)
            gn_args += " goma_dir=\"" + path + "\""
    if args.gn_args:
        gn_args += " " + " ".join(args.gn_args)

    gn_command += [gn_args]
    if passthrough:
        gn_command += passthrough

    return gn.run(gn_command)


if __name__ == "__main__":
    sys.exit(main())
