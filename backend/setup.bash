# Script that installs node modules for the server to run off of
rm package*
rm -fr node_modules

npm init

npm install --save express
npm install --save dotenv
npm install --save sqlite3

npm install --save -D nodemon