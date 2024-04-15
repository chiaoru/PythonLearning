# -*- coding: utf-8 -*-
"""
Created on Thu May 25 20:16:41 2023

@author: USER
"""

import os
import openai

openai.api_key = "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"

q = input('請輸入要詢問的問題:')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=q,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)
ans = response['choices'][0]['text'].strip()
print(ans)