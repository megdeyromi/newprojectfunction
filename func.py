#
# hello-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#
import io
import json
from fdk import response
import cohere
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import time

from langchain_community.embeddings import CohereEmbeddings
#from langchain_community.llms.oci_generative_ai import OCIGenAI
def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Hello World handler", flush=True)
    cohere_api_key = "TX8xfSGQm7btpYjQBrf3qYHyo7M9gAXtGrp2kJtT"
    co = cohere.Client(cohere_api_key)
    name = "World"
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)

    print("Vale of name = ", name, flush=True)
    print("Exiting Python Hello World handler", flush=True)
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )
