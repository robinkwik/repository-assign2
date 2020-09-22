# This shell script reorganizes files in a directory containing spectral reflectance data from ASD measurements and code which was created to calculate normalized difference vegetation index (NDVI) from spectral reflectance data.
# Therefore, this shell script creates data, doc, results, and src directories within the repository.

cd "$1"     # This changes directory to where user specifies in command line.
mkdir data     # This will contain raw data such as the ASD spectral reflectance measurements.
mkdir doc     # This will include text files other than requirements.txt.
mkdir results     # This will contain outputs of code execution.
mkdir src     # This will include code

git mv *.csv data/
git mv *.txt doc/
git mv *.xlsx *.png results/
git mv *.py src/

touch requirements.txt

cd results/
mkdir tables
mkdir plots
git mv *.png plots/
git mv *.xlsx tables/

cd ../
cd src/
mkdir spectral-reflectance
mkdir ndvi

