accommodation_query = """
[out:json][timeout:25];
area(3604583125)->.searchArea;
(
  node["tourism"](area.searchArea);
  way["tourism"](area.searchArea);
  relation["tourism"](area.searchArea);
);
out body;
>;
out skel qt;
"""

