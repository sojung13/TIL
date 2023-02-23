#### 네트워크의 분류

- `연결 정도`에 의한 분류
  - 강한 연결 (Tightly coupled)
    - 병렬컴퓨터 내부망
  - 느슨한 연결 (Loosely coupled)
    - 전산망
- `크기`에 의한 분류
  - LAN(Local Area Network)
  - MAN(Metropolitan Area Network)
  - WAN(Wide Area Network)



#### LAN

- Topology

  - 버스형

    ![image-20230223182046644](C:\Users\X-note\Desktop\새 폴더\TIL\CS\네트워크\3 네트워크 기술\assets/image-20230223182046644.png)

    - b가 e에게 메시지를 보내려고 한다면, a, c, d 모두가 e에게 보내는 메시지임을 볼 수 있어서 e가 메시지를 가져갈 수 있도록 가만히 있는다.
    - 하나의 긴 케이블이 네트워크상의 모든 장치를 연결하는 중추 네트워크의 역할을 하는 형태
    - 장점
      - 설치가 쉬움
      - 비용이 저렴
      - 각 호스트이 고장이 네트워크 내의 다른 부분에 영향을 주지 않음
    - 단점
      - 버스 케이블에 결함이 발생하면 전체 스테이션은 모든 전송을 할 수 없음
      - 네트워크에 부하가 많으면 응답시간이 늦어짐

  - 링형

    ![image-20230223182059597](C:\Users\X-note\Desktop\새 폴더\TIL\CS\네트워크\3 네트워크 기술\assets/image-20230223182059597.png)

    - 서로가 서로에게 메시지를 전달해준다.
    - 닫힌 루프 형태로 각 호스트가 자신의 양쪽 호스트와 전용으로 점 대 점으로 연결된 형태
    - 장점
      - 설치와 재구성이 쉬움
      - 장애가 발생한 호스트를 쉽게 찾음
    - 단점
      - 단방향 전송이기 때문에 링에 결함이 발생하면 전체 네트워크를 사용할 수 없음
      - 새로 호스트를 추가하기 위해서는 물리적으로 링을 절단하고 호스트를 추가해야 함

![image-20230223182124890](C:\Users\X-note\Desktop\새 폴더\TIL\CS\네트워크\3 네트워크 기술\assets/image-20230223182124890.png)

왼쪽과 같이 망을 설정할 경우, 만약 b 장비가 꺼져 있다면 순환이 되지 않는다.

오른쪽과 같이 망을 설정할 경우, 어떤 장비가 꺼져 있더라도 관련된 데이터를 싣거나 복사할 수 있다.



- 이더넷 (Ethernet)

  ![image-20230223182429136](C:\Users\X-note\Desktop\새 폴더\TIL\CS\네트워크\3 네트워크 기술\assets/image-20230223182429136.png)

  - Xerox - Palo Alto 연구소
  - 컴퓨터 네트워크 기술의 하나로, 일반적으로 LAN, MAN 및 WAN에서 가장 많이 활용되는 기술 규격
  - CSMA/CD (Carrier Censed Multiple Access Collision Detection) 방식
    - `캐리어 센스 (Carrier Sensed) `
      - 캐리어 (Carrier) : 이더넷 환경에서 통신을 하고 싶은 PC나 서버는 먼저 지금 네트워크 상에 통신이 일어나고 있는지 확인. 즉, 우리가 자원을 쓰고 있는 PC나 서버가 있는지 확인해보는 것.
      - 이러한 캐리어를 감지하는 것
    - `이중 접근 (Multiple Access)`
      - 두 개 이상의 PC나 서버가 동시에 네트워크 상에 데이터를 실어 보내는 경우 
    - `Collision Detection`
      - 충돌 (Collision) : 두 개의 장비들이 데이터를 동시에 보내려다 부딪치는 경우

- Token Ring

  - Token : LAN 망에서 사용되는 것으로 특별한 제어 프레임을 뜻함

- Token Bus

  - s → a → b → c → d → s
  - s → a → b → s → c → d

![image-20230223182516160](C:\Users\X-note\Desktop\새 폴더\TIL\CS\네트워크\3 네트워크 기술\assets/image-20230223182516160.png)





#### MAN

- 도시 규모
- DQDB(Distributed Queue Dual Bus)

![image-20230223182551170](C:\Users\X-note\Desktop\새 폴더\TIL\CS\네트워크\3 네트워크 기술\assets/image-20230223182551170.png)



#### WAN

- 국가 이상의 넓은 지역
- 점대점(Point-to-point) 환경
- 전송 및 교환 기능 필요

![image-20230223182626687](C:\Users\X-note\Desktop\새 폴더\TIL\CS\네트워크\3 네트워크 기술\assets/image-20230223182626687.png)

