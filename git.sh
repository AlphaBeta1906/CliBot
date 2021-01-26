
#this script were used to automate github workflow
git add .
echo 'enter message'
read  message

git commit -m "$message"

echo 'enter branch'
read  branch

echo 'enter origin branch'
read originBranch

git push origin $branch:$originBranch

echo 'finish'