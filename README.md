# Azure Function - 1 Function, N entry-points!

This demo show Azure Function write in Python hosted in Azure with 2 entry points.

## Step 1:

1. Create an Azure Function inside Azure.
2. Create an new Deploy inside the Deployment 3. Center to get all Access Tokens created on your Repo.
4. Adjust the Action file properly to use your Tokens.

## Step 2:

1. Run the Action
2. Get the app_key on the Portal inside your Azure Function created before.

## Step 3:

1. Check the functions in your browser. 

`
https://<function_name>.azurewebsites.net/api/function-a?code=<app_key>
`

or

`
https://<function_name>.azurewebsites.net/api/function-b?code=<app_key>
`

The response must be: `Function A completed` or `Function B completed` depending on wicth function you wanna test.

## Step 4:

1. Explore the logs, monitoring and metrics on the portal!
