## Simplify-view api endpoints

### 일반유저
<details>
<summary>회원가입</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|POST|http://52.78.93.9:8000/accounts/register/|회원가입|
```
{
    email: "dev@test.com",
    age_range: "20대",  # note: 10대 ~ 80대
    password: "greater eqaul than letter 8",
    password2": "password validation",
}
```
</div>
</details>

<details>
<summary>로그인</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|POST|http://52.78.93.9:8000/accounts/login/|로그인|

```
{
    email: "dev@test.com",
    password: "key in password",
}
```
</div>
</details>

<details>
<summary>로그아웃</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|POST|http://52.78.93.9:8000/accounts/logout/|로그아웃|
</div>
</details>

### 소셜유저
<details>
<summary>구글 로그인</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|POST|http://52.78.93.9:8000//accounts/google/login-request/|구글 로그인|

```
{
    access_token: string
}
```
</div>
</details>

<details>
<summary>카카오 로그인</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|POST|http://52.78.93.9:8000/accounts/kakao/login-request/|카카오 로그인|

```
{
    access_token: string
}
```
</div>
</details>


<details>
<summary>네이버 로그인</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|POST|http://52.78.93.9:8000/accounts/naver/login-request/|네이버 로그인|

```
{
    access_token: string
}
```
</div>
</details>

### 혈당 관리
<details>
<summary>현재 날짜 페이지</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|GET|http://52.78.93.9:8000/api/management/|현재 날짜 등록 정보 확인|
|GET|http://52.78.93.9:8000/api/management/feedback/|현재 날짜 메모 확인|
|PUT|http://52.78.93.9:8000/api/management/|현재 날짜 수치 등록(정확한 표기상 수정이 맞음, 0을 기본값으로 생성되기 때문)|
```
{
    "empty_stomach": 0,
    "morning": 0,
    "lunch": 0,
    "evening": 0,
}
```

|method|url endpoint|help text|
|------|---|---|
|PUT|http://52.78.93.9:8000/api/management/feedback/|현재 날짜 메모 등록(수정)|
```
{
    "content": "text"
}
```

|method|url endpoint|help text|
|------|---|---|
|DELETE|http://52.78.93.9:8000/api/management/|현재 날짜 등록 정보 삭제 -> 해당 기능은 잘 쓰이지 않는 기능으로 204 status code를 반환함|
|DELETE|http://52.78.93.9:8000/api/management/feedback/|현재 날짜 메모 정보 삭제|
</div>
</details>

<details>
<summary>특정 날짜 페이지</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|GET|http://52.78.93.9:8000/api/management/{int:year}/{int:month}/{int:day}/|특정 날짜 등록 정보 확인|
```
{
    http://52.78.93.9:8000/api/management/23/11/27, 또는
    http://52.78.93.9:8000/api/management/2023/11/27

}
```
|method|url endpoint|help text|
|------|---|---|
|GET|http://52.78.93.9:8000/api/management/{int:year}/{int:month}/{int:day}/feedback/|특정 날짜 메모 정보 확인|
|PUT|http://52.78.93.9:8000/api/management/{int:year}/{int:month}/{int:day}/|특정 날짜 수치 등록(정확한 표기상 수정이 맞음, 0을 기본값으로 생성되기 때문)|
```
{
    "empty_stomach": 0,
    "morning": 0,
    "lunch": 0,
    "evening": 0,
}
```
|method|url endpoint|help text|
|------|---|---|
|PUT|http://52.78.93.9:8000/api/management/{int:year}/{int:month}/{int:day}/feedback/|특정 날짜 메모 정보 수정|
```
{
    "content": "text"
}
```
|method|url endpoint|help text|
|------|---|---|
|DELETE|http://52.78.93.9:8000/api/management/{int:year}/{int:month}/{int:day}/|특정 날짜 등록 정보 삭제 -> 해당 기능은 잘 쓰이지 않는 기능으로 204 status code를 반환함|
|DELETE|http://52.78.93.9:8000/api/management/{int:year}/{int:month}/{int:day}/feedback/|특정 날짜 메모 정보 삭제|
</div>
</details>

<details>
<summary>통계</summary>
<div markdown="1">

|method|url endpoint|help text|
|------|---|---|
|GET|http://52.78.93.9:8000/api/management/aggregate/week/|주간 수치 목록 확인|
|GET|http://52.78.93.9:8000/api/management/aggregate/month/|월간 수치 목록 확인|

</div>
</details>