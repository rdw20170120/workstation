# Borrowed from https://gist.github.com/AndersonTorres/9fa2b059da82c951f7c9036dd054fdb1
let
    baseUrl = "https://github.com/NixOS/nixpkgs/archive";
    stable = {
        tag = "20.09";
        # sha256 is optional for builtins.fetchTarball
    };
#   unstable = {
#       tag = "fce7562cf46727fdaf801b232116bc9ce0512049";
        # sha256 is optional for builtins.fetchTarball
#   };
    nixpkgsStable = builtins.fetchTarball {
        url = "${baseUrl}/${stable.tag}.tar.gz";
    };
#   nixpkgsUnstable = builtins.fetchTarball {
#       url = "${baseUrl}/${unstable.tag}.tar.gz";
#   };
    in nixpkgsStable

