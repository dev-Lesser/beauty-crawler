### 뷰티 사이트 크롤러

### Notice
- 개인적 공부를 위한 용이지, 이걸 이용한 상업적 이익 + 해당 서비스에 심각한 방해를 초래시 법적인 책임을 물을 수 있습니다.

### v1 HTML 파싱
- BeautifulSoup 극혐한다. 안 쓴다.
- 셀레니움 극혐한다. 절대로 셀레니움을 안 쓸 것이다. 무겁다
- 셀레니움 안쓰니까 javascript render 페이지는 requests_html, phantomJS 등으로 Headless 하게 할 것임 
    - 이런 경우는 javascript 를 할 줄 안다면 오히려 javascript 로 언어를 바꾸는 것을 추천한다.

### 완료 사이트
- [x] 언니의파우치
- [x] 올리브영
- [x] 가가몰 & 스킨큐어 > 같은 API 형식
- [x] 아모레퍼시픽 & 에뛰드 > 같은 형식
- [x] 이니스프리
- [x] 아마존
- [ ] 미샤
- [x] 더샘
- [x] 네이처리퍼블릭
- [x] 더페이스샵
- [ ] 이외 필요한 화장품 브랜드가 있으면 깃헙 issue 로 요청