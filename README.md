# Korea_UHI_Python

가상환경 리스트 보기
> conda env list

가상환경 생성하기
> conda create -n Korea_UHI_Python_env_win python=3.8

가상환경 시작하기
> conda activate Korea_UHI_Python_env_win

deactivate 가상환경 종료
> conda deactivate

install module
> conda install cartopy
> pip install windrose
> conda install -c conda-forge pyhdf
> conda install basemap 
> conda install basemap-data-hires 
> conda install numpy pandas matplotlib
> conda install spyder
> conda install spyder

 

가상환경 내보내기 (export)
> conda env export > Korea_UHI_Python_env_win.yaml


.yaml 파일로 새로운 가상환경 만들기
> conda env create -f Korea_UHI_Python_env_win.yaml


가상환경 리스트 출력
> conda env list
 
가상환경 제거하기
> conda env remove -n Korea_UHI_Python_env_win
