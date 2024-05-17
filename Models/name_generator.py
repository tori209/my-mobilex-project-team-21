from typing import Literal

from pydantic import BaseModel, Field


class InputModel(BaseModel):
    order: str = Field(
        alias='order',
        description='삼행시에 사용될 초성 단어를 입력해주세요!',
        default='명령1 / 명령2 / ...',
        pattern=r'^[a-z|가-힣|0-9|\s]+(\s*\/\s*[a-z|가-힣|0-9|\s|\.,\-\_\!\@\#\$\%\^\&\*\(\)\[\]\{\}\"\'\:\;\/\\\<\>\+\=]+)*$'
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )

class OutputModel(BaseModel):
    output: str = Field(
        description='당신에게 다음의 이름을 추천드립니다!',
    )
