# usage: pypi_publish.sh USERNAME PASSWORD

rm -f MANIFEST
rm -rf sdist

python setup.py sdist
twine -u $1 -p $2 upload dist/*