color B
set DATE_NOW=%date%
echo %date%
pause
git config --global user.name "ryabovd"
git config --global user.email "ryabovd@outlook.com"
git add .
git commit -m %date%
git branch -M main
git remote add origin https://github.com/ryabovd/base_pd.git
git push -u origin main
pause

