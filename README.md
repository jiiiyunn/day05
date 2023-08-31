다음과 같이 패치합니다.

git init
필요하다면 다음의 명령을 사용하여 환경변수를 입력하세요.
git config --local user.email ' '
git config --local user.name ' '

git remote add origin https://github.com/jiiiyunn/day05.git

git pull origin master

데이터를 가져온 후 다음의 명령을 사용하여 가상환경을 구성합니다
python - m venv .venv
. .venv/bin/activate
pip freeze > requirements.txt