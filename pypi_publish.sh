# usage: pypi_publish.sh USERNAME PASSWORD

rm -rf dist
rm -rf errant.egg-info

python setup.py sdist
twine upload -u $1 -p $2 dist/*