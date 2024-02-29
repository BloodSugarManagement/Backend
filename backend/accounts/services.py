from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response
from rest_framework.request import Request
import requests
import logging
from json import JSONDecodeError
from typing import Union, Dict, Any

from .models import CustomUser


logger = logging.getLogger(__file__)


def user_does_not_exist(user: CustomUser, created: bool, ptf: str, uid: str) -> Response:
    platform = {
        "kakao": "kakao",
        "google": "google",
        "naver": "naver",
    }
    logger.debug(f"uid: {uid}")
    try_login_platform: str = platform.get(ptf)
    if created:
        SocialAccount.objects.create(user_id=user.id, provider=try_login_platform, uid=uid)
        access_token: AccessToken = AccessToken.for_user(user)
        refresh_token: RefreshToken = RefreshToken.for_user(user)

        return Response({'refresh': str(refresh_token), 'access': str(access_token), "msg": "회원가입 성공"},
                        status=status.HTTP_201_CREATED)


def social_user_login(user: CustomUser) -> Response:
    refresh: RefreshToken = RefreshToken.for_user(user)

    return Response({'refresh': str(refresh), 'access': str(refresh.access_token), "msg": "로그인 성공"},
                    status=status.HTTP_200_OK)


def access_token_is_valid(request: Request) -> Union[Dict[str, Any], Response]:
    if request.status_code != 200:
        error_message = {"err_msg": "Access token이 올바르지 않습니다."}
        return JsonResponse(error_message, status=request.status_code)
    return request.json()


def request_access_token_by_auth_code(request, auth):
    code = request.GET.get("code")

    auth["auth"]["code"] = code  # NOTE: CODE값 추가

    logger.debug(f"token request auth: {token_request(auth)}")
    token_req = requests.get(token_request(auth))  # TODO: GET 요청

    token_response_json = token_req.json()

    error = token_response_json.get("error")

    if error is not None:
        logger.error(f"error: {error}")
        raise ValueError(error)

    logger.debug(f"token request access token: {token_response_json.get('access_token')}")

    return token_response_json.get('access_token')


def token_request(auth):
    platform = auth.get("platform")
    print(f"platform: {platform}")

    platform_url = {
        "kakao": "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id="
                 "{client_id}&redirect_uri={callback_uri}&code={code}",
        "google": "https://oauth2.googleapis.com/token?client_id={client_id}&client_secret="
                  "{client_secret}&code={code}&grant_type=authorization_code&redirect_uri="
                  "{callback_uri}&state={state}",
        "naver": "https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id="
                 "{client_id}&client_secret={client_secret}&code={code}&state={state}",
    }

    return platform_url.get(platform).format(**auth.get("auth"))
