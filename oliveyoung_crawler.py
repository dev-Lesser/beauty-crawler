#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from lxml import html


# ### 예제
# - 스킨/로션/올인원 카테고리

# In[9]:


page = 2
url = 'https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100010008&fltDispCatNo=&prdSort=01&pageIdx={page}&rowsPerPage=24&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&trackingCd=Cat100000100010008_Small'.format(page=page)


# In[10]:


res = requests.get(url)
res


# ### 아래에서 사용할 goodsNo

# In[11]:


root= html.fromstring(res.text)
item_number = root.xpath('//div[@class="prd_info "]/../@criteo-goods')
item_number


# In[12]:


url = 'https://www.oliveyoung.co.kr/store/goods/getGdasNewListJson.do'


# In[13]:


params = {
    'goodsNo': item_number[0][:-3],#A000000161782001 뒤의 세자리는 빼줘야 함
    'gdasSort': '02', # 최신순
    'itemNo': 'all_search',
    'pageIdx': 1, # pagination
}
headers = {
    'X-Requested-With': 'XMLHttpRequest'
}
res = requests.get(url, params=params, headers=headers)
results = res.json()


# ### item name

# In[14]:


[i.get('goodsNm') for i in results.get('gdasList')]


# ### reviews

# In[15]:


[i.get('gdasCont') for i in results.get('gdasList')]