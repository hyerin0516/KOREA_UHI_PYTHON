# KOREA_UHI_PYTHON

가상환경 리스트 보기
> conda env list

가상환경 생성하기
> conda create -n Korea_UHI_Python_env_win python=3.8

가상환경 시작하기
> conda activate Korea_UHI_Python_env_win

deactivate 가상환경 종료
> conda deactivate

install module
> conda install numpy pandas matplotlib
> conda install spyder 
> conda install basemap 
> conda install basemap-data-hires 
> conda install -c conda-forge pyhdf 
> pip install cartopy (에러남, 꼭 필요한 것은 아님)

가상환경 내보내기 (export)
> conda env export > Korea_UHI_Python_env_win.yaml


.yaml 파일로 새로운 가상환경 만들기
> conda env create -f Korea_UHI_Python_env_win.yaml


가상환경 리스트 출력
> conda env list
 
가상환경 제거하기
> conda env remove -n Korea_UHI_Python_env_win
