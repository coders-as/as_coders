# 학습조직 시작하기 전 읽어주세요

0. (windows 의 경우) git 다운로드
```python
/*** git clone 을 하는 경우에는 아래 명령어가 필요없음 ***/
$ git init
$ git status
```
1. 원격저장소 연결

    1. 최초 작업시 - clone
    ```python
    $ git clone https://github.com/coders-as/as_coders.git
    $ git remote -v # 실행시 원격저장소명 origin 확인
    $ git config --global credential.helper store # 인증정보를 Disk에 저장하고 계속 유지
    $ git config --global user.name "[your_name]"
    $ git config --global user.email "[your_email_address]"
    ```
    2. 기존 연결된 저장소가 있을 때 - pull
    ```python
    $ git checkout main
    $ git pull
    ```

2. branch 생성 및 작업위치 변경
```python
$ git branch [branch_name]
$ git checkout [branch name]
```

3. local PC 에서 작업 후 add, commit, push 진행
- 파일명은 <font color="green">**해당 문제가 있는 폴더 내**</font>에서 solution_[my_nickname].py 로 작성
  - 예시 : <font size="4px" color="green">**solution_LSM**</font>.py
- commit comment 는 [my_nickname]_yyyymmdd_nth 으로 작성 
  - nth : 해당 날짜에 commit 한 순서
  - 예시 : git commit -m "<font size="4px" color="green">**LSM_20210426_001**</font>"
```python
$ git add [file_path] / git add * / git add . (해당 폴더 내에서)
$ git commit -m "[comment]"
$ git push origin [branch_name]
```
* 참조
![](https://www.secmem.org/assets/images/git_pr/git_transaction.png)

4. <font size="4px" color="RED">pull request 생성 (필수)</font>
- 본인 github 저장소에서 Compare & pull reqeust 버튼 클릭
- 메시지를 작성하고 PR을 생성

5. PR을 받은 관리자는 메시지란에 <font color="green">**코드 리뷰**</font> 작성 이후 Merge
