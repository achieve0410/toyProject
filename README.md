# toyProject

도움 받은 곳: https://2zycoding.tistory.com/4?category=888796

트러블슈팅:

1. 5432에러.. 소켓에 프로세스도 안보이고.. psql은 구동되는데 ps -ef 로 안보인다..
 - 한-------참을 헤매다 /etc/hosts 파일이 비어있는 것을 확인.
 - localhost == 127.0.0.1 이라는 것을 컴퓨터가 몰라서 localhost:5432로 프로세스를 못띄운 것.
 - /etc/hosts 파일 생성 후 해결

2. 장고 서버 외부ip로 포트포워딩이 안되는 것
 - 단순 python manage.py runserver 로는 localhost로 밖에 해결이 안됨
 - python manage.py runserver 0.0.0.0:8000으로 하면 공인ip로 접근 가능!

3. allowed_host 변경
 - config/settings/local.py 에서 allowed_host = ['*'] 로 변경 => 모든 ip 접근 가능