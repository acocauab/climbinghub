![UnitTests](https://github.com/acocauab/climbinghub/workflows/UnitTests/badge.svg)

Objective
=========

Get climbing route from webs in internet and classify them so it is easier to
find the routes we want.

How to classify the route?
==========================

Grade:
------
How difficult is the route.
  
- Climbing: V+, 6a ...
- Artificial: A-1, Ae ...
- Dificulty: D, BD ...


How to find it:
- If climbing is in the title take it from there.
- If it's not there then look at the `<h1></h1> <h2></h2> <h3></h3>`
- If it's not there then look all the `<p></p>` and similar tags and try to get
  the highest grade found there. NOTE: looking at <a> tags might get a wrong 
  grade since it can be titles or other routes.

Zone:
-----

  - GPS: With the track if any
  - Name: Seems very difficult. Any ideas?

Type:
-----

  - Via Classica: Friends, Tascons, Fisureros...
  - Via Llarga: Largo, Parabolt
  - Esportiva: Not sure yet.
  - Cresta?: Cresta
  - Alpinisme? Hivernal? Gel? Piolet, Grampons, Gel, Neu

Which extra information I want?
===============================

- Name of the route: -> Web title
- Original URL: -> Original url
- Original website -> Main page from original url
- Pictures? -> All pictures that can be found in original webpage

Extra things to care about
==========================

We want this page to be multi language.
That means that the key words not necessary are the same for each language
Suport for multilanguage

Any sugestion?
==============

If you have any sugestion on this project please open an issue.


