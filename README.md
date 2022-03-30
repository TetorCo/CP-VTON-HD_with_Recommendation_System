# CP-VTON-HD_with_Recommendation_System(추천시스템)

## 출처 : https://github.com/shadow2496/VITON-HD (저작권에 관한 모든 법률은 원본을 따릅니다. / 문제가 있을시 Repo를 비공개 처리 하겠습니다.)

## 프로젝트 기획 배경 및 설명
* 기획 배경
  * 사람들이 사고 싶은 옷을 사서 입어봤을 때 생각보다 만족도가 떨어지는 경우가 종종 있습니다. 그렇게 되면 자주 안 입게 되고 처리하기가 곤란한 상황도 올 수 있는 불편함을 해소하고자 기획하게 되었습니다.
* 설명
  * 내가 입어보고 싶은 옷을 집에서도 웹 사이트를 사용해서 실제로 입었을 때 느낌을 알아보고 구매 여부를 결정하는 것을 도와주고 업로드한 옷과 비슷한 옷을 추천해주는 프로젝트입니다.
![cpvtonhomepage](https://user-images.githubusercontent.com/76984534/160874287-857edf6e-b7dd-4c3a-a929-f8d934546d99.png)


## 모델 선정 과정
Virtual-On 모델 종류 중 하나인 Image-based Virtual-On 모델을 사용하기로 했고, 더 고화질의 이미지를 생성할 수 있는 CP-VTON-HD 모델을 선택하였습니다. 모델을 직접 구현하고 학습을 하는 것에 한계가 있었기 때문에 출처 링크에서 모델을 가져와서 유저가 업로드하는 사람 이미지와 옷 이미지를 적용시키는 것으로 결정했습니다.

## 프로젝트 진행 중 발생한 문제점 및 해결 방안
* 모델이 학습하기 위해서는 이미지를 피팅 모델과 옷 이미지를 CP-VTON에 맞게 전처리를 해주어야 했다. 그래서 피팅 모델은 수정하지 않고 저장되있는 것을 사용하고 사용자가 업로드한 옷 이미지만 모델이 학습할 수 있도록 전처리를 해주었다. (순서 : 원본 -> resize -> 오츠의 알고리즘을 이용하여 흑백 전환)

## 내부 디렉토리 구조
```
flask
┖ __pycache__
┖ static
  ┖ convert         # 변환된 결과를 저장
  ┖ image           # html에 사용하는 이미지
  ┖ upload_image    # 사용자가 업로드한 이미지
┖ templates
  ┖ end.html			  # 만족도까지 입력 받은 다음 main.html로 돌아가기 위한 페이지
  ┖ main.html		    # 메인 페이지
  ┖ view.html		    # 결과 값을 출력하는 페이지
┖ VITON_HD          # CP-VTON-HD 모델을 실행하는 파일
  ┖ __pycache__
  ┖ checkpoints     # 사전학습된 체크 포인트가 저장
    ┖ .gitignore
    ┖ alias_final.pth
    ┖ gmm_final.pth
    ┖ seg_final.pth
  ┖ datasets        # 모델 학습에 필요한 데이터
    ┖ test
      ┖ cloth         # 유저들이 업로드한 옷 이미지
      ┖ cloth-mask    # upload_cloth_segmention.py를 적용한 이미지
      ┖ image         # 사전 학습된 피팅 모델들 이미지
      ┖ image-parse   # 현재 모델의 segmentation map
      ┖ openpose-img  # openpose라이브리로 모델의 관절 포인트 검출 
      ┖ openpose-json # 관절 포인트의 json 파일
    .gitignore
    test_pairs.txt    # 모델이 학습할 피팅 모델의 이미지와 옷 이미지
  .gitignore
  datasets.py       # 모델이 학습할 수 있도록 전처리하는 파일
  networks.py       # 사용할 모델을 제작한 파일
  test.py           # 모델을 동작하는 파일
  utils.py          # 이미지 저장, 체크포인트 로드 확인 등을 수행하는 파일
.gitignore
main.py             # flask 실행 파일
mysql.py            # mysql에 만족도를 저장하는 파일
requirements.txt	  # 필요한 라이브러리 모음
upload_cloth_segmention.py  # 모델이 업로드한 이미지를 학습할 수 있게 segmention 해주는 파일
```

## 프로젝트 결과
![cp](https://user-images.githubusercontent.com/76984534/160847977-d156796e-23f6-46c7-823b-0057d778318f.png)

## 사용한 프로그램
* HTML : 웹 페이지 제작
* Python(Flak) : 서버 연결
* MySQL : 사용자에게 만족도를 받아서 저장

## 발전 방향
1. 추천 시스템 구현 (필수!)
2. 사용자가 지정되 있는 피팅 모델이 아니라 본인의 모습으로 모델에 적용할 수 있도록 코드를 수정
3. EC2나 Heroku에도 배포
4. Docker Image로 만들어서 Docker Hub에 
