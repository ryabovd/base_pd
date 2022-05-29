color B
datetime_now=`date "+%Y-%m-%d %H:%M"`
git config --global user.name "ryabovd"
git config --global user.email "ryabovd@outlook.com"
git add *
git commit -m "$datetime_now"
git branch -M main
git remote add origin https://github.com/ryabovd/base_pd.git
git push -u origin main

