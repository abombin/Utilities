cd ~/github/
for i in $(ls -d *)
do
	cd "$i"
	git pull origin main
	cd ../
done

