
#this script were used to automate github workflow
echo 'enter file name to commit or type . to add all file'
read file
if [[ $file == "." ]]
then 
	git add .
else
	git add $file
fi

echo 'enter message'
read  message

git commit -m "$message"

echo 'enter local branch'
read  branch

echo 'enter origin branch'
read originBranch

git push origin $branch:$originBranch

echo 'finish'