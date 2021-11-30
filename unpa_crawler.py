#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from lxml import html


# In[11]:


UNPA_REVIEW_URL = 'https://www.unpa.me/review?sort=createdAt'
URL_PREFIX = 'https://www.unpa.me'


# In[12]:


res = requests.get(UNPA_REVIEW_URL)
res


# In[13]:


root = html.fromstring(res.text)

review_urls = [URL_PREFIX + i for i in root.xpath('//div[contains(@class, "unpa-card")]/@data-unpa-url')]

# #### next page url 가져오기
# - page 번호로 하는것이 아닌 load more 로 진행하기 때문에, javascript 없이 가능하지 않음
# - 이 부분에서는 cursor 를 가지고 한다
# - 그럼 cursor 의 정보는 어디에 있는가
# - query 를 날리는 cursor 부분을 decoding 을 하였을때 advertisements, CsStartIndex 의 dict 형태였다 이걸 기준으로 decode 텍스트를 만들어 준다
# - page 를 0 부터 하면 가장 최신 것 부터 가져오는 것을 확인 default 로 9개씩 가져오는 것도 확인함

# In[116]:


# 예제
page = 1111
decode_query = '''{"advertisements":"empty","CsStartIndex":"%d"}''' % page
decoded_text = quote(decode_query)
decoded_text


# In[122]:


from urllib.parse import quote
urls = []
page= 0
while True:
    decode_query = '''{"advertisements":"empty","CsStartIndex":"%d"}''' % page
    decoded_text = quote(decode_query)
    params = {
        'sort': 'createdAt',
        'isLoadMore': 'true',
        'cursor': decoded_text
    }
    res = requests.get(URL_PREFIX + '/review', params=params)
    root_next = html.fromstring(res.json()['body'])
    data = root_next.xpath('//div[contains(@class, "unpa-card")]/@data-unpa-url')
    if data:
        urls.extend(data)
        print('''===== url parse end \t page = %d''' % page)
        page += 9
    else:break


# In[125]:


# 중복체크
len(list(set(urls))) == len(urls)


# #### 위에 있는 urls 를 가지고 각 상품별 리뷰의 메타데이터를 가지고 올 수 있음

# In[127]:


res = requests.get(URL_PREFIX+urls[0])
res


# ### 리뷰 아이템

# In[128]:


root_detail = html.fromstring(res.text)


# In[129]:


brand_xpath = '//div[@class="brand-name"]'
brand = root_detail.xpath(brand_xpath + '/text()')
brand


# In[130]:


product_name_xpath = '//div[@class="product-name"]'
product_name = root_detail.xpath(product_name_xpath + '/text()')
product_name


# In[131]:


score_xpath = '//div[@class="product-image-and-name"]/div/div[@class="rating-badge"]/span[@class="rating-value"]'
score = [i.strip() for i in root_detail.xpath(score_xpath +'/text()')]
score


# In[132]:


reviews_xpath = '//div[@class="resource"]/div[@class="text"]'
reviews = root_detail.xpath(reviews_xpath + '/text()')
' '.join(reviews)


# In[133]:


images_xpath = '//div[@class="resource"]/figure/img'
images = root_detail.xpath(images_xpath +'/@src')
images


# In[ ]:




