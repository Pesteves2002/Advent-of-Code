{
  description = "Advent of Code (AoC) flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    systems.url = "github:nix-systems/default";
    git-hooks.url = "github:cachix/git-hooks.nix";
  };

  outputs = {
    self,
    nixpkgs,
    systems,
    ...
  } @ inputs: let
    forEachSystem = nixpkgs.lib.genAttrs (import systems);
  in {
    devShells = forEachSystem (system: {
      default = let
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (self.checks.${system}.pre-commit-check) shellHook enabledPackages;
      in
        pkgs.mkShell {
          inherit shellHook;
          buildInputs = enabledPackages;
          packages = with pkgs; [
            (
              python3.withPackages (p:
                with p; [
                  pandas
                ])
            )

            hyperfine
          ];
        };
    });

    checks = forEachSystem (system: {
      pre-commit-check = inputs.git-hooks.lib.${system}.run {
        src = ./.;
        hooks = {
          alejandra.enable = true;
          deadnix.enable = true;

          ruff.enable = true;
        };
      };
    });
  };
}
