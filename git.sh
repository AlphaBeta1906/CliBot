
#this script were used to automate github workflow
git add .
echo 'enter message'
read  message

git commit -m "$message"

echo 'enter branch'
read  branch

git push origin $branch:edit

echo 'finish'


