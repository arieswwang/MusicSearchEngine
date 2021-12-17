# CS6200-Final-Project

For Solr admin:
Route to the solr directory, Activate solr using " bin/solr start -e cloud"
press enter till the end 
Create a core using : " bin/solr create -c lyric_core " 
Run load_files.py
Visit the solr link. Go to collections, select lyric_core, execute query.
To delete: bin/solr stop -all
           rm -Rf example/cloud/

To activate web app:
Route to app, activate the environment using “source venv/bin/activate”
export FLASK_APP=index
Then flask run
To end: Ctrl+c and deactivate

