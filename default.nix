{ nixpkgs ? import (import ./pinned.nix).nixpkgs }:
let
    pkgs = [
        nixpkgs.python39
        nixpkgs.which
    ];
in
    nixpkgs.stdenv.mkShell {
        nativeBuildInputs = pkgs;
        shellHook = ''
            source activate.bash
        '';
    }

# python3.9-pytest-6.1.2
# python3.9-coverage-5.3
# python3.9-pytest-cov-2.10.1
# python3.9-logzero-1.6.3
# awscli-1.19.5
# python3.9-boto3-1.17.5
# icdiff-1.9.5
# python3.9-ansi2html-1.6.0
# python3.9-black-20.8b1
# python3.9-pytest-html-3.1.1
# python3.9-pytest-sugar-0.9.4

