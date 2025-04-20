# Packages

Packages are lightweight apps that can be directly built from the Framework UI. A package is similar to an app and is a collection of Module Defs. These apps can be bundled into a "Package" and imported to other sites.

## Creating a Package

1. Create a new Package object.
2. Set a README and LICENSE.
3. Add custom Module Defs to the package.

## Making a Package Release

1. Export all package modules to the `[bench]/sites/[site]/packages` folder.
2. Bundle the folder into a gzipped tarfile `[package]-[version].tar.gz`.
3. Download the package release and import it to another site.

## Importing a Package

1. Create a `Package Import` and attach the exported package to a new site.
2. Check "Activate" to extract the package into the `[bench]/sites/[sitename]/packages` folder.
3. Run migrations to update the database.