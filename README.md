"# text_and_image_crawing" 

## 목적
- crawling을 연습하기 위해 만들어진 코드
- 연습 내용은 현재 네이버의 실시간 검색 순위를 crawling 함

## History
2020/1/22
- 홈페이지에 표시되는 부분의 코드를 확인 하기 위해서는 크롬 브라우져에서 개발자 모드 화면 중 'Ctrl + shift + c'를 통해
확인 하고자 하는 코드의 위치를 볼 수 있다.

- https://www.youtube.com/watch?v=ZTJjW7XuHIY&t=366s 의 참고해서 작성했지만, 네이버에서 실시간 검색 순위에 대한 HTML 위치가 변경되었다.
'www.naver.com'말고 여기서 실시간 검색 순위가 연될 된 부분에서 파싱 해야 된다. 'www.naver.com'에서 연결된 부분을 찾는 방법은 '크롬->개발자 도구'에서 XHR를 참고해서 찾아야 한다.