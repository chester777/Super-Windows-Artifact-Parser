# Super Windows Artifact Parser
Super Windows Artifact Parser 는 Window 운영체제가 자동적으로 생성한 Artifact를 통해 Digital Forensic 관점에서 필요한 흔적을 통합적으로 Parsing 하여 제공하는 도구입니다.

Windows Artifact를 하나씩 공부하면서 만들고있어 시간이 좀 오래 걸릴 것 같은데 언젠간 완성 되겠지요..

코드리뷰 후 이슈 생성은 언제나 환영입니다.

## done artifact lists

## in progress artifact lists
* Prefetch
* Result Output
  * SQLite

## to do lists
* Result Output
  * CSV
* Registry
  * Basic Information
  * AppCache
  * USB Connections
  * Shell Bag
  * Task Schedule
  * Auto Runs
* Jump List
* Lnk File
* Event Log
* Job File
* AmCache
* VSS(VSC)
* File System Log
* User Interface

## dependencies
라이브러리는 최대한 standard 만 가져다 쓰려고 했는데 구현에 한계가 있는 경우는 외부 라이브러리를 사용했습니다.
* wimlib - https://github.com/0xGiddi/python-wimlib : Windows 10 Prefetch 압축해제 시 사용. pip로 설치 안됨. 나중에 배포할때 어떡하냐..