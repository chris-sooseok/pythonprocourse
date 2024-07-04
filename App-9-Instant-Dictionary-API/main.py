
import api
import documentation

import justpy as jp


jp.Route(documentation.Doc.path, documentation.Doc.serve)
jp.Route(api.Api.path, api.Api.serve)

jp.justpy(port=8000)