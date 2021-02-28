# TODO: How do I pin Nix repository version?
with import <nixpkgs> {};
let
    # TODO: These two are not Python libraries,
    # so how do I include them?
    # awscli
    # icdiff
    pythonEnv = python39.withPackages (ps: [
        # TODO: How do I pin library versions?
        ps.ansi2html
        ps.black
        ps.boto3
        ps.coverage
        ps.logzero
        ps.pytest
        ps.pytest-cov
        ps.pytest-html
        ps.pytest-sugar
    ]);
in mkShell {
    buildInputs = [
        pythonEnv
    ];
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

