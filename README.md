# Korea_UHI_Python

가상환경 리스트 보기
> conda env list

windows
가상환경 생성하기 (windows)
> conda create -n Korea_UHI_Python_env_win python=3.8

가상환경 시작하기 (windows)
> conda activate Korea_UHI_Python_env_win

install module
> conda install cartopy
> pip install windrose
> conda install -c conda-forge pyhdf
> conda install basemap 
> conda install basemap-data-hires 
> conda install numpy pandas matplotlib
> conda install spyder

가상환경 내보내기 (windows)
> conda env export > Korea_UHI_Python_env_win.yaml

.yaml 파일로 새로운 가상환경 만들기  (windows)
> conda env create -f Korea_UHI_Python_env_win.yaml

deactivate 가상환경 종료
> conda deactivate

가상환경 제거하기 (windows)
> conda env remove -n Korea_UHI_Python_env_win


ubuntu

가상환경 생성하기 (ubuntu)
> conda create -n Korea_UHI_Python_env python=3.8

가상환경 시작하기 (ubuntu)
> conda activate Korea_UHI_Python_env

install module
> conda install cartopy
> pip install windrose
> conda install -c conda-forge pyhdf
> conda install basemap
> conda install basemap-data-hires
> conda install numpy pandas matplotlib
> conda install spyder

가상환경 내보내기 (ubuntu)
> conda env export > Korea_UHI_Python_env.yaml

.yaml 파일로 새로운 가상환경 만들기 (ubuntu)
> conda env create -f Korea_UHI_Python_env.yaml

deactivate 가상환경 종료
> conda deactivate

가상환경 제거하기(ubuntu)
> conda env remove -n Korea_UHI_Python_env
