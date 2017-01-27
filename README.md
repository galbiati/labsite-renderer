# labsite-renderer

This tool uses tornado templates to make managing lab websites easier.

`base.html` defines the basic layout, with a header, possibly a footer.

Other html files will `{% extends base.html %}`.

Page contents that require updating will be created as YAML files for easy maintenance.

For example, `people.yaml` will include dictionaries of people including their names, bios, and image filepaths, and `publications.yaml` will include publications with title, author, year, etc.

`render.py` will output static html files into the `website` directory; all image files etc will need to be preloaded into the appropriate folders of `website`.

Most of this has yet to be implemented, but it should greatly
