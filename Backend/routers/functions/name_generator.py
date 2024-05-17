import os
import re

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.name_generator import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_acrostic_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    order_list = "\n".join([item.strip() for item in model.order.split("/")])

    return OutputModel(
        output=chain.invoke({
            'input_context': order_list,
        }),
    )
