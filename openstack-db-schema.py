#!/usr/bin/env python
import ConfigParser
from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph
config = ConfigParser.RawConfigParser()
config.read('/etc/cinder/cinder.conf')
connection = config.get("database", "connection")
graph = create_schema_graph(metadata=MetaData(connection),
                            show_datatypes=False,
                            show_indexes=False,
                            rankdir='LR',
                            concentrate=True)
graph.write_png('dbschema.png')
