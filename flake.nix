{
  description = "devshell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
        let
          pkgs = import nixpkgs {
            inherit system;
          };
        in
          {
            devShells.default = with pkgs; mkShell {
	      name = "nix";
              LD_LIBRARY_PATH = lib.makeLibraryPath [
                stdenv.cc.cc.lib
                zlib
                "/run/opengl-driver"
              ];
              NIX_ENFORCE_NO_NATIVE = 0;
              buildInputs = [
                uv
		python312Full
              ];
            };
          }
    );
}
