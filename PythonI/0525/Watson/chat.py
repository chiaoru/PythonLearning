# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import openai

q = input('請輸入要問的問題?')

openai.api_key = "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"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=q,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)


ans = response['choices'][0]['text'].strip()

print(ans)
