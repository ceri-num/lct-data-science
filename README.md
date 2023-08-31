# Data Sience: Lecture ressources

Data Sience: Lecture ressources

- **Licence:** This solution is distributed under the [MIT license](./LICENCE.md) and come with no more guarantee than the devotion of the authors.
- **Authors:** Guillaume Lozenguez

## Get Stated:

This directory and all the included filles leads on _Git_ repository and the extention to handle large files (LFS).
Make sure you have this two elelement installed on your machine.

With `apt` under a Ubuntu system:

```bash
sudo apt update
sudo apt install git git-lfs
```

On **GitLab**, **GitHub** or **Bitbucket**, it is recommanded to reccord a _ssh_ key in order to make you on your machine identifiable by those web-services.

You can now get all the elements, i.e. clone the distant repository (make a local copy of all it contents and it history) : 

```bash
git clone git@bitbucket.org:imt-mobisyst/lecture-data-science.git lct-data-science
cd lct-data-science
ls
```


## Some Tools

### Slide Presentations

The presentation/slides are prepared using `marp` (an extantion to Markdown permiting to generate slides pdf).
`marp` is fully integrated to VisualCode:

- Get *Marp for VS Code* extention
- On `VS Code parameters > working space > Marp for VS Code` you can add elements on `Markdown › Marp: Themes` : `style/imt-slide.css`.


### Overleaf Web-Editor

[Overleaf](https://www.overleaf.com) is a Latex dedicated web-editor.

It is possible to clone locally overleaf project based on `git` tool.
For instance to clone `PROJECT-NAME` with overleaf code `CODE` : 

```sh
git clone https://$OVERLEAF_ID@git.overleaf.com/CODE PROJECT-NAME
```

Your `$OVERLEAF_ID` is typically your e-mail and the code is the one in the overleaf url of your project.

For instance: 
```sh
export OVERLEAF_ID=guillaume.lozenguez%40imt-nord-europe.fr
git clone https://$OVERLEAF_ID@git.overleaf.com/6374b3bd73dbc0e894cf0901 my_wonderfull_project
```

## New on Git

- **Git** is a decentralized solution for version management. Its first feature is to allow several contributors to work on a same directory, each one on its own machine.
It permits to share an entire historic of all modifications through a common *repo* on a server, to facilitate fusion of document version (mainly by using text format), and to do it in a safe way.

- A **GitServer**, *Bitbucket*, *GitHub*, [framagit](https://framagit.org) or private install of gitlab (*[gvipers](gvipers.imt-lille-douai.fr)* at IMT Lille Douai), propose solutions based on *git* to share a directory or repository on the cloud with management services (groups, members, access rules).

- **Markdown Documents** is a text format, very simple and directly interpretable on all _git_ server solutions. The format follows the philosophy: **What you see is what you get**

- Going further with Git:
	* [Learn Git](https://try.github.io/)
	* [GitForWindows](https://gitforwindows.org/) a simple IDE for Windows.
	* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
